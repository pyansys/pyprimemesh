""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any

import logging
from ansys.meshing.prime.internals import utils

class Model(CoreObject, CommunicationManager):
    """ 
    

    Description 
    ----------- 
    """ 

    def __init__(self, comm, id: int, object_id: int, name: str):
        """ Initialize Model """
        self._comm = comm
        self._logger = logging.getLogger("PyPrime")
        self._id = id
        self._object_id = object_id
        self._name = name

    def _print_logs_before_command(self, command, args):
        utils.print_logs_before_command(self._logger, command, args)

    def _print_logs_after_command(self, command, args = None):
        utils.print_logs_after_command(self._logger, command, args)

    
    def get_child_objects_json(self) -> str:
        """  Gets child objects of model in JSON format.

        Description 
        ----------- 
        Used to create proxy child objects of the model at client side.
        Client side model store the proxy child objects(e.g Part, TopoData, ControlData, etc), those can be queried directly from client side model.

        Parameters 
        ---------- 

        Return 
        ------ 
        String
             Returns the JSON format which can be loaded to create proxy child objects of the model.

        Note 
        ---- 
        This method is used by FileIO to synchronize model after read or append files.
        User may not need to call this API explicitly.

        
        Example 
        ------- 
        
        >>> results = model.get_child_objects_json()

        """
        args = {}
        command_name = "PrimeMesh::Model/GetChildObjectsJson"
        self._print_logs_before_command("get_child_objects_json", args)
        result = self._comm.serve(command_name, self.object_id, args=args)
        self._print_logs_after_command("get_child_objects_json")
        return result
    
    @property
    def id(self):
        """ Get id """
        return self._id
    
    @property
    def object_id(self):
        """ GetObjectId """
        return self._object_id
    @property
    def name(self):
        """ Get name """
        return self._name
    
    @name.setter
    def name(self, name):
        """ Set the name """
        self._name = name
    
