import logging
from ansys.meshing.prime.internals.utils import terminate_process
from ansys.meshing.prime.core.model import Model
import ansys.meshing.prime.internals.defaults as defaults

__all__ = [ 'Client' ]

class Client(object):
    '''Client class for PyPRIME.'''
    def __init__(self, *,
                 server_process=None,
                 ip: str=defaults.ip(),
                 port: int=defaults.port(),
                 timeout: float=defaults.connection_timeout(),
                 credentials=None,
                 **kwargs):
        self._default_model: Model = None
        local = kwargs.get('local', False)
        if local and server_process is not None:
            raise ValueError('Local client cannot be instantiated with a server process')
        self._local = local
        self._process = server_process
        self._comm = None
        if not local:
            try:
                from ansys.meshing.prime.internals.grpc_communicator import GRPCCommunicator
                self._comm = GRPCCommunicator(ip, port, timeout, credentials=credentials)
            except ImportError as err:
                logging.getLogger('PyPrime').error(
                    f'Failed to load grpc_communicator with message: {err.msg}')
                raise
            except ConnectionError:
                self.exit()

                logging.getLogger('PyPrime').error('Failed to connect to PRIME GRPC server')
                raise
        else:
            try:
                from ansys.meshing.prime.internals.prime_communicator import PrimeCommunicator
                self._comm = PrimeCommunicator()
            except ImportError as err:
                logging.getLogger('PyPrime').error(
                    f'Failed to load prime_communicator with message: {err.msg}')

    @property
    def model(self):
        '''Get model associated with the client.'''
        if self._default_model is None:
            # This assumes that the Model is always object id 1....
            self._default_model = Model(self._comm, 1, 1, "Default")
        return self._default_model

    def run_on_server(self, recipe : str):
        '''Run a recipe on server.

        Parameters
        ----------
        recipe: str
            Recipe to run on the server. This needs to be a valid
            python script.
        '''
        if self._comm is not None:
            result = self._comm.run_on_server(recipe)
            return result['Results']

    def exit(self):
        '''Close the connection with the server

        If the client had launched the server, then this will also
        kill the server process.

        Examples
        --------
        >>> import ansys.meshing.prime as prime
        >>> pyprime = prime.launch_prime() # This will launch a server process
        >>> model = pyprime.model
        >>> fileio = prime.FileIO(model)
        >>> result = fileio.read_pmdat('example.pmdat', prime.FileReadParams(model=model))
        >>> print(result)
        >>> pyprime.exit() # Sever connection with server and kill server
        '''
        if self._comm is not None:
            self._comm.close()
            self._comm = None
        if self._process is not None:
            assert self._local == False
            terminate_process(self._process)
            self._process = None

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.exit()
