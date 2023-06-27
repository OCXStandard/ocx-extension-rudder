from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from ocx_extension_rudder.unitsml.unitsml_schema_lite_0_9_18 import UnitsMl
from ocx_extension_rudder.v286_fix.ocx_schema import (
    DescriptionBaseT,
    DesignView,
    EntityBaseT,
    ExternalGeometryRef,
    Header,
    Length,
    MaterialCatalogueT,
    MaterialRef,
    MaterialT,
    QuantityT,
    Thickness,
    Xgrid,
    Ygrid,
    Zgrid,
    TightnessValue,
)

__NAMESPACE__ = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"


@dataclass
class BushAllowableSurfacePressure:
    """
    The allowable surface pressure of the bush in Pa.
    """
    class Meta:
        namespace = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"


class IceNotationValue(Enum):
    ICE_1_A_F = "ICE (1A*F)"
    ICE_1_A = "ICE (1A*)"
    ICE_1_A_1 = "ICE (1A)"
    ICE_1_B = "ICE (1B)"
    ICE_1_C = "ICE (1C)"
    ICE_C = "ICE-C"
    NONE = "NONE"


class RudderArrangementValue(Enum):
    NORMAL = "Normal"
    NOT_IN_PROPELLER_SLIP_STREAM = "Not in propeller slip stream"
    BEHIND_FIXED_PROPELLER_NOZZLE = "Behind fixed propeller nozzle"


class RudderFunctionValue(Enum):
    LOWER_CASTING = "Lower Casting"
    UPPER_CASTING = "Upper Casting"
    TOP_PLATE = "Top Plate"
    BOTTOM_PLATE = "Bottom Plate"
    MID_TOP_PLATE = "Mid Top Plate"
    RUDDER_NOSE = "Rudder Nose"
    PLATE_TO_SOLID = "Plate to Solid"
    OUTER_PLATE = "Outer Plate"
    REMOVABLE_PLATE = "Removable Plate"
    TAIL = "Tail"
    VERTICAL_PLATE = "Vertical Plate"
    UPPER_COVER_PLATE = "Upper Cover Plate"
    BELOW_COVER_PLATE = "Below Cover Plate"
    HORIZONTAL_PLATE = "Horizontal Plate"
    SUB_PLATE = "Sub Plate"
    HOLE = "Hole"


class RudderProfileTypeValue(Enum):
    VALUE = ""
    MIXED_PROFILES = "Mixed profiles"
    HOLLOW_PROFILE = "Hollow profile"
    FLAT_SIDED = "Flat-sided"
    NACA_G_TTINGEN = "NACA/Göttingen"
    NOZZLE_RUDDER = "Nozzle rudder"
    RUDDER_WITH_FLAP = "Rudder with flap"
    SINGLE_PLATE = "Single plate"


@dataclass
class BearingThickness(QuantityT):
    """
    The bearing thickness of the parent element (pintle, stock).
    """
    class Meta:
        namespace = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"


@dataclass
class CastedMaterialT(MaterialT):
    """
    Type definition of the Charpy V test data.
    """
    class Meta:
        name = "CastedMaterial_T"


@dataclass
class CharpyVdataT(MaterialT):
    """
    Type definition of the Charpy V test data.
    """
    class Meta:
        name = "CharpyVData_T"


@dataclass
class ForgedMaterialT(MaterialT):
    """
    Type definition of the forged material data.
    """
    class Meta:
        name = "ForgedMaterial_T"


@dataclass
class HornPintleHeightHh(QuantityT):
    """
    Horn pintle height mesured form rudder base (bottom), Hh.
    """
    class Meta:
        namespace = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"


@dataclass
class InnerDiameter(QuantityT):
    """
    The inner diameter of a part.
    """
    class Meta:
        namespace = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"


@dataclass
class MaxServiceSpeedAhead(QuantityT):
    """
    Maximum service speeed ahead.
    """
    class Meta:
        namespace = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"


@dataclass
class MaxServiceSpeedAstern(QuantityT):
    """
    Maximum service speed astern.
    """
    class Meta:
        namespace = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"


@dataclass
class NeckBearingHeightHn(QuantityT):
    """
    Neck bearing height mesured form rudder base (bottom), Hn.
    """
    class Meta:
        namespace = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"


@dataclass
class OuterDiameter(QuantityT):
    """
    The outer diameter of a part.
    """
    class Meta:
        namespace = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"


