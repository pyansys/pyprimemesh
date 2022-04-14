__all__ = [ 'GRPCCommunicator' ]
import grpc
import ansys.meshing.prime.internals.json_utils as json
from ansys.meshing.prime.internals.error_handling import (
    communicator_error_handler,
    error_code_handler
)
from ansys.meshing.prime.internals.communicator import Communicator
import ansys.meshing.prime.internals.config as config
import ansys.meshing.prime.internals.defaults as defaults
from ansys.api.meshing.prime.v1 import prime_pb2, prime_pb2_grpc

MAX_MESSAGE_LENGTH = 4194310
# Keep some buffer for gRPC metadata that it may want to send
BUFFER_MESSAGE_LENGTH = MAX_MESSAGE_LENGTH - 100

def make_chunks(data, chunk_size):
    n = max(1, chunk_size)
    return (data[i:i+n] for i in range(0, len(data), n))

def request_iterator(model_id, data, message_cls, model_cls, content_cls, completion_cls):
    yield message_cls(model=model_cls(object_id=model_id))
    for chunk in make_chunks(data, BUFFER_MESSAGE_LENGTH):
        yield message_cls(content=content_cls(data=chunk))
    yield message_cls(completion_token=completion_cls())

def get_response_messages(response_generator):
    for response in response_generator:
        if response.HasField('completion_token'):
            break

        assert response.HasField('content')
        yield response.content

def get_response(response_iterator, separator):
    return separator.join(response.data for response in get_response_messages(response_iterator))

class GRPCCommunicator(Communicator):
    def __init__(self, ip: str, port: int,
                 timeout: float, credentials = None):
        ip_addr = f"{ip}:{port}"
        if credentials is None:
            self._channel = grpc.insecure_channel(
                                ip_addr,
                                options=[
                                    ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
                                    ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)
                                ])
        else:
            self._channel = grpc.secure_channel(
                                ip_addr,
                                credentials,
                                options=[
                                    ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
                                    ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)
                                ])
        try:
            grpc.channel_ready_future(self._channel).result(timeout=timeout)
        except grpc.FutureTimeoutError as err:
            raise ConnectionError(
                    'Failed to connect to Server in given timeout of 10 secs') from err
        self._stub = prime_pb2_grpc.PrimeStub(self._channel)

    @error_code_handler
    @communicator_error_handler
    def serve(self, model, command, *args, **kwargs) -> dict:
        if self._stub is not None:
            command = { "Command" : command }
            if(len(args) > 0 ):
                command.update({ "ObjectID" : args[0]})
            if (kwargs is not None):
                if "args" in kwargs:
                    command.update({ "Args" : kwargs["args"]})

            if config.is_optimizing_numpy_arrays():
                response = self._stub.ServeJsonBinary(
                                request_iterator(
                                    model._object_id,
                                    json.dumps(command),
                                    prime_pb2.BinaryMessage,
                                    prime_pb2.Model,
                                    prime_pb2.BinaryJsonContent,
                                    prime_pb2.MessageCompletionToken))
                message = get_response(response, b'')
            else:
                response = self._stub.ServeJson(
                                request_iterator(
                                    model._object_id,
                                    json.dumps(command),
                                    prime_pb2.StringMessage,
                                    prime_pb2.Model,
                                    prime_pb2.StringJsonContent,
                                    prime_pb2.MessageCompletionToken))
                message = get_response(response, '')
            if defaults.print_communicator_stats():
                import logging
                logging.getLogger("PyPrime").info(f'Data Transfer: Received {len(message)} bytes')
            return json.loads(message)
        else:
            raise RuntimeError("No connection with server")

    def initialize_params(self, model, param_name: str, *args) -> dict:
        if self._stub is not None:
            command = { "ParamName" : param_name }
            with config.numpy_array_optimization_disabled():
                response = self._stub.GetParamDefaultJson(
                                request_iterator(
                                    model._object_id,
                                    json.dumps(command),
                                    prime_pb2.StringMessage,
                                    prime_pb2.Model,
                                    prime_pb2.StringJsonContent,
                                    prime_pb2.MessageCompletionToken))
                message = get_response(response, '')
                result = json.loads(message)
            return result
        else:
            raise RuntimeError("No connection with server")

    def run_on_server(self, model, recipe: str) -> dict:
        if self._stub is not None:
            commands = recipe
            response = self._stub.RunOnServer(
                            request_iterator(
                                model._object_id,
                                commands,
                                prime_pb2.StringMessage,
                                prime_pb2.Model,
                                prime_pb2.StringJsonContent,
                                prime_pb2.MessageCompletionToken))
            message = get_response(response, '')
            with config.numpy_array_optimization_disabled():
                result = json.loads(message)
            if "Error" in result:
                raise RuntimeError(result['Error'])
            return result
        else:
            raise RuntimeError("No connection with server")

    @error_code_handler
    @communicator_error_handler
    def import_cad(self, model, file_name: str, *args) -> dict:
        if self._stub is not None:
            params = { "filename" : file_name }
            if(len(args) > 0 ):
                params.update(args[0])
            with config.numpy_array_optimization_disabled():
                response = self._stub.ImportCAD(
                                request_iterator(
                                    model._object_id,
                                    json.dumps(params),
                                    prime_pb2.StringMessage,
                                    prime_pb2.Model,
                                    prime_pb2.StringJsonContent,
                                    prime_pb2.MessageCompletionToken))
            message = get_response(response, '')
            result = json.loads(message)
            if "Error" in result:
                raise RuntimeError(result['Error'])
            return result
        else:
            raise RuntimeError("No connection with server")

    def close(self):
        self._stub = None
        if self._channel is not None:
            self._channel.close()
            self._channel = None

    def __del__(self):
        self.close()
