""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any

class Wrapper(CoreObject):
    """Provides operations to generate surface mesh using wrapper technology.

    """

    def __init__(self, model: CommunicationManager):
        """ Initialize Wrapper """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::Wrapper/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for Wrapper. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for Wrapper. """
        command_name = "PrimeMesh::Wrapper/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def wrap(self, wrapper_control_id : int, params : WrapParams) -> WrapResult:
        """ Performs wrapping with specified controls in wrapper control and with provided parameters.


        Parameters
        ----------
        wrapper_control_id : int
            Id of wrapper control.
        params : WrapParams
            Wrap Parameters.

        Returns
        -------
        WrapResult
            Returns the Wrap Results.


        Examples
        --------
        >>> results = wrapper.wrap(wrapper_control_id, params)

        """
        args = {"wrapper_control_id" : wrapper_control_id,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Wrapper/Wrap"
        self._model._print_logs_before_command("wrap", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("wrap", WrapResult(model = self._model, json_data = result))
        return WrapResult(model = self._model, json_data = result)

    def improve_quality(self, part_id : int, params : WrapperImproveQualityParams) -> WrapperImproveResult:
        """ Improve the surface quality and resolve connectivity issues like intersections, multi, free, spikes, point contacts and so on.


        Parameters
        ----------
        part_id : int
            ID of part.
        params : WrapperImproveQualityParams
            Wrapper improve quality parameters.

        Returns
        -------
        WrapperImproveResult
            Returns the Wrapper improve result.


        Examples
        --------
        >>> result = wrapper.improve_quality(part_id, params)

        """
        args = {"part_id" : part_id,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Wrapper/ImproveQuality"
        self._model._print_logs_before_command("improve_quality", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("improve_quality", WrapperImproveResult(model = self._model, json_data = result))
        return WrapperImproveResult(model = self._model, json_data = result)