@dataclass
class RudderCoordinateSystemT(DescriptionBaseT):
    """
    Type definition of rudder coordinate system.
    """
    class Meta:
        name = "RudderCoordinateSystem_T"

    xgrid: List[Xgrid] = field(
        default_factory=list,
        metadata={
            "name": "XGrid",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V286_fix//OCX_Schema.xsd",
            "max_occurs": 3,
        }
    )
    ygrid: List[Ygrid] = field(
        default_factory=list,
        metadata={
            "name": "YGrid",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V286_fix//OCX_Schema.xsd",
            "max_occurs": 3,
        }
    )
    zgrid: List[Zgrid] = field(
        default_factory=list,
        metadata={
            "name": "ZGrid",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V286_fix//OCX_Schema.xsd",
            "max_occurs": 3,
        }
    )


@dataclass
class RudderPartT(EntityBaseT):
    """
    Abstract Type definition of a rudder part.
    """
    class Meta:
        name = "RudderPart_T"

    material_ref: List[MaterialRef] = field(
        default_factory=list,
        metadata={
            "name": "MaterialRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V286_fix//OCX_Schema.xsd",
            "max_occurs": 2,
        }
    )
    external_geometry_ref: List[ExternalGeometryRef] = field(
        default_factory=list,
        metadata={
            "name": "ExternalGeometryRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V286_fix//OCX_Schema.xsd",
            "max_occurs": 2,
        }
    )
    rudder_function: Optional[RudderFunctionValue] = field(
        default=None,
        metadata={
            "name": "rudderFunction",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
            "required": True,
        }
    )
    tightness: Optional[TightnessValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V286_fix//OCX_Schema.xsd",
            "required": True,
        }
    )


@dataclass
class UpperBearingHeightHu(QuantityT):
    """
    Upper bearing height mesured form rudder base (bottom), Hu.
    """
    class Meta:
        namespace = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"


@dataclass
class UpperCouplingHeightHc(QuantityT):
    """
    Upper coupling height mesured form rudder base (bottom), Hc.
    """
    class Meta:
        namespace = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"


@dataclass
class BushT(RudderPartT):
    """
    Type definition of the rudder bush.
    """
    class Meta:
        name = "Bush_T"

    outer_diameter: Optional[OuterDiameter] = field(
        default=None,
        metadata={
            "name": "OuterDiameter",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
            "required": True,
        }
    )
    inner_diameter: Optional[InnerDiameter] = field(
        default=None,
        metadata={
            "name": "InnerDiameter",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
            "required": True,
        }
    )
    length: Optional[Length] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V286_fix//OCX_Schema.xsd",
            "required": True,
        }
    )
    thickness: Optional[Thickness] = field(
        default=None,
        metadata={
            "name": "Thickness",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V286_fix//OCX_Schema.xsd",
            "required": True,
        }
    )
    bush_allowable_surface_pressure: Optional[BushAllowableSurfacePressure] = field(
        default=None,
        metadata={
            "name": "BushAllowableSurfacePressure",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
            "required": True,
        }
    )


@dataclass
class CastedMaterial(CastedMaterialT):
    """
    The Charpy V test data for a casted part.
    """
    class Meta:
        namespace = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"


@dataclass
class CastedPartT(RudderPartT):
    """
    Type definition of the rudder pintle.
    """
    class Meta:
        name = "CastedPart_T"

    ndt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NDT",
            "type": "Attribute",
        }
    )
    heat_treatment: Optional[str] = field(
        default=None,
        metadata={
            "name": "heatTreatment",
            "type": "Attribute",
        }
    )


@dataclass
class CharpyVdata(CharpyVdataT):
    """
    The Charpy V test data for a material.
    """
    class Meta:
        name = "CharpyVData"
        namespace = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"


@dataclass
class ForgedMaterial(CastedMaterialT):
    """
    Forged material data.
    """
    class Meta:
        namespace = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"


@dataclass
class IceTypeT:
    """
    Type definition of the IceClass.
    """
    class Meta:
        name = "IceClass_T"

    max_service_speed_ahead: List[MaxServiceSpeedAhead] = field(
        default_factory=list,
        metadata={
            "name": "MaxServiceSpeedAhead",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
            "max_occurs": 2,
        }
    )
    max_service_speed_astern: List[MaxServiceSpeedAstern] = field(
        default_factory=list,
        metadata={
            "name": "MaxServiceSpeedAstern",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
            "max_occurs": 2,
        }
    )
    ice_notation: Optional[IceNotationValue] = field(
        default=None,
        metadata={
            "name": "iceNotation",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
            "required": True,
        }
    )


@dataclass
class LinerT(RudderPartT):
    """
    Type definition of the liner.
    """
    class Meta:
        name = "Liner_T"

    length: Optional[Length] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V286_fix//OCX_Schema.xsd",
            "required": True,
        }
    )
    outer_diameter: Optional[OuterDiameter] = field(
        default=None,
        metadata={
            "name": "OuterDiameter",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
            "required": True,
        }
    )
    inner_diameter: Optional[InnerDiameter] = field(
        default=None,
        metadata={
            "name": "InnerDiameter",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
            "required": True,
        }
    )
    thickness: Optional[Thickness] = field(
        default=None,
        metadata={
            "name": "Thickness",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V286_fix//OCX_Schema.xsd",
            "required": True,
        }
    )


