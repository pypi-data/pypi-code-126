'''_2279.py

FELink
'''


from typing import List
from collections import OrderedDict

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value, list_with_selected_item, overridable
from mastapy.system_model.fe import (
    _2259, _2263, _2225, _2258,
    _2246
)
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.nodal_analysis.dev_tools_analyses import _178
from mastapy.system_model.part_model import (
    _2306, _2298, _2299, _2302,
    _2304, _2309, _2310, _2313,
    _2314, _2316, _2323, _2324,
    _2325, _2327, _2330, _2332,
    _2333, _2338, _2340
)
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model.shaft_model import _2343
from mastapy.system_model.part_model.gears import (
    _2373, _2375, _2377, _2378,
    _2379, _2381, _2383, _2385,
    _2387, _2388, _2390, _2394,
    _2396, _2398, _2400, _2403,
    _2405, _2407, _2409, _2410,
    _2411, _2413
)
from mastapy.system_model.part_model.cycloidal import _2429, _2430
from mastapy.system_model.part_model.couplings import (
    _2439, _2442, _2444, _2447,
    _2449, _2450, _2456, _2458,
    _2461, _2464, _2465, _2466,
    _2468, _2470
)
from mastapy.system_model.connections_and_sockets import (
    _2158, _2128, _2129, _2136,
    _2138, _2140, _2141, _2142,
    _2144, _2145, _2146, _2147,
    _2148, _2150, _2151, _2152,
    _2155, _2156
)
from mastapy.system_model.connections_and_sockets.gears import (
    _2162, _2164, _2166, _2168,
    _2170, _2172, _2174, _2176,
    _2178, _2179, _2183, _2184,
    _2186, _2188, _2190, _2192,
    _2194
)
from mastapy.system_model.connections_and_sockets.cycloidal import (
    _2195, _2196, _2198, _2199,
    _2201, _2202
)
from mastapy.system_model.connections_and_sockets.couplings import (
    _2205, _2207, _2209, _2211,
    _2213, _2215, _2216
)
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_FE_LINK = python_net_import('SMT.MastaAPI.SystemModel.FE.Links', 'FELink')


__docformat__ = 'restructuredtext en'
__all__ = ('FELink',)


