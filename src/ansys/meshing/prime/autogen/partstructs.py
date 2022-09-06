""" Auto-generated file. DO NOT MODIFY """
# Copyright 2023 ANSYS, Inc.
# Unauthorized use, distribution, or duplication is prohibited.
import enum
from typing import Dict, Any, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class CellZoneletType(enum.IntEnum):
    """Types of cell zonelet.
    """
    DEAD = 0
    """Cell zonelet type is dead."""
    FLUID = 1
    """Cell zonelet type is fluid."""
    SOLID = 17
    """Cell zonelet type is solid."""

class ZoneType(enum.IntEnum):
    """ZoneType decides the type of zone.
    """
    EDGE = 1
    """Denotes the zone is edge zone."""
    FACE = 2
    """Denotes the zone is face zone."""
    VOLUME = 3
    """Denotes the zone is volume zone."""

class VolumeNamingType(enum.IntEnum):
    """Indicate source types used to name volumes.
    """
    BYFACELABEL = 1
    """Option to use face label name as source to name volumes."""
    BYFACEZONE = 2
    """Option to use face zone name as source to name volumes."""

class BoundingBox(CoreObject):
    """Provides information about the definition of a bounding box.
    """
    _default_params = {}

    def __initialize(
            self,
            xmin: float,
            ymin: float,
            zmin: float,
            xmax: float,
            ymax: float,
            zmax: float):
        self._xmin = xmin
        self._ymin = ymin
        self._zmin = zmin
        self._xmax = xmax
        self._ymax = ymax
        self._zmax = zmax

    def __init__(
            self,
            model: CommunicationManager=None,
            xmin: float = None,
            ymin: float = None,
            zmin: float = None,
            xmax: float = None,
            ymax: float = None,
            zmax: float = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the BoundingBox.

        Parameters
        ----------
        model: Model
            Model to create a BoundingBox object with default parameters.
        xmin: float, optional
            Minimal X coordinate of the bounding box.
        ymin: float, optional
            Minimal Y coordinate of the bounding box.
        zmin: float, optional
            Minimal Z coordinate of the bounding box.
        xmax: float, optional
            Maximal X coordinate of the bounding box.
        ymax: float, optional
            Maximal Y coordinate of the bounding box.
        zmax: float, optional
            Maximal Z coordinate of the bounding box.
        json_data: dict, optional
            JSON dictionary to create a BoundingBox object with provided parameters.

        Examples
        --------
        >>> bounding_box = prime.BoundingBox(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["xmin"],
                json_data["ymin"],
                json_data["zmin"],
                json_data["xmax"],
                json_data["ymax"],
                json_data["zmax"])
        else:
            all_field_specified = all(arg is not None for arg in [xmin, ymin, zmin, xmax, ymax, zmax])
            if all_field_specified:
                self.__initialize(
                    xmin,
                    ymin,
                    zmin,
                    xmax,
                    ymax,
                    zmax)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "BoundingBox")["BoundingBox"]
                    self.__initialize(
                        xmin if xmin is not None else ( BoundingBox._default_params["xmin"] if "xmin" in BoundingBox._default_params else json_data["xmin"]),
                        ymin if ymin is not None else ( BoundingBox._default_params["ymin"] if "ymin" in BoundingBox._default_params else json_data["ymin"]),
                        zmin if zmin is not None else ( BoundingBox._default_params["zmin"] if "zmin" in BoundingBox._default_params else json_data["zmin"]),
                        xmax if xmax is not None else ( BoundingBox._default_params["xmax"] if "xmax" in BoundingBox._default_params else json_data["xmax"]),
                        ymax if ymax is not None else ( BoundingBox._default_params["ymax"] if "ymax" in BoundingBox._default_params else json_data["ymax"]),
                        zmax if zmax is not None else ( BoundingBox._default_params["zmax"] if "zmax" in BoundingBox._default_params else json_data["zmax"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            xmin: float = None,
            ymin: float = None,
            zmin: float = None,
            xmax: float = None,
            ymax: float = None,
            zmax: float = None):
        """Set the default values of BoundingBox.

        Parameters
        ----------
        xmin: float, optional
            Minimal X coordinate of the bounding box.
        ymin: float, optional
            Minimal Y coordinate of the bounding box.
        zmin: float, optional
            Minimal Z coordinate of the bounding box.
        xmax: float, optional
            Maximal X coordinate of the bounding box.
        ymax: float, optional
            Maximal Y coordinate of the bounding box.
        zmax: float, optional
            Maximal Z coordinate of the bounding box.
        """
        args = locals()
        [BoundingBox._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of BoundingBox.

        Examples
        --------
        >>> BoundingBox.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in BoundingBox._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["xmin"] = self._xmin
        json_data["ymin"] = self._ymin
        json_data["zmin"] = self._zmin
        json_data["xmax"] = self._xmax
        json_data["ymax"] = self._ymax
        json_data["zmax"] = self._zmax
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "xmin :  %s\nymin :  %s\nzmin :  %s\nxmax :  %s\nymax :  %s\nzmax :  %s" % (self._xmin, self._ymin, self._zmin, self._xmax, self._ymax, self._zmax)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def xmin(self) -> float:
        """Minimal X coordinate of the bounding box.
        """
        return self._xmin

    @xmin.setter
    def xmin(self, value: float):
        self._xmin = value

    @property
    def ymin(self) -> float:
        """Minimal Y coordinate of the bounding box.
        """
        return self._ymin

    @ymin.setter
    def ymin(self, value: float):
        self._ymin = value

    @property
    def zmin(self) -> float:
        """Minimal Z coordinate of the bounding box.
        """
        return self._zmin

    @zmin.setter
    def zmin(self, value: float):
        self._zmin = value

    @property
    def xmax(self) -> float:
        """Maximal X coordinate of the bounding box.
        """
        return self._xmax

    @xmax.setter
    def xmax(self, value: float):
        self._xmax = value

    @property
    def ymax(self) -> float:
        """Maximal Y coordinate of the bounding box.
        """
        return self._ymax

    @ymax.setter
    def ymax(self, value: float):
        self._ymax = value

    @property
    def zmax(self) -> float:
        """Maximal Z coordinate of the bounding box.
        """
        return self._zmax

    @zmax.setter
    def zmax(self, value: float):
        self._zmax = value

class ComputeVolumesResults(CoreObject):
    """Results associated with compute volumes.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            error_locations: Iterable[float],
            volumes: Iterable[int],
            material_point_volumes: Iterable[int],
            external_open_face_zonelets: Iterable[int],
            warning_codes: List[WarningCode]):
        self._error_code = ErrorCode(error_code)
        self._error_locations = error_locations if isinstance(error_locations, np.ndarray) else np.array(error_locations, dtype=np.double)
        self._volumes = volumes if isinstance(volumes, np.ndarray) else np.array(volumes, dtype=np.int32)
        self._material_point_volumes = material_point_volumes if isinstance(material_point_volumes, np.ndarray) else np.array(material_point_volumes, dtype=np.int32)
        self._external_open_face_zonelets = external_open_face_zonelets if isinstance(external_open_face_zonelets, np.ndarray) else np.array(external_open_face_zonelets, dtype=np.int32)
        self._warning_codes = warning_codes

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            error_locations: Iterable[float] = None,
            volumes: Iterable[int] = None,
            material_point_volumes: Iterable[int] = None,
            external_open_face_zonelets: Iterable[int] = None,
            warning_codes: List[WarningCode] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ComputeVolumesResults.

        Parameters
        ----------
        model: Model
            Model to create a ComputeVolumesResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        error_locations: Iterable[float], optional
            Coordinates of problematic locations in the surface mesh.
        volumes: Iterable[int], optional
            Ids of computed volumes.
        material_point_volumes: Iterable[int], optional
            Ids of computed volumes enclosing material points.
        external_open_face_zonelets: Iterable[int], optional
            Face zonelet ids that are in external space and not part of any computed volumes.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the compute volumes.
        json_data: dict, optional
            JSON dictionary to create a ComputeVolumesResults object with provided parameters.

        Examples
        --------
        >>> compute_volumes_results = prime.ComputeVolumesResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"]),
                json_data["errorLocations"],
                json_data["volumes"],
                json_data["materialPointVolumes"],
                json_data["externalOpenFaceZonelets"],
                [WarningCode(data) for data in json_data["warningCodes"]])
        else:
            all_field_specified = all(arg is not None for arg in [error_code, error_locations, volumes, material_point_volumes, external_open_face_zonelets, warning_codes])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    error_locations,
                    volumes,
                    material_point_volumes,
                    external_open_face_zonelets,
                    warning_codes)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "ComputeVolumesResults")["ComputeVolumesResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( ComputeVolumesResults._default_params["error_code"] if "error_code" in ComputeVolumesResults._default_params else ErrorCode(json_data["errorCode"])),
                        error_locations if error_locations is not None else ( ComputeVolumesResults._default_params["error_locations"] if "error_locations" in ComputeVolumesResults._default_params else json_data["errorLocations"]),
                        volumes if volumes is not None else ( ComputeVolumesResults._default_params["volumes"] if "volumes" in ComputeVolumesResults._default_params else json_data["volumes"]),
                        material_point_volumes if material_point_volumes is not None else ( ComputeVolumesResults._default_params["material_point_volumes"] if "material_point_volumes" in ComputeVolumesResults._default_params else json_data["materialPointVolumes"]),
                        external_open_face_zonelets if external_open_face_zonelets is not None else ( ComputeVolumesResults._default_params["external_open_face_zonelets"] if "external_open_face_zonelets" in ComputeVolumesResults._default_params else json_data["externalOpenFaceZonelets"]),
                        warning_codes if warning_codes is not None else ( ComputeVolumesResults._default_params["warning_codes"] if "warning_codes" in ComputeVolumesResults._default_params else [WarningCode(data) for data in json_data["warningCodes"]]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            error_locations: Iterable[float] = None,
            volumes: Iterable[int] = None,
            material_point_volumes: Iterable[int] = None,
            external_open_face_zonelets: Iterable[int] = None,
            warning_codes: List[WarningCode] = None):
        """Set the default values of ComputeVolumesResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        error_locations: Iterable[float], optional
            Coordinates of problematic locations in the surface mesh.
        volumes: Iterable[int], optional
            Ids of computed volumes.
        material_point_volumes: Iterable[int], optional
            Ids of computed volumes enclosing material points.
        external_open_face_zonelets: Iterable[int], optional
            Face zonelet ids that are in external space and not part of any computed volumes.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the compute volumes.
        """
        args = locals()
        [ComputeVolumesResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ComputeVolumesResults.

        Examples
        --------
        >>> ComputeVolumesResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ComputeVolumesResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["errorCode"] = self._error_code
        json_data["errorLocations"] = self._error_locations
        json_data["volumes"] = self._volumes
        json_data["materialPointVolumes"] = self._material_point_volumes
        json_data["externalOpenFaceZonelets"] = self._external_open_face_zonelets
        json_data["warningCodes"] = [data for data in self._warning_codes]
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nerror_locations :  %s\nvolumes :  %s\nmaterial_point_volumes :  %s\nexternal_open_face_zonelets :  %s\nwarning_codes :  %s" % (self._error_code, self._error_locations, self._volumes, self._material_point_volumes, self._external_open_face_zonelets, '[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def error_locations(self) -> Iterable[float]:
        """Coordinates of problematic locations in the surface mesh.
        """
        return self._error_locations

    @error_locations.setter
    def error_locations(self, value: Iterable[float]):
        self._error_locations = value

    @property
    def volumes(self) -> Iterable[int]:
        """Ids of computed volumes.
        """
        return self._volumes

    @volumes.setter
    def volumes(self, value: Iterable[int]):
        self._volumes = value

    @property
    def material_point_volumes(self) -> Iterable[int]:
        """Ids of computed volumes enclosing material points.
        """
        return self._material_point_volumes

    @material_point_volumes.setter
    def material_point_volumes(self, value: Iterable[int]):
        self._material_point_volumes = value

    @property
    def external_open_face_zonelets(self) -> Iterable[int]:
        """Face zonelet ids that are in external space and not part of any computed volumes.
        """
        return self._external_open_face_zonelets

    @external_open_face_zonelets.setter
    def external_open_face_zonelets(self, value: Iterable[int]):
        self._external_open_face_zonelets = value

    @property
    def warning_codes(self) -> List[WarningCode]:
        """Warning codes associated with the compute volumes.
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, value: List[WarningCode]):
        self._warning_codes = value

class ComputeTopoVolumesResults(CoreObject):
    """Results associated with compute topovolumes.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            error_locations: Iterable[float],
            topo_volumes: Iterable[int],
            material_point_topo_volumes: Iterable[int],
            external_open_topo_faces: Iterable[int],
            new_topo_volumes: Iterable[int],
            deleted_topo_volumes: Iterable[int],
            warning_codes: List[WarningCode]):
        self._error_code = ErrorCode(error_code)
        self._error_locations = error_locations if isinstance(error_locations, np.ndarray) else np.array(error_locations, dtype=np.double)
        self._topo_volumes = topo_volumes if isinstance(topo_volumes, np.ndarray) else np.array(topo_volumes, dtype=np.int32)
        self._material_point_topo_volumes = material_point_topo_volumes if isinstance(material_point_topo_volumes, np.ndarray) else np.array(material_point_topo_volumes, dtype=np.int32)
        self._external_open_topo_faces = external_open_topo_faces if isinstance(external_open_topo_faces, np.ndarray) else np.array(external_open_topo_faces, dtype=np.int32)
        self._new_topo_volumes = new_topo_volumes if isinstance(new_topo_volumes, np.ndarray) else np.array(new_topo_volumes, dtype=np.int32)
        self._deleted_topo_volumes = deleted_topo_volumes if isinstance(deleted_topo_volumes, np.ndarray) else np.array(deleted_topo_volumes, dtype=np.int32)
        self._warning_codes = warning_codes

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            error_locations: Iterable[float] = None,
            topo_volumes: Iterable[int] = None,
            material_point_topo_volumes: Iterable[int] = None,
            external_open_topo_faces: Iterable[int] = None,
            new_topo_volumes: Iterable[int] = None,
            deleted_topo_volumes: Iterable[int] = None,
            warning_codes: List[WarningCode] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ComputeTopoVolumesResults.

        Parameters
        ----------
        model: Model
            Model to create a ComputeTopoVolumesResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        error_locations: Iterable[float], optional
            Coordinates of problematic locations in the surface mesh.
        topo_volumes: Iterable[int], optional
            Ids of all topovolumes computed.
        material_point_topo_volumes: Iterable[int], optional
            Ids of topovolumes enclosing material points.
        external_open_topo_faces: Iterable[int], optional
            Topoface ids that are in external space and not part of any topovolumes.
        new_topo_volumes: Iterable[int], optional
            Ids of new topovolumes computed.
        deleted_topo_volumes: Iterable[int], optional
            Ids of existing topovolumes that got deleted.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the compute topovolumes.
        json_data: dict, optional
            JSON dictionary to create a ComputeTopoVolumesResults object with provided parameters.

        Examples
        --------
        >>> compute_topo_volumes_results = prime.ComputeTopoVolumesResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"]),
                json_data["errorLocations"],
                json_data["topoVolumes"],
                json_data["materialPointTopoVolumes"],
                json_data["externalOpenTopoFaces"],
                json_data["newTopoVolumes"],
                json_data["deletedTopoVolumes"],
                [WarningCode(data) for data in json_data["warningCodes"]])
        else:
            all_field_specified = all(arg is not None for arg in [error_code, error_locations, topo_volumes, material_point_topo_volumes, external_open_topo_faces, new_topo_volumes, deleted_topo_volumes, warning_codes])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    error_locations,
                    topo_volumes,
                    material_point_topo_volumes,
                    external_open_topo_faces,
                    new_topo_volumes,
                    deleted_topo_volumes,
                    warning_codes)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "ComputeTopoVolumesResults")["ComputeTopoVolumesResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( ComputeTopoVolumesResults._default_params["error_code"] if "error_code" in ComputeTopoVolumesResults._default_params else ErrorCode(json_data["errorCode"])),
                        error_locations if error_locations is not None else ( ComputeTopoVolumesResults._default_params["error_locations"] if "error_locations" in ComputeTopoVolumesResults._default_params else json_data["errorLocations"]),
                        topo_volumes if topo_volumes is not None else ( ComputeTopoVolumesResults._default_params["topo_volumes"] if "topo_volumes" in ComputeTopoVolumesResults._default_params else json_data["topoVolumes"]),
                        material_point_topo_volumes if material_point_topo_volumes is not None else ( ComputeTopoVolumesResults._default_params["material_point_topo_volumes"] if "material_point_topo_volumes" in ComputeTopoVolumesResults._default_params else json_data["materialPointTopoVolumes"]),
                        external_open_topo_faces if external_open_topo_faces is not None else ( ComputeTopoVolumesResults._default_params["external_open_topo_faces"] if "external_open_topo_faces" in ComputeTopoVolumesResults._default_params else json_data["externalOpenTopoFaces"]),
                        new_topo_volumes if new_topo_volumes is not None else ( ComputeTopoVolumesResults._default_params["new_topo_volumes"] if "new_topo_volumes" in ComputeTopoVolumesResults._default_params else json_data["newTopoVolumes"]),
                        deleted_topo_volumes if deleted_topo_volumes is not None else ( ComputeTopoVolumesResults._default_params["deleted_topo_volumes"] if "deleted_topo_volumes" in ComputeTopoVolumesResults._default_params else json_data["deletedTopoVolumes"]),
                        warning_codes if warning_codes is not None else ( ComputeTopoVolumesResults._default_params["warning_codes"] if "warning_codes" in ComputeTopoVolumesResults._default_params else [WarningCode(data) for data in json_data["warningCodes"]]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            error_locations: Iterable[float] = None,
            topo_volumes: Iterable[int] = None,
            material_point_topo_volumes: Iterable[int] = None,
            external_open_topo_faces: Iterable[int] = None,
            new_topo_volumes: Iterable[int] = None,
            deleted_topo_volumes: Iterable[int] = None,
            warning_codes: List[WarningCode] = None):
        """Set the default values of ComputeTopoVolumesResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        error_locations: Iterable[float], optional
            Coordinates of problematic locations in the surface mesh.
        topo_volumes: Iterable[int], optional
            Ids of all topovolumes computed.
        material_point_topo_volumes: Iterable[int], optional
            Ids of topovolumes enclosing material points.
        external_open_topo_faces: Iterable[int], optional
            Topoface ids that are in external space and not part of any topovolumes.
        new_topo_volumes: Iterable[int], optional
            Ids of new topovolumes computed.
        deleted_topo_volumes: Iterable[int], optional
            Ids of existing topovolumes that got deleted.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the compute topovolumes.
        """
        args = locals()
        [ComputeTopoVolumesResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ComputeTopoVolumesResults.

        Examples
        --------
        >>> ComputeTopoVolumesResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ComputeTopoVolumesResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["errorCode"] = self._error_code
        json_data["errorLocations"] = self._error_locations
        json_data["topoVolumes"] = self._topo_volumes
        json_data["materialPointTopoVolumes"] = self._material_point_topo_volumes
        json_data["externalOpenTopoFaces"] = self._external_open_topo_faces
        json_data["newTopoVolumes"] = self._new_topo_volumes
        json_data["deletedTopoVolumes"] = self._deleted_topo_volumes
        json_data["warningCodes"] = [data for data in self._warning_codes]
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nerror_locations :  %s\ntopo_volumes :  %s\nmaterial_point_topo_volumes :  %s\nexternal_open_topo_faces :  %s\nnew_topo_volumes :  %s\ndeleted_topo_volumes :  %s\nwarning_codes :  %s" % (self._error_code, self._error_locations, self._topo_volumes, self._material_point_topo_volumes, self._external_open_topo_faces, self._new_topo_volumes, self._deleted_topo_volumes, '[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def error_locations(self) -> Iterable[float]:
        """Coordinates of problematic locations in the surface mesh.
        """
        return self._error_locations

    @error_locations.setter
    def error_locations(self, value: Iterable[float]):
        self._error_locations = value

    @property
    def topo_volumes(self) -> Iterable[int]:
        """Ids of all topovolumes computed.
        """
        return self._topo_volumes

    @topo_volumes.setter
    def topo_volumes(self, value: Iterable[int]):
        self._topo_volumes = value

    @property
    def material_point_topo_volumes(self) -> Iterable[int]:
        """Ids of topovolumes enclosing material points.
        """
        return self._material_point_topo_volumes

    @material_point_topo_volumes.setter
    def material_point_topo_volumes(self, value: Iterable[int]):
        self._material_point_topo_volumes = value

    @property
    def external_open_topo_faces(self) -> Iterable[int]:
        """Topoface ids that are in external space and not part of any topovolumes.
        """
        return self._external_open_topo_faces

    @external_open_topo_faces.setter
    def external_open_topo_faces(self, value: Iterable[int]):
        self._external_open_topo_faces = value

    @property
    def new_topo_volumes(self) -> Iterable[int]:
        """Ids of new topovolumes computed.
        """
        return self._new_topo_volumes

    @new_topo_volumes.setter
    def new_topo_volumes(self, value: Iterable[int]):
        self._new_topo_volumes = value

    @property
    def deleted_topo_volumes(self) -> Iterable[int]:
        """Ids of existing topovolumes that got deleted.
        """
        return self._deleted_topo_volumes

    @deleted_topo_volumes.setter
    def deleted_topo_volumes(self, value: Iterable[int]):
        self._deleted_topo_volumes = value

    @property
    def warning_codes(self) -> List[WarningCode]:
        """Warning codes associated with the compute topovolumes.
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, value: List[WarningCode]):
        self._warning_codes = value

class ComputeVolumesParams(CoreObject):
    """Parameters to compute volumes.
    """
    _default_params = {}

    def __initialize(
            self,
            volume_naming_type: VolumeNamingType,
            create_zone_per_volume: bool,
            material_point_names: List[str]):
        self._volume_naming_type = VolumeNamingType(volume_naming_type)
        self._create_zone_per_volume = create_zone_per_volume
        self._material_point_names = material_point_names

    def __init__(
            self,
            model: CommunicationManager=None,
            volume_naming_type: VolumeNamingType = None,
            create_zone_per_volume: bool = None,
            material_point_names: List[str] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ComputeVolumesParams.

        Parameters
        ----------
        model: Model
            Model to create a ComputeVolumesParams object with default parameters.
        volume_naming_type: VolumeNamingType, optional
            Indicates source type used to name volumes.
        create_zone_per_volume: bool, optional
            Option to create zone per volume computed using volume name.
        material_point_names: List[str], optional
            Material point names provided to identify volumes. Material point names will have precedence over the volume names.
        json_data: dict, optional
            JSON dictionary to create a ComputeVolumesParams object with provided parameters.

        Examples
        --------
        >>> compute_volumes_params = prime.ComputeVolumesParams(model = model)
        """
        if json_data:
            self.__initialize(
                VolumeNamingType(json_data["volumeNamingType"]),
                json_data["createZonePerVolume"],
                json_data["materialPointNames"])
        else:
            all_field_specified = all(arg is not None for arg in [volume_naming_type, create_zone_per_volume, material_point_names])
            if all_field_specified:
                self.__initialize(
                    volume_naming_type,
                    create_zone_per_volume,
                    material_point_names)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "ComputeVolumesParams")["ComputeVolumesParams"]
                    self.__initialize(
                        volume_naming_type if volume_naming_type is not None else ( ComputeVolumesParams._default_params["volume_naming_type"] if "volume_naming_type" in ComputeVolumesParams._default_params else VolumeNamingType(json_data["volumeNamingType"])),
                        create_zone_per_volume if create_zone_per_volume is not None else ( ComputeVolumesParams._default_params["create_zone_per_volume"] if "create_zone_per_volume" in ComputeVolumesParams._default_params else json_data["createZonePerVolume"]),
                        material_point_names if material_point_names is not None else ( ComputeVolumesParams._default_params["material_point_names"] if "material_point_names" in ComputeVolumesParams._default_params else json_data["materialPointNames"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            volume_naming_type: VolumeNamingType = None,
            create_zone_per_volume: bool = None,
            material_point_names: List[str] = None):
        """Set the default values of ComputeVolumesParams.

        Parameters
        ----------
        volume_naming_type: VolumeNamingType, optional
            Indicates source type used to name volumes.
        create_zone_per_volume: bool, optional
            Option to create zone per volume computed using volume name.
        material_point_names: List[str], optional
            Material point names provided to identify volumes. Material point names will have precedence over the volume names.
        """
        args = locals()
        [ComputeVolumesParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ComputeVolumesParams.

        Examples
        --------
        >>> ComputeVolumesParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ComputeVolumesParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["volumeNamingType"] = self._volume_naming_type
        json_data["createZonePerVolume"] = self._create_zone_per_volume
        json_data["materialPointNames"] = self._material_point_names
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "volume_naming_type :  %s\ncreate_zone_per_volume :  %s\nmaterial_point_names :  %s" % (self._volume_naming_type, self._create_zone_per_volume, self._material_point_names)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def volume_naming_type(self) -> VolumeNamingType:
        """Indicates source type used to name volumes.
        """
        return self._volume_naming_type

    @volume_naming_type.setter
    def volume_naming_type(self, value: VolumeNamingType):
        self._volume_naming_type = value

    @property
    def create_zone_per_volume(self) -> bool:
        """Option to create zone per volume computed using volume name.
        """
        return self._create_zone_per_volume

    @create_zone_per_volume.setter
    def create_zone_per_volume(self, value: bool):
        self._create_zone_per_volume = value

    @property
    def material_point_names(self) -> List[str]:
        """Material point names provided to identify volumes. Material point names will have precedence over the volume names.
        """
        return self._material_point_names

    @material_point_names.setter
    def material_point_names(self, value: List[str]):
        self._material_point_names = value

class NamePatternParams(CoreObject):
    """Parameters to be used to match name pattern with names.
    """
    _default_params = {}

    def __initialize(
            self):
        pass

    def __init__(
            self,
            model: CommunicationManager=None,
            json_data : dict = None,
             **kwargs):
        """Initializes the NamePatternParams.

        Parameters
        ----------
        model: Model
            Model to create a NamePatternParams object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a NamePatternParams object with provided parameters.

        Examples
        --------
        >>> name_pattern_params = prime.NamePatternParams(model = model)
        """
        if json_data:
            self.__initialize()
        else:
            all_field_specified = all(arg is not None for arg in [])
            if all_field_specified:
                self.__initialize()
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "NamePatternParams")["NamePatternParams"]
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of NamePatternParams.

        """
        args = locals()
        [NamePatternParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of NamePatternParams.

        Examples
        --------
        >>> NamePatternParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in NamePatternParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "" % ()
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

class PartSummaryParams(CoreObject):
    """Parameters to control part summary results.
    """
    _default_params = {}

    def __initialize(
            self,
            print_id: bool,
            print_mesh: bool):
        self._print_id = print_id
        self._print_mesh = print_mesh

    def __init__(
            self,
            model: CommunicationManager=None,
            print_id: bool = None,
            print_mesh: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the PartSummaryParams.

        Parameters
        ----------
        model: Model
            Model to create a PartSummaryParams object with default parameters.
        print_id: bool, optional
            Boolean to control print ids. The default is false.
        print_mesh: bool, optional
            Boolean to control print mesh information. The default is true.
        json_data: dict, optional
            JSON dictionary to create a PartSummaryParams object with provided parameters.

        Examples
        --------
        >>> part_summary_params = prime.PartSummaryParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["printId"],
                json_data["printMesh"])
        else:
            all_field_specified = all(arg is not None for arg in [print_id, print_mesh])
            if all_field_specified:
                self.__initialize(
                    print_id,
                    print_mesh)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "PartSummaryParams")["PartSummaryParams"]
                    self.__initialize(
                        print_id if print_id is not None else ( PartSummaryParams._default_params["print_id"] if "print_id" in PartSummaryParams._default_params else json_data["printId"]),
                        print_mesh if print_mesh is not None else ( PartSummaryParams._default_params["print_mesh"] if "print_mesh" in PartSummaryParams._default_params else json_data["printMesh"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            print_id: bool = None,
            print_mesh: bool = None):
        """Set the default values of PartSummaryParams.

        Parameters
        ----------
        print_id: bool, optional
            Boolean to control print ids. The default is false.
        print_mesh: bool, optional
            Boolean to control print mesh information. The default is true.
        """
        args = locals()
        [PartSummaryParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of PartSummaryParams.

        Examples
        --------
        >>> PartSummaryParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in PartSummaryParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["printId"] = self._print_id
        json_data["printMesh"] = self._print_mesh
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "print_id :  %s\nprint_mesh :  %s" % (self._print_id, self._print_mesh)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def print_id(self) -> bool:
        """Boolean to control print ids. The default is false.
        """
        return self._print_id

    @print_id.setter
    def print_id(self, value: bool):
        self._print_id = value

    @property
    def print_mesh(self) -> bool:
        """Boolean to control print mesh information. The default is true.
        """
        return self._print_mesh

    @print_mesh.setter
    def print_mesh(self, value: bool):
        self._print_mesh = value

class PartSummaryResults(CoreObject):
    """Results of part summary.
    """
    _default_params = {}

    def __initialize(
            self,
            message: str,
            n_topo_edges: int,
            n_topo_faces: int,
            n_topo_volumes: int,
            n_edge_zonelets: int,
            n_face_zonelets: int,
            n_cell_zonelets: int,
            n_edge_zones: int,
            n_face_zones: int,
            n_volume_zones: int,
            n_labels: int,
            n_nodes: int,
            n_faces: int,
            n_cells: int,
            n_tri_faces: int,
            n_poly_faces: int,
            n_quad_faces: int,
            n_tet_cells: int,
            n_pyra_cells: int,
            n_prism_cells: int,
            n_poly_cells: int,
            n_hex_cells: int,
            n_unmeshed_topo_faces: int):
        self._message = message
        self._n_topo_edges = n_topo_edges
        self._n_topo_faces = n_topo_faces
        self._n_topo_volumes = n_topo_volumes
        self._n_edge_zonelets = n_edge_zonelets
        self._n_face_zonelets = n_face_zonelets
        self._n_cell_zonelets = n_cell_zonelets
        self._n_edge_zones = n_edge_zones
        self._n_face_zones = n_face_zones
        self._n_volume_zones = n_volume_zones
        self._n_labels = n_labels
        self._n_nodes = n_nodes
        self._n_faces = n_faces
        self._n_cells = n_cells
        self._n_tri_faces = n_tri_faces
        self._n_poly_faces = n_poly_faces
        self._n_quad_faces = n_quad_faces
        self._n_tet_cells = n_tet_cells
        self._n_pyra_cells = n_pyra_cells
        self._n_prism_cells = n_prism_cells
        self._n_poly_cells = n_poly_cells
        self._n_hex_cells = n_hex_cells
        self._n_unmeshed_topo_faces = n_unmeshed_topo_faces

    def __init__(
            self,
            model: CommunicationManager=None,
            message: str = None,
            n_topo_edges: int = None,
            n_topo_faces: int = None,
            n_topo_volumes: int = None,
            n_edge_zonelets: int = None,
            n_face_zonelets: int = None,
            n_cell_zonelets: int = None,
            n_edge_zones: int = None,
            n_face_zones: int = None,
            n_volume_zones: int = None,
            n_labels: int = None,
            n_nodes: int = None,
            n_faces: int = None,
            n_cells: int = None,
            n_tri_faces: int = None,
            n_poly_faces: int = None,
            n_quad_faces: int = None,
            n_tet_cells: int = None,
            n_pyra_cells: int = None,
            n_prism_cells: int = None,
            n_poly_cells: int = None,
            n_hex_cells: int = None,
            n_unmeshed_topo_faces: int = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the PartSummaryResults.

        Parameters
        ----------
        model: Model
            Model to create a PartSummaryResults object with default parameters.
        message: str, optional
            Part summary text.
        n_topo_edges: int, optional
            Number of topoedges.
        n_topo_faces: int, optional
            Number of topofaces.
        n_topo_volumes: int, optional
            Number of topovolumes.
        n_edge_zonelets: int, optional
            Number of edge zonelets.
        n_face_zonelets: int, optional
            Number of face zonelets.
        n_cell_zonelets: int, optional
            Number of cell zonelets.
        n_edge_zones: int, optional
            Number of edge zones.
        n_face_zones: int, optional
            Number of face zones.
        n_volume_zones: int, optional
            Number of volume zones.
        n_labels: int, optional
            Number of labels.
        n_nodes: int, optional
            Number of nodes.
        n_faces: int, optional
            Number of faces.
        n_cells: int, optional
            Number of cells.
        n_tri_faces: int, optional
            Number of triangular faces.
        n_poly_faces: int, optional
            Number of polygonal faces.
        n_quad_faces: int, optional
            Number of quadrilateral faces.
        n_tet_cells: int, optional
            Number of tetrahedral cells.
        n_pyra_cells: int, optional
            Number of pyramid cells.
        n_prism_cells: int, optional
            Number of prism cells.
        n_poly_cells: int, optional
            Number of polyhedral cells.
        n_hex_cells: int, optional
            Number of hexahedral cells.
        n_unmeshed_topo_faces: int, optional
            Number of unmeshed topofaces.
        json_data: dict, optional
            JSON dictionary to create a PartSummaryResults object with provided parameters.

        Examples
        --------
        >>> part_summary_results = prime.PartSummaryResults(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["message"],
                json_data["nTopoEdges"],
                json_data["nTopoFaces"],
                json_data["nTopoVolumes"],
                json_data["nEdgeZonelets"],
                json_data["nFaceZonelets"],
                json_data["nCellZonelets"],
                json_data["nEdgeZones"],
                json_data["nFaceZones"],
                json_data["nVolumeZones"],
                json_data["nLabels"],
                json_data["nNodes"],
                json_data["nFaces"],
                json_data["nCells"],
                json_data["nTriFaces"],
                json_data["nPolyFaces"],
                json_data["nQuadFaces"],
                json_data["nTetCells"],
                json_data["nPyraCells"],
                json_data["nPrismCells"],
                json_data["nPolyCells"],
                json_data["nHexCells"],
                json_data["nUnmeshedTopoFaces"])
        else:
            all_field_specified = all(arg is not None for arg in [message, n_topo_edges, n_topo_faces, n_topo_volumes, n_edge_zonelets, n_face_zonelets, n_cell_zonelets, n_edge_zones, n_face_zones, n_volume_zones, n_labels, n_nodes, n_faces, n_cells, n_tri_faces, n_poly_faces, n_quad_faces, n_tet_cells, n_pyra_cells, n_prism_cells, n_poly_cells, n_hex_cells, n_unmeshed_topo_faces])
            if all_field_specified:
                self.__initialize(
                    message,
                    n_topo_edges,
                    n_topo_faces,
                    n_topo_volumes,
                    n_edge_zonelets,
                    n_face_zonelets,
                    n_cell_zonelets,
                    n_edge_zones,
                    n_face_zones,
                    n_volume_zones,
                    n_labels,
                    n_nodes,
                    n_faces,
                    n_cells,
                    n_tri_faces,
                    n_poly_faces,
                    n_quad_faces,
                    n_tet_cells,
                    n_pyra_cells,
                    n_prism_cells,
                    n_poly_cells,
                    n_hex_cells,
                    n_unmeshed_topo_faces)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "PartSummaryResults")["PartSummaryResults"]
                    self.__initialize(
                        message if message is not None else ( PartSummaryResults._default_params["message"] if "message" in PartSummaryResults._default_params else json_data["message"]),
                        n_topo_edges if n_topo_edges is not None else ( PartSummaryResults._default_params["n_topo_edges"] if "n_topo_edges" in PartSummaryResults._default_params else json_data["nTopoEdges"]),
                        n_topo_faces if n_topo_faces is not None else ( PartSummaryResults._default_params["n_topo_faces"] if "n_topo_faces" in PartSummaryResults._default_params else json_data["nTopoFaces"]),
                        n_topo_volumes if n_topo_volumes is not None else ( PartSummaryResults._default_params["n_topo_volumes"] if "n_topo_volumes" in PartSummaryResults._default_params else json_data["nTopoVolumes"]),
                        n_edge_zonelets if n_edge_zonelets is not None else ( PartSummaryResults._default_params["n_edge_zonelets"] if "n_edge_zonelets" in PartSummaryResults._default_params else json_data["nEdgeZonelets"]),
                        n_face_zonelets if n_face_zonelets is not None else ( PartSummaryResults._default_params["n_face_zonelets"] if "n_face_zonelets" in PartSummaryResults._default_params else json_data["nFaceZonelets"]),
                        n_cell_zonelets if n_cell_zonelets is not None else ( PartSummaryResults._default_params["n_cell_zonelets"] if "n_cell_zonelets" in PartSummaryResults._default_params else json_data["nCellZonelets"]),
                        n_edge_zones if n_edge_zones is not None else ( PartSummaryResults._default_params["n_edge_zones"] if "n_edge_zones" in PartSummaryResults._default_params else json_data["nEdgeZones"]),
                        n_face_zones if n_face_zones is not None else ( PartSummaryResults._default_params["n_face_zones"] if "n_face_zones" in PartSummaryResults._default_params else json_data["nFaceZones"]),
                        n_volume_zones if n_volume_zones is not None else ( PartSummaryResults._default_params["n_volume_zones"] if "n_volume_zones" in PartSummaryResults._default_params else json_data["nVolumeZones"]),
                        n_labels if n_labels is not None else ( PartSummaryResults._default_params["n_labels"] if "n_labels" in PartSummaryResults._default_params else json_data["nLabels"]),
                        n_nodes if n_nodes is not None else ( PartSummaryResults._default_params["n_nodes"] if "n_nodes" in PartSummaryResults._default_params else json_data["nNodes"]),
                        n_faces if n_faces is not None else ( PartSummaryResults._default_params["n_faces"] if "n_faces" in PartSummaryResults._default_params else json_data["nFaces"]),
                        n_cells if n_cells is not None else ( PartSummaryResults._default_params["n_cells"] if "n_cells" in PartSummaryResults._default_params else json_data["nCells"]),
                        n_tri_faces if n_tri_faces is not None else ( PartSummaryResults._default_params["n_tri_faces"] if "n_tri_faces" in PartSummaryResults._default_params else json_data["nTriFaces"]),
                        n_poly_faces if n_poly_faces is not None else ( PartSummaryResults._default_params["n_poly_faces"] if "n_poly_faces" in PartSummaryResults._default_params else json_data["nPolyFaces"]),
                        n_quad_faces if n_quad_faces is not None else ( PartSummaryResults._default_params["n_quad_faces"] if "n_quad_faces" in PartSummaryResults._default_params else json_data["nQuadFaces"]),
                        n_tet_cells if n_tet_cells is not None else ( PartSummaryResults._default_params["n_tet_cells"] if "n_tet_cells" in PartSummaryResults._default_params else json_data["nTetCells"]),
                        n_pyra_cells if n_pyra_cells is not None else ( PartSummaryResults._default_params["n_pyra_cells"] if "n_pyra_cells" in PartSummaryResults._default_params else json_data["nPyraCells"]),
                        n_prism_cells if n_prism_cells is not None else ( PartSummaryResults._default_params["n_prism_cells"] if "n_prism_cells" in PartSummaryResults._default_params else json_data["nPrismCells"]),
                        n_poly_cells if n_poly_cells is not None else ( PartSummaryResults._default_params["n_poly_cells"] if "n_poly_cells" in PartSummaryResults._default_params else json_data["nPolyCells"]),
                        n_hex_cells if n_hex_cells is not None else ( PartSummaryResults._default_params["n_hex_cells"] if "n_hex_cells" in PartSummaryResults._default_params else json_data["nHexCells"]),
                        n_unmeshed_topo_faces if n_unmeshed_topo_faces is not None else ( PartSummaryResults._default_params["n_unmeshed_topo_faces"] if "n_unmeshed_topo_faces" in PartSummaryResults._default_params else json_data["nUnmeshedTopoFaces"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            message: str = None,
            n_topo_edges: int = None,
            n_topo_faces: int = None,
            n_topo_volumes: int = None,
            n_edge_zonelets: int = None,
            n_face_zonelets: int = None,
            n_cell_zonelets: int = None,
            n_edge_zones: int = None,
            n_face_zones: int = None,
            n_volume_zones: int = None,
            n_labels: int = None,
            n_nodes: int = None,
            n_faces: int = None,
            n_cells: int = None,
            n_tri_faces: int = None,
            n_poly_faces: int = None,
            n_quad_faces: int = None,
            n_tet_cells: int = None,
            n_pyra_cells: int = None,
            n_prism_cells: int = None,
            n_poly_cells: int = None,
            n_hex_cells: int = None,
            n_unmeshed_topo_faces: int = None):
        """Set the default values of PartSummaryResults.

        Parameters
        ----------
        message: str, optional
            Part summary text.
        n_topo_edges: int, optional
            Number of topoedges.
        n_topo_faces: int, optional
            Number of topofaces.
        n_topo_volumes: int, optional
            Number of topovolumes.
        n_edge_zonelets: int, optional
            Number of edge zonelets.
        n_face_zonelets: int, optional
            Number of face zonelets.
        n_cell_zonelets: int, optional
            Number of cell zonelets.
        n_edge_zones: int, optional
            Number of edge zones.
        n_face_zones: int, optional
            Number of face zones.
        n_volume_zones: int, optional
            Number of volume zones.
        n_labels: int, optional
            Number of labels.
        n_nodes: int, optional
            Number of nodes.
        n_faces: int, optional
            Number of faces.
        n_cells: int, optional
            Number of cells.
        n_tri_faces: int, optional
            Number of triangular faces.
        n_poly_faces: int, optional
            Number of polygonal faces.
        n_quad_faces: int, optional
            Number of quadrilateral faces.
        n_tet_cells: int, optional
            Number of tetrahedral cells.
        n_pyra_cells: int, optional
            Number of pyramid cells.
        n_prism_cells: int, optional
            Number of prism cells.
        n_poly_cells: int, optional
            Number of polyhedral cells.
        n_hex_cells: int, optional
            Number of hexahedral cells.
        n_unmeshed_topo_faces: int, optional
            Number of unmeshed topofaces.
        """
        args = locals()
        [PartSummaryResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of PartSummaryResults.

        Examples
        --------
        >>> PartSummaryResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in PartSummaryResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["message"] = self._message
        json_data["nTopoEdges"] = self._n_topo_edges
        json_data["nTopoFaces"] = self._n_topo_faces
        json_data["nTopoVolumes"] = self._n_topo_volumes
        json_data["nEdgeZonelets"] = self._n_edge_zonelets
        json_data["nFaceZonelets"] = self._n_face_zonelets
        json_data["nCellZonelets"] = self._n_cell_zonelets
        json_data["nEdgeZones"] = self._n_edge_zones
        json_data["nFaceZones"] = self._n_face_zones
        json_data["nVolumeZones"] = self._n_volume_zones
        json_data["nLabels"] = self._n_labels
        json_data["nNodes"] = self._n_nodes
        json_data["nFaces"] = self._n_faces
        json_data["nCells"] = self._n_cells
        json_data["nTriFaces"] = self._n_tri_faces
        json_data["nPolyFaces"] = self._n_poly_faces
        json_data["nQuadFaces"] = self._n_quad_faces
        json_data["nTetCells"] = self._n_tet_cells
        json_data["nPyraCells"] = self._n_pyra_cells
        json_data["nPrismCells"] = self._n_prism_cells
        json_data["nPolyCells"] = self._n_poly_cells
        json_data["nHexCells"] = self._n_hex_cells
        json_data["nUnmeshedTopoFaces"] = self._n_unmeshed_topo_faces
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "message :  %s\nn_topo_edges :  %s\nn_topo_faces :  %s\nn_topo_volumes :  %s\nn_edge_zonelets :  %s\nn_face_zonelets :  %s\nn_cell_zonelets :  %s\nn_edge_zones :  %s\nn_face_zones :  %s\nn_volume_zones :  %s\nn_labels :  %s\nn_nodes :  %s\nn_faces :  %s\nn_cells :  %s\nn_tri_faces :  %s\nn_poly_faces :  %s\nn_quad_faces :  %s\nn_tet_cells :  %s\nn_pyra_cells :  %s\nn_prism_cells :  %s\nn_poly_cells :  %s\nn_hex_cells :  %s\nn_unmeshed_topo_faces :  %s" % (self._message, self._n_topo_edges, self._n_topo_faces, self._n_topo_volumes, self._n_edge_zonelets, self._n_face_zonelets, self._n_cell_zonelets, self._n_edge_zones, self._n_face_zones, self._n_volume_zones, self._n_labels, self._n_nodes, self._n_faces, self._n_cells, self._n_tri_faces, self._n_poly_faces, self._n_quad_faces, self._n_tet_cells, self._n_pyra_cells, self._n_prism_cells, self._n_poly_cells, self._n_hex_cells, self._n_unmeshed_topo_faces)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def message(self) -> str:
        """Part summary text.
        """
        return self._message

    @message.setter
    def message(self, value: str):
        self._message = value

    @property
    def n_topo_edges(self) -> int:
        """Number of topoedges.
        """
        return self._n_topo_edges

    @n_topo_edges.setter
    def n_topo_edges(self, value: int):
        self._n_topo_edges = value

    @property
    def n_topo_faces(self) -> int:
        """Number of topofaces.
        """
        return self._n_topo_faces

    @n_topo_faces.setter
    def n_topo_faces(self, value: int):
        self._n_topo_faces = value

    @property
    def n_topo_volumes(self) -> int:
        """Number of topovolumes.
        """
        return self._n_topo_volumes

    @n_topo_volumes.setter
    def n_topo_volumes(self, value: int):
        self._n_topo_volumes = value

    @property
    def n_edge_zonelets(self) -> int:
        """Number of edge zonelets.
        """
        return self._n_edge_zonelets

    @n_edge_zonelets.setter
    def n_edge_zonelets(self, value: int):
        self._n_edge_zonelets = value

    @property
    def n_face_zonelets(self) -> int:
        """Number of face zonelets.
        """
        return self._n_face_zonelets

    @n_face_zonelets.setter
    def n_face_zonelets(self, value: int):
        self._n_face_zonelets = value

    @property
    def n_cell_zonelets(self) -> int:
        """Number of cell zonelets.
        """
        return self._n_cell_zonelets

    @n_cell_zonelets.setter
    def n_cell_zonelets(self, value: int):
        self._n_cell_zonelets = value

    @property
    def n_edge_zones(self) -> int:
        """Number of edge zones.
        """
        return self._n_edge_zones

    @n_edge_zones.setter
    def n_edge_zones(self, value: int):
        self._n_edge_zones = value

    @property
    def n_face_zones(self) -> int:
        """Number of face zones.
        """
        return self._n_face_zones

    @n_face_zones.setter
    def n_face_zones(self, value: int):
        self._n_face_zones = value

    @property
    def n_volume_zones(self) -> int:
        """Number of volume zones.
        """
        return self._n_volume_zones

    @n_volume_zones.setter
    def n_volume_zones(self, value: int):
        self._n_volume_zones = value

    @property
    def n_labels(self) -> int:
        """Number of labels.
        """
        return self._n_labels

    @n_labels.setter
    def n_labels(self, value: int):
        self._n_labels = value

    @property
    def n_nodes(self) -> int:
        """Number of nodes.
        """
        return self._n_nodes

    @n_nodes.setter
    def n_nodes(self, value: int):
        self._n_nodes = value

    @property
    def n_faces(self) -> int:
        """Number of faces.
        """
        return self._n_faces

    @n_faces.setter
    def n_faces(self, value: int):
        self._n_faces = value

    @property
    def n_cells(self) -> int:
        """Number of cells.
        """
        return self._n_cells

    @n_cells.setter
    def n_cells(self, value: int):
        self._n_cells = value

    @property
    def n_tri_faces(self) -> int:
        """Number of triangular faces.
        """
        return self._n_tri_faces

    @n_tri_faces.setter
    def n_tri_faces(self, value: int):
        self._n_tri_faces = value

    @property
    def n_poly_faces(self) -> int:
        """Number of polygonal faces.
        """
        return self._n_poly_faces

    @n_poly_faces.setter
    def n_poly_faces(self, value: int):
        self._n_poly_faces = value

    @property
    def n_quad_faces(self) -> int:
        """Number of quadrilateral faces.
        """
        return self._n_quad_faces

    @n_quad_faces.setter
    def n_quad_faces(self, value: int):
        self._n_quad_faces = value

    @property
    def n_tet_cells(self) -> int:
        """Number of tetrahedral cells.
        """
        return self._n_tet_cells

    @n_tet_cells.setter
    def n_tet_cells(self, value: int):
        self._n_tet_cells = value

    @property
    def n_pyra_cells(self) -> int:
        """Number of pyramid cells.
        """
        return self._n_pyra_cells

    @n_pyra_cells.setter
    def n_pyra_cells(self, value: int):
        self._n_pyra_cells = value

    @property
    def n_prism_cells(self) -> int:
        """Number of prism cells.
        """
        return self._n_prism_cells

    @n_prism_cells.setter
    def n_prism_cells(self, value: int):
        self._n_prism_cells = value

    @property
    def n_poly_cells(self) -> int:
        """Number of polyhedral cells.
        """
        return self._n_poly_cells

    @n_poly_cells.setter
    def n_poly_cells(self, value: int):
        self._n_poly_cells = value

    @property
    def n_hex_cells(self) -> int:
        """Number of hexahedral cells.
        """
        return self._n_hex_cells

    @n_hex_cells.setter
    def n_hex_cells(self, value: int):
        self._n_hex_cells = value

    @property
    def n_unmeshed_topo_faces(self) -> int:
        """Number of unmeshed topofaces.
        """
        return self._n_unmeshed_topo_faces

    @n_unmeshed_topo_faces.setter
    def n_unmeshed_topo_faces(self, value: int):
        self._n_unmeshed_topo_faces = value

class DeleteTopoEntitiesParams(CoreObject):
    """Parameters to control delete topoentities.
    """
    _default_params = {}

    def __initialize(
            self,
            delete_geom_zonelets: bool,
            delete_mesh_zonelets: bool):
        self._delete_geom_zonelets = delete_geom_zonelets
        self._delete_mesh_zonelets = delete_mesh_zonelets

    def __init__(
            self,
            model: CommunicationManager=None,
            delete_geom_zonelets: bool = None,
            delete_mesh_zonelets: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the DeleteTopoEntitiesParams.

        Parameters
        ----------
        model: Model
            Model to create a DeleteTopoEntitiesParams object with default parameters.
        delete_geom_zonelets: bool, optional
            Option to delete geometry zonelets of topology.
        delete_mesh_zonelets: bool, optional
            Option to delete mesh zonelets of topology.
        json_data: dict, optional
            JSON dictionary to create a DeleteTopoEntitiesParams object with provided parameters.

        Examples
        --------
        >>> delete_topo_entities_params = prime.DeleteTopoEntitiesParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["deleteGeomZonelets"],
                json_data["deleteMeshZonelets"])
        else:
            all_field_specified = all(arg is not None for arg in [delete_geom_zonelets, delete_mesh_zonelets])
            if all_field_specified:
                self.__initialize(
                    delete_geom_zonelets,
                    delete_mesh_zonelets)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "DeleteTopoEntitiesParams")["DeleteTopoEntitiesParams"]
                    self.__initialize(
                        delete_geom_zonelets if delete_geom_zonelets is not None else ( DeleteTopoEntitiesParams._default_params["delete_geom_zonelets"] if "delete_geom_zonelets" in DeleteTopoEntitiesParams._default_params else json_data["deleteGeomZonelets"]),
                        delete_mesh_zonelets if delete_mesh_zonelets is not None else ( DeleteTopoEntitiesParams._default_params["delete_mesh_zonelets"] if "delete_mesh_zonelets" in DeleteTopoEntitiesParams._default_params else json_data["deleteMeshZonelets"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            delete_geom_zonelets: bool = None,
            delete_mesh_zonelets: bool = None):
        """Set the default values of DeleteTopoEntitiesParams.

        Parameters
        ----------
        delete_geom_zonelets: bool, optional
            Option to delete geometry zonelets of topology.
        delete_mesh_zonelets: bool, optional
            Option to delete mesh zonelets of topology.
        """
        args = locals()
        [DeleteTopoEntitiesParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of DeleteTopoEntitiesParams.

        Examples
        --------
        >>> DeleteTopoEntitiesParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in DeleteTopoEntitiesParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["deleteGeomZonelets"] = self._delete_geom_zonelets
        json_data["deleteMeshZonelets"] = self._delete_mesh_zonelets
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "delete_geom_zonelets :  %s\ndelete_mesh_zonelets :  %s" % (self._delete_geom_zonelets, self._delete_mesh_zonelets)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def delete_geom_zonelets(self) -> bool:
        """Option to delete geometry zonelets of topology.
        """
        return self._delete_geom_zonelets

    @delete_geom_zonelets.setter
    def delete_geom_zonelets(self, value: bool):
        self._delete_geom_zonelets = value

    @property
    def delete_mesh_zonelets(self) -> bool:
        """Option to delete mesh zonelets of topology.
        """
        return self._delete_mesh_zonelets

    @delete_mesh_zonelets.setter
    def delete_mesh_zonelets(self, value: bool):
        self._delete_mesh_zonelets = value

class DeleteTopoEntitiesResults(CoreObject):
    """Results associated with delete topoentities.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode):
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the DeleteTopoEntitiesResults.

        Parameters
        ----------
        model: Model
            Model to create a DeleteTopoEntitiesResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with delete topoentities.
        json_data: dict, optional
            JSON dictionary to create a DeleteTopoEntitiesResults object with provided parameters.

        Examples
        --------
        >>> delete_topo_entities_results = prime.DeleteTopoEntitiesResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"]))
        else:
            all_field_specified = all(arg is not None for arg in [error_code])
            if all_field_specified:
                self.__initialize(
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "DeleteTopoEntitiesResults")["DeleteTopoEntitiesResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( DeleteTopoEntitiesResults._default_params["error_code"] if "error_code" in DeleteTopoEntitiesResults._default_params else ErrorCode(json_data["errorCode"])))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of DeleteTopoEntitiesResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with delete topoentities.
        """
        args = locals()
        [DeleteTopoEntitiesResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of DeleteTopoEntitiesResults.

        Examples
        --------
        >>> DeleteTopoEntitiesResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in DeleteTopoEntitiesResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s" % (self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with delete topoentities.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class AddToZoneResults(CoreObject):
    """Results associated with the add to zone operation.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            warning_codes: List[WarningCode]):
        self._error_code = ErrorCode(error_code)
        self._warning_codes = warning_codes

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the AddToZoneResults.

        Parameters
        ----------
        model: Model
            Model to create a AddToZoneResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the add to zone operation.
        json_data: dict, optional
            JSON dictionary to create a AddToZoneResults object with provided parameters.

        Examples
        --------
        >>> add_to_zone_results = prime.AddToZoneResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"]),
                [WarningCode(data) for data in json_data["warningCodes"]])
        else:
            all_field_specified = all(arg is not None for arg in [error_code, warning_codes])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    warning_codes)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "AddToZoneResults")["AddToZoneResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( AddToZoneResults._default_params["error_code"] if "error_code" in AddToZoneResults._default_params else ErrorCode(json_data["errorCode"])),
                        warning_codes if warning_codes is not None else ( AddToZoneResults._default_params["warning_codes"] if "warning_codes" in AddToZoneResults._default_params else [WarningCode(data) for data in json_data["warningCodes"]]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None):
        """Set the default values of AddToZoneResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the add to zone operation.
        """
        args = locals()
        [AddToZoneResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of AddToZoneResults.

        Examples
        --------
        >>> AddToZoneResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in AddToZoneResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["errorCode"] = self._error_code
        json_data["warningCodes"] = [data for data in self._warning_codes]
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nwarning_codes :  %s" % (self._error_code, '[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def warning_codes(self) -> List[WarningCode]:
        """Warning codes associated with the add to zone operation.
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, value: List[WarningCode]):
        self._warning_codes = value

class RemoveZoneResults(CoreObject):
    """Results associated with the remove zone operation.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            warning_codes: List[WarningCode]):
        self._error_code = ErrorCode(error_code)
        self._warning_codes = warning_codes

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the RemoveZoneResults.

        Parameters
        ----------
        model: Model
            Model to create a RemoveZoneResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the remove zone operation.
        json_data: dict, optional
            JSON dictionary to create a RemoveZoneResults object with provided parameters.

        Examples
        --------
        >>> remove_zone_results = prime.RemoveZoneResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"]),
                [WarningCode(data) for data in json_data["warningCodes"]])
        else:
            all_field_specified = all(arg is not None for arg in [error_code, warning_codes])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    warning_codes)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "RemoveZoneResults")["RemoveZoneResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( RemoveZoneResults._default_params["error_code"] if "error_code" in RemoveZoneResults._default_params else ErrorCode(json_data["errorCode"])),
                        warning_codes if warning_codes is not None else ( RemoveZoneResults._default_params["warning_codes"] if "warning_codes" in RemoveZoneResults._default_params else [WarningCode(data) for data in json_data["warningCodes"]]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None):
        """Set the default values of RemoveZoneResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the remove zone operation.
        """
        args = locals()
        [RemoveZoneResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of RemoveZoneResults.

        Examples
        --------
        >>> RemoveZoneResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in RemoveZoneResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["errorCode"] = self._error_code
        json_data["warningCodes"] = [data for data in self._warning_codes]
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nwarning_codes :  %s" % (self._error_code, '[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def warning_codes(self) -> List[WarningCode]:
        """Warning codes associated with the remove zone operation.
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, value: List[WarningCode]):
        self._warning_codes = value

class AddLabelResults(CoreObject):
    """Results associated with the add label operation.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode):
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the AddLabelResults.

        Parameters
        ----------
        model: Model
            Model to create a AddLabelResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the add label operation.
        json_data: dict, optional
            JSON dictionary to create a AddLabelResults object with provided parameters.

        Examples
        --------
        >>> add_label_results = prime.AddLabelResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"]))
        else:
            all_field_specified = all(arg is not None for arg in [error_code])
            if all_field_specified:
                self.__initialize(
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "AddLabelResults")["AddLabelResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( AddLabelResults._default_params["error_code"] if "error_code" in AddLabelResults._default_params else ErrorCode(json_data["errorCode"])))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of AddLabelResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the add label operation.
        """
        args = locals()
        [AddLabelResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of AddLabelResults.

        Examples
        --------
        >>> AddLabelResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in AddLabelResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s" % (self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the add label operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class RemoveLabelResults(CoreObject):
    """Results associated with the remove label operation.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode):
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the RemoveLabelResults.

        Parameters
        ----------
        model: Model
            Model to create a RemoveLabelResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the remove label operation.
        json_data: dict, optional
            JSON dictionary to create a RemoveLabelResults object with provided parameters.

        Examples
        --------
        >>> remove_label_results = prime.RemoveLabelResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"]))
        else:
            all_field_specified = all(arg is not None for arg in [error_code])
            if all_field_specified:
                self.__initialize(
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "RemoveLabelResults")["RemoveLabelResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( RemoveLabelResults._default_params["error_code"] if "error_code" in RemoveLabelResults._default_params else ErrorCode(json_data["errorCode"])))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of RemoveLabelResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the remove label operation.
        """
        args = locals()
        [RemoveLabelResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of RemoveLabelResults.

        Examples
        --------
        >>> RemoveLabelResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in RemoveLabelResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s" % (self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the remove label operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value