@dataclass
class NutT(RudderPartT):
    """
    Type definition of the rudder nut.
    """
    class Meta:
        name = "Nut_T"

    outer_diameter: Optional[OuterDiameter] = field(
        default=None,
        metadata={
            "name": "OuterDiameter",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
            "required": True,
        }
    )
    inner_diameter: Optional[InnerDiameter] = field(
        default=None,
        metadata={
            "name": "InnerDiameter",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
            "required": True,
        }
    )


@dataclass
class PintleT(RudderPartT):
    """
    Type definition of the rudder pintle.

    Attributes
        bearing_thickness: The pintle bearing thickness.
    """
    class Meta:
        name = "Pintle_T"

    bearing_thickness: Optional[BearingThickness] = field(
        default=None,
        metadata={
            "name": "BearingThickness",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
            "required": True,
        }
    )


@dataclass
class RudderCoordinateSystem(RudderCoordinateSystemT):
    """The rudder coordinate system.

    X = 0 ant the centre of rudder stock. Z = 0 at base.
    """
    class Meta:
        namespace = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"


@dataclass
class RudderDimensions:
    """
    The main rudder dimensions.
    """
    class Meta:
        namespace = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"

    neck_bearing_height_hn: List[NeckBearingHeightHn] = field(
        default_factory=list,
        metadata={
            "name": "NeckBearingHeightHn",
            "type": "Element",
        }
    )
    upper_bearing_height_hu: List[UpperBearingHeightHu] = field(
        default_factory=list,
        metadata={
            "name": "UpperBearingHeightHu",
            "type": "Element",
        }
    )
    upper_coupling_height_hc: List[UpperCouplingHeightHc] = field(
        default_factory=list,
        metadata={
            "name": "UpperCouplingHeightHc",
            "type": "Element",
        }
    )
    horn_pintle_height_hh: List[HornPintleHeightHh] = field(
        default_factory=list,
        metadata={
            "name": "HornPintleHeightHh",
            "type": "Element",
        }
    )


@dataclass
class RudderPlateT(RudderPartT):
    """
    Type definition of the rudder plating.
    """
    class Meta:
        name = "RudderPlate_T"

    thickness: Optional[Thickness] = field(
        default=None,
        metadata={
            "name": "Thickness",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V286_fix//OCX_Schema.xsd",
            "required": True,
        }
    )


@dataclass
class Bush(BushT):
    """
    The rudder bushr.
    """
    class Meta:
        namespace = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"


@dataclass
class CastedPart(CastedPartT):
    """
    A rudder casted part.
    """
    class Meta:
        namespace = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"


@dataclass
class IceType(IceTypeT):
    """
    The ICE notation of the rudder if any.
    """
    class Meta:
        name = "IceClass"
        namespace = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"


@dataclass
class Liner(LinerT):
    """
    The rudder stock or pintle liner.
    """
    class Meta:
        namespace = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"


@dataclass
class Nut(PintleT):
    """
    The rudder nut.
    """
    class Meta:
        namespace = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"


@dataclass
class Pintle(PintleT):
    """
    The rudder pintle.
    """
    class Meta:
        namespace = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"


@dataclass
class RudderMaterialsT(MaterialCatalogueT):
    """
    Type definition of catalogue rudder materials.
    """
    class Meta:
        name = "RudderMaterials_T"

    forged_material: List[ForgedMaterial] = field(
        default_factory=list,
        metadata={
            "name": "ForgedMaterial",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
        }
    )
    casted_material: List[CastedMaterial] = field(
        default_factory=list,
        metadata={
            "name": "CastedMaterial",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
        }
    )


@dataclass
class RudderPlate(RudderPlateT):
    """
    The rudder plating.
    """
    class Meta:
        namespace = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"


@dataclass
class GeneralRudderDataT:
    class Meta:
        name = "GeneralRudderData_T"

    max_service_speed_ahead: List[MaxServiceSpeedAhead] = field(
        default_factory=list,
        metadata={
            "name": "MaxServiceSpeedAhead",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
        }
    )
    max_service_speed_astern: List[MaxServiceSpeedAstern] = field(
        default_factory=list,
        metadata={
            "name": "MaxServiceSpeedAstern",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
        }
    )
    ice_class: List[IceType] = field(
        default_factory=list,
        metadata={
            "name": "IceClass",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
        }
    )
    rudder_dimensions: List[RudderDimensions] = field(
        default_factory=list,
        metadata={
            "name": "RudderDimensions",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
        }
    )
    rudder_arrangement: Optional[RudderArrangementValue] = field(
        default=None,
        metadata={
            "name": "rudderArrangement",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
            "required": True,
        }
    )
    rudder_profile_type: Optional[RudderProfileTypeValue] = field(
        default=None,
        metadata={
            "name": "rudderProfileType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
            "required": True,
        }
    )