class FELink(_0.APIBase):
    '''FELink

    This is a mastapy class.
    '''

    TYPE = _FE_LINK

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FELink.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def external_node_ids(self) -> 'str':
        '''str: 'ExternalNodeIDs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ExternalNodeIDs

    @property
    def component_name(self) -> 'str':
        '''str: 'ComponentName' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ComponentName

    @property
    def connection(self) -> 'str':
        '''str: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Connection

    @property
    def link_node_source(self) -> 'enum_with_selected_value.EnumWithSelectedValue_LinkNodeSource':
        '''enum_with_selected_value.EnumWithSelectedValue_LinkNodeSource: 'LinkNodeSource' is the original name of this property.'''

        value = enum_with_selected_value.EnumWithSelectedValue_LinkNodeSource.wrapped_type()
        return enum_with_selected_value_runtime.create(self.wrapped.LinkNodeSource, value) if self.wrapped.LinkNodeSource is not None else None

    @link_node_source.setter
    def link_node_source(self, value: 'enum_with_selected_value.EnumWithSelectedValue_LinkNodeSource.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_LinkNodeSource.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LinkNodeSource = value

    @property
    def link_to_get_nodes_from(self) -> 'list_with_selected_item.ListWithSelectedItem_FELink':
        '''list_with_selected_item.ListWithSelectedItem_FELink: 'LinkToGetNodesFrom' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_FELink)(self.wrapped.LinkToGetNodesFrom) if self.wrapped.LinkToGetNodesFrom is not None else None

    @link_to_get_nodes_from.setter
    def link_to_get_nodes_from(self, value: 'list_with_selected_item.ListWithSelectedItem_FELink.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_FELink.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_FELink.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.LinkToGetNodesFrom = value

    @property
    def node_cylinder_search_diameter(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'NodeCylinderSearchDiameter' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.NodeCylinderSearchDiameter) if self.wrapped.NodeCylinderSearchDiameter is not None else None

    @node_cylinder_search_diameter.setter
    def node_cylinder_search_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.NodeCylinderSearchDiameter = value

    @property
    def node_cone_search_angle(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'NodeConeSearchAngle' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.NodeConeSearchAngle) if self.wrapped.NodeConeSearchAngle is not None else None

    @node_cone_search_angle.setter
    def node_cone_search_angle(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.NodeConeSearchAngle = value

    @property
    def node_search_cylinder_thickness(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'NodeSearchCylinderThickness' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.NodeSearchCylinderThickness) if self.wrapped.NodeSearchCylinderThickness is not None else None

    @node_search_cylinder_thickness.setter
    def node_search_cylinder_thickness(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.NodeSearchCylinderThickness = value

    @property
    def node_cylinder_search_length(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'NodeCylinderSearchLength' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.NodeCylinderSearchLength) if self.wrapped.NodeCylinderSearchLength is not None else None

    @node_cylinder_search_length.setter
    def node_cylinder_search_length(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.NodeCylinderSearchLength = value

    @property
    def node_cylinder_search_axial_offset(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'NodeCylinderSearchAxialOffset' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.NodeCylinderSearchAxialOffset) if self.wrapped.NodeCylinderSearchAxialOffset is not None else None

    @node_cylinder_search_axial_offset.setter
    def node_cylinder_search_axial_offset(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.NodeCylinderSearchAxialOffset = value

    @property
    def number_of_nodes_in_ring(self) -> 'overridable.Overridable_int':
        '''overridable.Overridable_int: 'NumberOfNodesInRing' is the original name of this property.'''

        return constructor.new(overridable.Overridable_int)(self.wrapped.NumberOfNodesInRing) if self.wrapped.NumberOfNodesInRing is not None else None

    @number_of_nodes_in_ring.setter
    def number_of_nodes_in_ring(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0, is_overridden)
        self.wrapped.NumberOfNodesInRing = value

    @property
    def has_teeth(self) -> 'bool':
        '''bool: 'HasTeeth' is the original name of this property.'''

        return self.wrapped.HasTeeth

    @has_teeth.setter
    def has_teeth(self, value: 'bool'):
        self.wrapped.HasTeeth = bool(value) if value else False

    @property
    def angle_of_centre_of_connection_patch(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'AngleOfCentreOfConnectionPatch' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.AngleOfCentreOfConnectionPatch) if self.wrapped.AngleOfCentreOfConnectionPatch is not None else None

    @angle_of_centre_of_connection_patch.setter
    def angle_of_centre_of_connection_patch(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.AngleOfCentreOfConnectionPatch = value

    @property
    def span_of_patch(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'SpanOfPatch' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.SpanOfPatch) if self.wrapped.SpanOfPatch is not None else None

    @span_of_patch.setter
    def span_of_patch(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.SpanOfPatch = value

    @property
    def node_selection_depth(self) -> 'overridable.Overridable_NodeSelectionDepthOption':
        '''overridable.Overridable_NodeSelectionDepthOption: 'NodeSelectionDepth' is the original name of this property.'''

        value = overridable.Overridable_NodeSelectionDepthOption.wrapped_type()
        return enum_with_selected_value_runtime.create(self.wrapped.NodeSelectionDepth, value) if self.wrapped.NodeSelectionDepth is not None else None

    @node_selection_depth.setter
    def node_selection_depth(self, value: 'overridable.Overridable_NodeSelectionDepthOption.implicit_type()'):
        wrapper_type = overridable.Overridable_NodeSelectionDepthOption.wrapper_type()
        enclosed_type = overridable.Overridable_NodeSelectionDepthOption.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value is not None else None, is_overridden)
        self.wrapped.NodeSelectionDepth = value

    @property
    def coupling_type(self) -> 'overridable.Overridable_RigidCouplingType':
        '''overridable.Overridable_RigidCouplingType: 'CouplingType' is the original name of this property.'''

        value = overridable.Overridable_RigidCouplingType.wrapped_type()
        return enum_with_selected_value_runtime.create(self.wrapped.CouplingType, value) if self.wrapped.CouplingType is not None else None

    @coupling_type.setter
    def coupling_type(self, value: 'overridable.Overridable_RigidCouplingType.implicit_type()'):
        wrapper_type = overridable.Overridable_RigidCouplingType.wrapper_type()
        enclosed_type = overridable.Overridable_RigidCouplingType.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value is not None else None, is_overridden)
        self.wrapped.CouplingType = value

    @property
    def number_of_axial_nodes(self) -> 'int':
        '''int: 'NumberOfAxialNodes' is the original name of this property.'''

        return self.wrapped.NumberOfAxialNodes

    @number_of_axial_nodes.setter
    def number_of_axial_nodes(self, value: 'int'):
        self.wrapped.NumberOfAxialNodes = int(value) if value else 0

    @property
    def bearing_node_link_option(self) -> 'enum_with_selected_value.EnumWithSelectedValue_BearingNodeOption':
        '''enum_with_selected_value.EnumWithSelectedValue_BearingNodeOption: 'BearingNodeLinkOption' is the original name of this property.'''

        value = enum_with_selected_value.EnumWithSelectedValue_BearingNodeOption.wrapped_type()
        return enum_with_selected_value_runtime.create(self.wrapped.BearingNodeLinkOption, value) if self.wrapped.BearingNodeLinkOption is not None else None

    @bearing_node_link_option.setter
    def bearing_node_link_option(self, value: 'enum_with_selected_value.EnumWithSelectedValue_BearingNodeOption.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_BearingNodeOption.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.BearingNodeLinkOption = value

    @property
    def width_of_axial_patch(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'WidthOfAxialPatch' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.WidthOfAxialPatch) if self.wrapped.WidthOfAxialPatch is not None else None

    @width_of_axial_patch.setter
    def width_of_axial_patch(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.WidthOfAxialPatch = value

    @property
    def connect_to_midside_nodes(self) -> 'bool':
        '''bool: 'ConnectToMidsideNodes' is the original name of this property.'''

        return self.wrapped.ConnectToMidsideNodes

    @connect_to_midside_nodes.setter
    def connect_to_midside_nodes(self, value: 'bool'):
        self.wrapped.ConnectToMidsideNodes = bool(value) if value else False

    @property
    def bearing_race_in_fe(self) -> 'overridable.Overridable_bool':
        '''overridable.Overridable_bool: 'BearingRaceInFE' is the original name of this property.'''

        return constructor.new(overridable.Overridable_bool)(self.wrapped.BearingRaceInFE) if self.wrapped.BearingRaceInFE is not None else None

    @bearing_race_in_fe.setter
    def bearing_race_in_fe(self, value: 'overridable.Overridable_bool.implicit_type()'):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else False, is_overridden)
        self.wrapped.BearingRaceInFE = value

    @property
    def number_of_nodes_in_full_fe_mesh(self) -> 'int':
        '''int: 'NumberOfNodesInFullFEMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NumberOfNodesInFullFEMesh

    @property
    def component(self) -> '_2306.Component':
        '''Component: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2306.Component.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to Component. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_abstract_shaft(self) -> '_2298.AbstractShaft':
        '''AbstractShaft: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2298.AbstractShaft.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to AbstractShaft. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_abstract_shaft_or_housing(self) -> '_2299.AbstractShaftOrHousing':
        '''AbstractShaftOrHousing: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2299.AbstractShaftOrHousing.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to AbstractShaftOrHousing. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_bearing(self) -> '_2302.Bearing':
        '''Bearing: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2302.Bearing.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to Bearing. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_bolt(self) -> '_2304.Bolt':
        '''Bolt: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2304.Bolt.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to Bolt. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_connector(self) -> '_2309.Connector':
        '''Connector: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2309.Connector.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to Connector. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_datum(self) -> '_2310.Datum':
        '''Datum: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2310.Datum.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to Datum. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_external_cad_model(self) -> '_2313.ExternalCADModel':
        '''ExternalCADModel: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2313.ExternalCADModel.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to ExternalCADModel. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_fe_part(self) -> '_2314.FEPart':
        '''FEPart: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2314.FEPart.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to FEPart. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_guide_dxf_model(self) -> '_2316.GuideDxfModel':
        '''GuideDxfModel: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2316.GuideDxfModel.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to GuideDxfModel. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_mass_disc(self) -> '_2323.MassDisc':
        '''MassDisc: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2323.MassDisc.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to MassDisc. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_measurement_component(self) -> '_2324.MeasurementComponent':
        '''MeasurementComponent: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2324.MeasurementComponent.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to MeasurementComponent. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_mountable_component(self) -> '_2325.MountableComponent':
        '''MountableComponent: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2325.MountableComponent.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to MountableComponent. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_oil_seal(self) -> '_2327.OilSeal':
        '''OilSeal: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2327.OilSeal.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to OilSeal. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_planet_carrier(self) -> '_2330.PlanetCarrier':
        '''PlanetCarrier: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2330.PlanetCarrier.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to PlanetCarrier. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_point_load(self) -> '_2332.PointLoad':
        '''PointLoad: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2332.PointLoad.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to PointLoad. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_power_load(self) -> '_2333.PowerLoad':
        '''PowerLoad: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2333.PowerLoad.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to PowerLoad. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_unbalanced_mass(self) -> '_2338.UnbalancedMass':
        '''UnbalancedMass: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2338.UnbalancedMass.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to UnbalancedMass. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_virtual_component(self) -> '_2340.VirtualComponent':
        '''VirtualComponent: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2340.VirtualComponent.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to VirtualComponent. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_shaft(self) -> '_2343.Shaft':
        '''Shaft: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2343.Shaft.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to Shaft. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_agma_gleason_conical_gear(self) -> '_2373.AGMAGleasonConicalGear':
        '''AGMAGleasonConicalGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2373.AGMAGleasonConicalGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to AGMAGleasonConicalGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_bevel_differential_gear(self) -> '_2375.BevelDifferentialGear':
        '''BevelDifferentialGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2375.BevelDifferentialGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to BevelDifferentialGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_bevel_differential_planet_gear(self) -> '_2377.BevelDifferentialPlanetGear':
        '''BevelDifferentialPlanetGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2377.BevelDifferentialPlanetGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to BevelDifferentialPlanetGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_bevel_differential_sun_gear(self) -> '_2378.BevelDifferentialSunGear':
        '''BevelDifferentialSunGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2378.BevelDifferentialSunGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to BevelDifferentialSunGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_bevel_gear(self) -> '_2379.BevelGear':
        '''BevelGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2379.BevelGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to BevelGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_concept_gear(self) -> '_2381.ConceptGear':
        '''ConceptGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2381.ConceptGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to ConceptGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_conical_gear(self) -> '_2383.ConicalGear':
        '''ConicalGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2383.ConicalGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to ConicalGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_cylindrical_gear(self) -> '_2385.CylindricalGear':
        '''CylindricalGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2385.CylindricalGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to CylindricalGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_cylindrical_planet_gear(self) -> '_2387.CylindricalPlanetGear':
        '''CylindricalPlanetGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2387.CylindricalPlanetGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to CylindricalPlanetGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_face_gear(self) -> '_2388.FaceGear':
        '''FaceGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2388.FaceGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to FaceGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_gear(self) -> '_2390.Gear':
        '''Gear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2390.Gear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to Gear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_hypoid_gear(self) -> '_2394.HypoidGear':
        '''HypoidGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2394.HypoidGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to HypoidGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_klingelnberg_cyclo_palloid_conical_gear(self) -> '_2396.KlingelnbergCycloPalloidConicalGear':
        '''KlingelnbergCycloPalloidConicalGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2396.KlingelnbergCycloPalloidConicalGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to KlingelnbergCycloPalloidConicalGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self) -> '_2398.KlingelnbergCycloPalloidHypoidGear':
        '''KlingelnbergCycloPalloidHypoidGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2398.KlingelnbergCycloPalloidHypoidGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to KlingelnbergCycloPalloidHypoidGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> '_2400.KlingelnbergCycloPalloidSpiralBevelGear':
        '''KlingelnbergCycloPalloidSpiralBevelGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2400.KlingelnbergCycloPalloidSpiralBevelGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to KlingelnbergCycloPalloidSpiralBevelGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_spiral_bevel_gear(self) -> '_2403.SpiralBevelGear':
        '''SpiralBevelGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2403.SpiralBevelGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to SpiralBevelGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_straight_bevel_diff_gear(self) -> '_2405.StraightBevelDiffGear':
        '''StraightBevelDiffGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2405.StraightBevelDiffGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to StraightBevelDiffGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_straight_bevel_gear(self) -> '_2407.StraightBevelGear':
        '''StraightBevelGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2407.StraightBevelGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to StraightBevelGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_straight_bevel_planet_gear(self) -> '_2409.StraightBevelPlanetGear':
        '''StraightBevelPlanetGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2409.StraightBevelPlanetGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to StraightBevelPlanetGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_straight_bevel_sun_gear(self) -> '_2410.StraightBevelSunGear':
        '''StraightBevelSunGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2410.StraightBevelSunGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to StraightBevelSunGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_worm_gear(self) -> '_2411.WormGear':
        '''WormGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2411.WormGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to WormGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_zerol_bevel_gear(self) -> '_2413.ZerolBevelGear':
        '''ZerolBevelGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2413.ZerolBevelGear.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to ZerolBevelGear. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_cycloidal_disc(self) -> '_2429.CycloidalDisc':
        '''CycloidalDisc: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2429.CycloidalDisc.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to CycloidalDisc. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_ring_pins(self) -> '_2430.RingPins':
        '''RingPins: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2430.RingPins.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to RingPins. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_clutch_half(self) -> '_2439.ClutchHalf':
        '''ClutchHalf: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2439.ClutchHalf.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to ClutchHalf. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_concept_coupling_half(self) -> '_2442.ConceptCouplingHalf':
        '''ConceptCouplingHalf: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2442.ConceptCouplingHalf.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to ConceptCouplingHalf. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_coupling_half(self) -> '_2444.CouplingHalf':
        '''CouplingHalf: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2444.CouplingHalf.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to CouplingHalf. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_cvt_pulley(self) -> '_2447.CVTPulley':
        '''CVTPulley: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2447.CVTPulley.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to CVTPulley. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_part_to_part_shear_coupling_half(self) -> '_2449.PartToPartShearCouplingHalf':
        '''PartToPartShearCouplingHalf: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2449.PartToPartShearCouplingHalf.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to PartToPartShearCouplingHalf. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_pulley(self) -> '_2450.Pulley':
        '''Pulley: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2450.Pulley.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to Pulley. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_rolling_ring(self) -> '_2456.RollingRing':
        '''RollingRing: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2456.RollingRing.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to RollingRing. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_shaft_hub_connection(self) -> '_2458.ShaftHubConnection':
        '''ShaftHubConnection: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2458.ShaftHubConnection.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to ShaftHubConnection. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_spring_damper_half(self) -> '_2461.SpringDamperHalf':
        '''SpringDamperHalf: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2461.SpringDamperHalf.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to SpringDamperHalf. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_synchroniser_half(self) -> '_2464.SynchroniserHalf':
        '''SynchroniserHalf: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2464.SynchroniserHalf.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to SynchroniserHalf. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_synchroniser_part(self) -> '_2465.SynchroniserPart':
        '''SynchroniserPart: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2465.SynchroniserPart.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to SynchroniserPart. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_synchroniser_sleeve(self) -> '_2466.SynchroniserSleeve':
        '''SynchroniserSleeve: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2466.SynchroniserSleeve.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to SynchroniserSleeve. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_torque_converter_pump(self) -> '_2468.TorqueConverterPump':
        '''TorqueConverterPump: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2468.TorqueConverterPump.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to TorqueConverterPump. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def component_of_type_torque_converter_turbine(self) -> '_2470.TorqueConverterTurbine':
        '''TorqueConverterTurbine: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2470.TorqueConverterTurbine.TYPE not in self.wrapped.Component.__class__.__mro__:
            raise CastException('Failed to cast component to TorqueConverterTurbine. Expected: {}.'.format(self.wrapped.Component.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Component.__class__)(self.wrapped.Component) if self.wrapped.Component is not None else None

    @property
    def socket(self) -> '_2158.Socket':
        '''Socket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2158.Socket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to Socket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_bearing_inner_socket(self) -> '_2128.BearingInnerSocket':
        '''BearingInnerSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2128.BearingInnerSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to BearingInnerSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_bearing_outer_socket(self) -> '_2129.BearingOuterSocket':
        '''BearingOuterSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2129.BearingOuterSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to BearingOuterSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_cvt_pulley_socket(self) -> '_2136.CVTPulleySocket':
        '''CVTPulleySocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2136.CVTPulleySocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to CVTPulleySocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_cylindrical_socket(self) -> '_2138.CylindricalSocket':
        '''CylindricalSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2138.CylindricalSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to CylindricalSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_electric_machine_stator_socket(self) -> '_2140.ElectricMachineStatorSocket':
        '''ElectricMachineStatorSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2140.ElectricMachineStatorSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to ElectricMachineStatorSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_inner_shaft_socket(self) -> '_2141.InnerShaftSocket':
        '''InnerShaftSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2141.InnerShaftSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to InnerShaftSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_inner_shaft_socket_base(self) -> '_2142.InnerShaftSocketBase':
        '''InnerShaftSocketBase: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2142.InnerShaftSocketBase.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to InnerShaftSocketBase. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_mountable_component_inner_socket(self) -> '_2144.MountableComponentInnerSocket':
        '''MountableComponentInnerSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2144.MountableComponentInnerSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to MountableComponentInnerSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_mountable_component_outer_socket(self) -> '_2145.MountableComponentOuterSocket':
        '''MountableComponentOuterSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2145.MountableComponentOuterSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to MountableComponentOuterSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_mountable_component_socket(self) -> '_2146.MountableComponentSocket':
        '''MountableComponentSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2146.MountableComponentSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to MountableComponentSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_outer_shaft_socket(self) -> '_2147.OuterShaftSocket':
        '''OuterShaftSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2147.OuterShaftSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to OuterShaftSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_outer_shaft_socket_base(self) -> '_2148.OuterShaftSocketBase':
        '''OuterShaftSocketBase: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2148.OuterShaftSocketBase.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to OuterShaftSocketBase. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_planetary_socket(self) -> '_2150.PlanetarySocket':
        '''PlanetarySocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2150.PlanetarySocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to PlanetarySocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_planetary_socket_base(self) -> '_2151.PlanetarySocketBase':
        '''PlanetarySocketBase: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2151.PlanetarySocketBase.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to PlanetarySocketBase. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_pulley_socket(self) -> '_2152.PulleySocket':
        '''PulleySocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2152.PulleySocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to PulleySocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_rolling_ring_socket(self) -> '_2155.RollingRingSocket':
        '''RollingRingSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2155.RollingRingSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to RollingRingSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_shaft_socket(self) -> '_2156.ShaftSocket':
        '''ShaftSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2156.ShaftSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to ShaftSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_agma_gleason_conical_gear_teeth_socket(self) -> '_2162.AGMAGleasonConicalGearTeethSocket':
        '''AGMAGleasonConicalGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2162.AGMAGleasonConicalGearTeethSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to AGMAGleasonConicalGearTeethSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_bevel_differential_gear_teeth_socket(self) -> '_2164.BevelDifferentialGearTeethSocket':
        '''BevelDifferentialGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2164.BevelDifferentialGearTeethSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to BevelDifferentialGearTeethSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_bevel_gear_teeth_socket(self) -> '_2166.BevelGearTeethSocket':
        '''BevelGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2166.BevelGearTeethSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to BevelGearTeethSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_concept_gear_teeth_socket(self) -> '_2168.ConceptGearTeethSocket':
        '''ConceptGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2168.ConceptGearTeethSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to ConceptGearTeethSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_conical_gear_teeth_socket(self) -> '_2170.ConicalGearTeethSocket':
        '''ConicalGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2170.ConicalGearTeethSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to ConicalGearTeethSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_cylindrical_gear_teeth_socket(self) -> '_2172.CylindricalGearTeethSocket':
        '''CylindricalGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2172.CylindricalGearTeethSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to CylindricalGearTeethSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_face_gear_teeth_socket(self) -> '_2174.FaceGearTeethSocket':
        '''FaceGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2174.FaceGearTeethSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to FaceGearTeethSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_gear_teeth_socket(self) -> '_2176.GearTeethSocket':
        '''GearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2176.GearTeethSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to GearTeethSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_hypoid_gear_teeth_socket(self) -> '_2178.HypoidGearTeethSocket':
        '''HypoidGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2178.HypoidGearTeethSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to HypoidGearTeethSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_klingelnberg_conical_gear_teeth_socket(self) -> '_2179.KlingelnbergConicalGearTeethSocket':
        '''KlingelnbergConicalGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2179.KlingelnbergConicalGearTeethSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to KlingelnbergConicalGearTeethSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_klingelnberg_hypoid_gear_teeth_socket(self) -> '_2183.KlingelnbergHypoidGearTeethSocket':
        '''KlingelnbergHypoidGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2183.KlingelnbergHypoidGearTeethSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to KlingelnbergHypoidGearTeethSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_klingelnberg_spiral_bevel_gear_teeth_socket(self) -> '_2184.KlingelnbergSpiralBevelGearTeethSocket':
        '''KlingelnbergSpiralBevelGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2184.KlingelnbergSpiralBevelGearTeethSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to KlingelnbergSpiralBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_spiral_bevel_gear_teeth_socket(self) -> '_2186.SpiralBevelGearTeethSocket':
        '''SpiralBevelGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2186.SpiralBevelGearTeethSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to SpiralBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_straight_bevel_diff_gear_teeth_socket(self) -> '_2188.StraightBevelDiffGearTeethSocket':
        '''StraightBevelDiffGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2188.StraightBevelDiffGearTeethSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to StraightBevelDiffGearTeethSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_straight_bevel_gear_teeth_socket(self) -> '_2190.StraightBevelGearTeethSocket':
        '''StraightBevelGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2190.StraightBevelGearTeethSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to StraightBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_worm_gear_teeth_socket(self) -> '_2192.WormGearTeethSocket':
        '''WormGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2192.WormGearTeethSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to WormGearTeethSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_zerol_bevel_gear_teeth_socket(self) -> '_2194.ZerolBevelGearTeethSocket':
        '''ZerolBevelGearTeethSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2194.ZerolBevelGearTeethSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to ZerolBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_cycloidal_disc_axial_left_socket(self) -> '_2195.CycloidalDiscAxialLeftSocket':
        '''CycloidalDiscAxialLeftSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2195.CycloidalDiscAxialLeftSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to CycloidalDiscAxialLeftSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_cycloidal_disc_axial_right_socket(self) -> '_2196.CycloidalDiscAxialRightSocket':
        '''CycloidalDiscAxialRightSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2196.CycloidalDiscAxialRightSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to CycloidalDiscAxialRightSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_cycloidal_disc_inner_socket(self) -> '_2198.CycloidalDiscInnerSocket':
        '''CycloidalDiscInnerSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2198.CycloidalDiscInnerSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to CycloidalDiscInnerSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_cycloidal_disc_outer_socket(self) -> '_2199.CycloidalDiscOuterSocket':
        '''CycloidalDiscOuterSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2199.CycloidalDiscOuterSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to CycloidalDiscOuterSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_cycloidal_disc_planetary_bearing_socket(self) -> '_2201.CycloidalDiscPlanetaryBearingSocket':
        '''CycloidalDiscPlanetaryBearingSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2201.CycloidalDiscPlanetaryBearingSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to CycloidalDiscPlanetaryBearingSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_ring_pins_socket(self) -> '_2202.RingPinsSocket':
        '''RingPinsSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2202.RingPinsSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to RingPinsSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_clutch_socket(self) -> '_2205.ClutchSocket':
        '''ClutchSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2205.ClutchSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to ClutchSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_concept_coupling_socket(self) -> '_2207.ConceptCouplingSocket':
        '''ConceptCouplingSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2207.ConceptCouplingSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to ConceptCouplingSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_coupling_socket(self) -> '_2209.CouplingSocket':
        '''CouplingSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2209.CouplingSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to CouplingSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_part_to_part_shear_coupling_socket(self) -> '_2211.PartToPartShearCouplingSocket':
        '''PartToPartShearCouplingSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2211.PartToPartShearCouplingSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to PartToPartShearCouplingSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_spring_damper_socket(self) -> '_2213.SpringDamperSocket':
        '''SpringDamperSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2213.SpringDamperSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to SpringDamperSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_torque_converter_pump_socket(self) -> '_2215.TorqueConverterPumpSocket':
        '''TorqueConverterPumpSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2215.TorqueConverterPumpSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to TorqueConverterPumpSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def socket_of_type_torque_converter_turbine_socket(self) -> '_2216.TorqueConverterTurbineSocket':
        '''TorqueConverterTurbineSocket: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2216.TorqueConverterTurbineSocket.TYPE not in self.wrapped.Socket.__class__.__mro__:
            raise CastException('Failed to cast socket to TorqueConverterTurbineSocket. Expected: {}.'.format(self.wrapped.Socket.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Socket.__class__)(self.wrapped.Socket) if self.wrapped.Socket is not None else None

    @property
    def alignment_in_world_coordinate_system(self) -> '_2258.LinkComponentAxialPositionErrorReporter':
        '''LinkComponentAxialPositionErrorReporter: 'AlignmentInWorldCoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2258.LinkComponentAxialPositionErrorReporter)(self.wrapped.AlignmentInWorldCoordinateSystem) if self.wrapped.AlignmentInWorldCoordinateSystem is not None else None

    @property
    def alignment_in_fe_coordinate_system(self) -> '_2258.LinkComponentAxialPositionErrorReporter':
        '''LinkComponentAxialPositionErrorReporter: 'AlignmentInFECoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2258.LinkComponentAxialPositionErrorReporter)(self.wrapped.AlignmentInFECoordinateSystem) if self.wrapped.AlignmentInFECoordinateSystem is not None else None

    @property
    def alignment_in_component_coordinate_system(self) -> '_2258.LinkComponentAxialPositionErrorReporter':
        '''LinkComponentAxialPositionErrorReporter: 'AlignmentInComponentCoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2258.LinkComponentAxialPositionErrorReporter)(self.wrapped.AlignmentInComponentCoordinateSystem) if self.wrapped.AlignmentInComponentCoordinateSystem is not None else None

    @property
    def nodes(self) -> 'List[_2246.FESubstructureNode]':
        '''List[FESubstructureNode]: 'Nodes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Nodes, constructor.new(_2246.FESubstructureNode))
        return value

    @property
    def report_names(self) -> 'List[str]':
        '''List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ReportNames, str)
        return value

    def nodes_grouped_by_angle(self) -> 'OrderedDict[float, List[_2246.FESubstructureNode]]':
        ''' 'NodesGroupedByAngle' is the original name of this method.

        Returns:
            OrderedDict[float, List[mastapy.system_model.fe.FESubstructureNode]]
        '''

        return conversion.pn_to_mp_objects_in_list_in_ordered_dict(self.wrapped.NodesGroupedByAngle(), constructor.new(_2246.FESubstructureNode))

    def remove_all_nodes(self):
        ''' 'RemoveAllNodes' is the original name of this method.'''

        self.wrapped.RemoveAllNodes()

    def add_or_replace_node(self, node: '_2246.FESubstructureNode'):
        ''' 'AddOrReplaceNode' is the original name of this method.

        Args:
            node (mastapy.system_model.fe.FESubstructureNode)
        '''

        self.wrapped.AddOrReplaceNode(node.wrapped if node else None)

    def output_default_report_to(self, file_path: 'str'):
        ''' 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        '''

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        ''' 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        '''

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        ''' 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        '''

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        ''' 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        '''

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        ''' 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        '''

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        ''' 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        '''

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        ''' 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        '''

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        ''' 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        '''

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        ''' 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        '''

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result