@dataclass
class RudderMaterials(RudderMaterialsT):
    """
    Catalogue of Rudder material types.
    """
    class Meta:
        namespace = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"


@dataclass
class RudderStockT(RudderPartT):
    """
    Type definition of the rudder stock.

    Attributes
        liner:
        bush:
        bearing_thickness: The neck  bearing thickness of the rudder
            stock.
    """
    class Meta:
        name = "RudderStock_T"

    liner: Optional[Liner] = field(
        default=None,
        metadata={
            "name": "Liner",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
            "required": True,
        }
    )
    bush: Optional[Bush] = field(
        default=None,
        metadata={
            "name": "Bush",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
            "required": True,
        }
    )
    bearing_thickness: Optional[BearingThickness] = field(
        default=None,
        metadata={
            "name": "BearingThickness",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
            "required": True,
        }
    )


@dataclass
class GeneralRudderData(GeneralRudderDataT):
    """
    The rudder data.
    """
    class Meta:
        namespace = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"


@dataclass
class RudderStock(RudderStockT):
    """
    The rudder stock.
    """
    class Meta:
        namespace = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"


@dataclass
class SemiSpadeRudderT(EntityBaseT):
    """
    Type definition of the semi-spade rudder.
    """
    class Meta:
        name = "SemiSpadeRudder_T"

    rudder_coordinate_system: List[RudderCoordinateSystem] = field(
        default_factory=list,
        metadata={
            "name": "RudderCoordinateSystem",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
        }
    )
    rudder_plate: List[RudderPlate] = field(
        default_factory=list,
        metadata={
            "name": "RudderPlate",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
        }
    )
    casted_part: List[CastedPart] = field(
        default_factory=list,
        metadata={
            "name": "CastedPart",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
        }
    )
    rudder_stock: List[RudderStock] = field(
        default_factory=list,
        metadata={
            "name": "RudderStock",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
        }
    )
    pintle: List[Pintle] = field(
        default_factory=list,
        metadata={
            "name": "Pintle",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
        }
    )
    liner: List[Liner] = field(
        default_factory=list,
        metadata={
            "name": "Liner",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
        }
    )
    nut: List[Nut] = field(
        default_factory=list,
        metadata={
            "name": "Nut",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
        }
    )


@dataclass
class SemiSpadeRudder(SemiSpadeRudderT):
    """
    The  model-based definitiion of a semi-spade rudder type.
    """
    class Meta:
        namespace = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"


@dataclass
class RudderDocumentT:
    """
    Type definition of the root element.

    Attributes
        header:
        semi_spade_rudder:
        general_rudder_data:
        rudder_materials:
        design_view:
        units_ml:
        schema_version: Current XML schema version (Format - x.y.z) x :
            Incremented for backward incompatible changes ( Ex - Adding
            a required attribute, etc.) y : Major backward compatible
            changes [ Ex - Adding a new node ,fixing major CRs,etc..] z
            : Minor backward compatible changes (Ex - adding an optional
            attribute, etc).
    """
    class Meta:
        name = "RudderDocument_T"

    header: List[Header] = field(
        default_factory=list,
        metadata={
            "name": "Header",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V286_fix//OCX_Schema.xsd",
        }
    )
    semi_spade_rudder: List[SemiSpadeRudder] = field(
        default_factory=list,
        metadata={
            "name": "SemiSpadeRudder",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
        }
    )
    general_rudder_data: List[GeneralRudderData] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRudderData",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
        }
    )
    rudder_materials: List[RudderMaterials] = field(
        default_factory=list,
        metadata={
            "name": "RudderMaterials",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd",
        }
    )
    design_view: List[DesignView] = field(
        default_factory=list,
        metadata={
            "name": "DesignView",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V286_fix//OCX_Schema.xsd",
        }
    )
    units_ml: List[UnitsMl] = field(
        default_factory=list,
        metadata={
            "name": "UnitsML",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
        }
    )
    schema_version: str = field(
        init=False,
        default="1.0.0",
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class RudderDocument(RudderDocumentT):
    """
    Root element of the Rudder document.
    """
    class Meta:
        namespace = "https://3docx.org/fileadmin/ocx_schema/extension/rudder/v1.0.0/OCX_ext_rudder.xsd"
