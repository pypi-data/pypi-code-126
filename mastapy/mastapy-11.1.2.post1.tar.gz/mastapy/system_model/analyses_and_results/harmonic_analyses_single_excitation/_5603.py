'''_5603.py

PartHarmonicAnalysisOfSingleExcitation
'''


from mastapy.system_model.part_model import (
    _2329, _2296, _2297, _2298,
    _2299, _2302, _2304, _2305,
    _2306, _2309, _2310, _2313,
    _2314, _2315, _2316, _2323,
    _2324, _2325, _2327, _2330,
    _2332, _2333, _2335, _2337,
    _2338, _2340
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model.shaft_model import _2343
from mastapy.system_model.part_model.gears import (
    _2373, _2374, _2375, _2376,
    _2377, _2378, _2379, _2380,
    _2381, _2382, _2383, _2384,
    _2385, _2386, _2387, _2388,
    _2389, _2390, _2392, _2394,
    _2395, _2396, _2397, _2398,
    _2399, _2400, _2401, _2402,
    _2403, _2404, _2405, _2406,
    _2407, _2408, _2409, _2410,
    _2411, _2412, _2413, _2414
)
from mastapy.system_model.part_model.cycloidal import _2428, _2429, _2430
from mastapy.system_model.part_model.couplings import (
    _2436, _2438, _2439, _2441,
    _2442, _2443, _2444, _2446,
    _2447, _2448, _2449, _2450,
    _2456, _2457, _2458, _2460,
    _2461, _2462, _2464, _2465,
    _2466, _2467, _2468, _2470
)
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5585
from mastapy.system_model.analyses_and_results.modal_analyses import (
    _5025, _4940, _4941, _4942,
    _4945, _4946, _4947, _4948,
    _4950, _4952, _4953, _4954,
    _4955, _4957, _4958, _4959,
    _4960, _4962, _4963, _4965,
    _4967, _4968, _4970, _4971,
    _4973, _4974, _4976, _4979,
    _4980, _4982, _4983, _4984,
    _4986, _4989, _4990, _4991,
    _4992, _4993, _4995, _4996,
    _4997, _4998, _5001, _5002,
    _5003, _5005, _5006, _5009,
    _5010, _5012, _5013, _5015,
    _5016, _5017, _5018, _5022,
    _5023, _5027, _5028, _5030,
    _5031, _5032, _5033, _5034,
    _5035, _5037, _5039, _5040,
    _5041, _5042, _5045, _5047,
    _5048, _5050, _5051, _5053,
    _5054, _5056, _5057, _5058,
    _5059, _5060, _5061, _5062,
    _5063, _5065, _5066, _5067,
    _5068, _5069, _5076, _5077,
    _5079, _5080
)
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5866
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6904
from mastapy.system_model.analyses_and_results.analysis_cases import _7379
from mastapy._internal.python_net import python_net_import

_PART_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'PartHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('PartHarmonicAnalysisOfSingleExcitation',)


class PartHarmonicAnalysisOfSingleExcitation(_7379.PartStaticLoadAnalysisCase):
    '''PartHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    '''

    TYPE = _PART_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PartHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2329.Part':
        '''Part: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2329.Part.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Part. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_assembly(self) -> '_2296.Assembly':
        '''Assembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2296.Assembly.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Assembly. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_abstract_assembly(self) -> '_2297.AbstractAssembly':
        '''AbstractAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2297.AbstractAssembly.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to AbstractAssembly. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_abstract_shaft(self) -> '_2298.AbstractShaft':
        '''AbstractShaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2298.AbstractShaft.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to AbstractShaft. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_abstract_shaft_or_housing(self) -> '_2299.AbstractShaftOrHousing':
        '''AbstractShaftOrHousing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2299.AbstractShaftOrHousing.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to AbstractShaftOrHousing. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_bearing(self) -> '_2302.Bearing':
        '''Bearing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2302.Bearing.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Bearing. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_bolt(self) -> '_2304.Bolt':
        '''Bolt: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2304.Bolt.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Bolt. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_bolted_joint(self) -> '_2305.BoltedJoint':
        '''BoltedJoint: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2305.BoltedJoint.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to BoltedJoint. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_component(self) -> '_2306.Component':
        '''Component: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2306.Component.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Component. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_connector(self) -> '_2309.Connector':
        '''Connector: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2309.Connector.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Connector. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_datum(self) -> '_2310.Datum':
        '''Datum: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2310.Datum.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Datum. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_external_cad_model(self) -> '_2313.ExternalCADModel':
        '''ExternalCADModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2313.ExternalCADModel.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ExternalCADModel. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_fe_part(self) -> '_2314.FEPart':
        '''FEPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2314.FEPart.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to FEPart. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_flexible_pin_assembly(self) -> '_2315.FlexiblePinAssembly':
        '''FlexiblePinAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2315.FlexiblePinAssembly.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to FlexiblePinAssembly. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_guide_dxf_model(self) -> '_2316.GuideDxfModel':
        '''GuideDxfModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2316.GuideDxfModel.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to GuideDxfModel. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_mass_disc(self) -> '_2323.MassDisc':
        '''MassDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2323.MassDisc.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to MassDisc. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_measurement_component(self) -> '_2324.MeasurementComponent':
        '''MeasurementComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2324.MeasurementComponent.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to MeasurementComponent. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_mountable_component(self) -> '_2325.MountableComponent':
        '''MountableComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2325.MountableComponent.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to MountableComponent. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_oil_seal(self) -> '_2327.OilSeal':
        '''OilSeal: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2327.OilSeal.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to OilSeal. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_planet_carrier(self) -> '_2330.PlanetCarrier':
        '''PlanetCarrier: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2330.PlanetCarrier.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to PlanetCarrier. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_point_load(self) -> '_2332.PointLoad':
        '''PointLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2332.PointLoad.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to PointLoad. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_power_load(self) -> '_2333.PowerLoad':
        '''PowerLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2333.PowerLoad.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to PowerLoad. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_root_assembly(self) -> '_2335.RootAssembly':
        '''RootAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2335.RootAssembly.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to RootAssembly. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_specialised_assembly(self) -> '_2337.SpecialisedAssembly':
        '''SpecialisedAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2337.SpecialisedAssembly.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to SpecialisedAssembly. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_unbalanced_mass(self) -> '_2338.UnbalancedMass':
        '''UnbalancedMass: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2338.UnbalancedMass.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to UnbalancedMass. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_virtual_component(self) -> '_2340.VirtualComponent':
        '''VirtualComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2340.VirtualComponent.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to VirtualComponent. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_shaft(self) -> '_2343.Shaft':
        '''Shaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2343.Shaft.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Shaft. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_agma_gleason_conical_gear(self) -> '_2373.AGMAGleasonConicalGear':
        '''AGMAGleasonConicalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2373.AGMAGleasonConicalGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to AGMAGleasonConicalGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_agma_gleason_conical_gear_set(self) -> '_2374.AGMAGleasonConicalGearSet':
        '''AGMAGleasonConicalGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2374.AGMAGleasonConicalGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to AGMAGleasonConicalGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_bevel_differential_gear(self) -> '_2375.BevelDifferentialGear':
        '''BevelDifferentialGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2375.BevelDifferentialGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelDifferentialGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_bevel_differential_gear_set(self) -> '_2376.BevelDifferentialGearSet':
        '''BevelDifferentialGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2376.BevelDifferentialGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelDifferentialGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_bevel_differential_planet_gear(self) -> '_2377.BevelDifferentialPlanetGear':
        '''BevelDifferentialPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2377.BevelDifferentialPlanetGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelDifferentialPlanetGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_bevel_differential_sun_gear(self) -> '_2378.BevelDifferentialSunGear':
        '''BevelDifferentialSunGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2378.BevelDifferentialSunGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelDifferentialSunGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_bevel_gear(self) -> '_2379.BevelGear':
        '''BevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2379.BevelGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_bevel_gear_set(self) -> '_2380.BevelGearSet':
        '''BevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2380.BevelGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_concept_gear(self) -> '_2381.ConceptGear':
        '''ConceptGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2381.ConceptGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConceptGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_concept_gear_set(self) -> '_2382.ConceptGearSet':
        '''ConceptGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2382.ConceptGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConceptGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_conical_gear(self) -> '_2383.ConicalGear':
        '''ConicalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2383.ConicalGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConicalGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_conical_gear_set(self) -> '_2384.ConicalGearSet':
        '''ConicalGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2384.ConicalGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConicalGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_cylindrical_gear(self) -> '_2385.CylindricalGear':
        '''CylindricalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2385.CylindricalGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to CylindricalGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_cylindrical_gear_set(self) -> '_2386.CylindricalGearSet':
        '''CylindricalGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2386.CylindricalGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to CylindricalGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_cylindrical_planet_gear(self) -> '_2387.CylindricalPlanetGear':
        '''CylindricalPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2387.CylindricalPlanetGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to CylindricalPlanetGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_face_gear(self) -> '_2388.FaceGear':
        '''FaceGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2388.FaceGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to FaceGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_face_gear_set(self) -> '_2389.FaceGearSet':
        '''FaceGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2389.FaceGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to FaceGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_gear(self) -> '_2390.Gear':
        '''Gear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2390.Gear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Gear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_gear_set(self) -> '_2392.GearSet':
        '''GearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2392.GearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to GearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_hypoid_gear(self) -> '_2394.HypoidGear':
        '''HypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2394.HypoidGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to HypoidGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_hypoid_gear_set(self) -> '_2395.HypoidGearSet':
        '''HypoidGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2395.HypoidGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to HypoidGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_conical_gear(self) -> '_2396.KlingelnbergCycloPalloidConicalGear':
        '''KlingelnbergCycloPalloidConicalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2396.KlingelnbergCycloPalloidConicalGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidConicalGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_conical_gear_set(self) -> '_2397.KlingelnbergCycloPalloidConicalGearSet':
        '''KlingelnbergCycloPalloidConicalGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2397.KlingelnbergCycloPalloidConicalGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidConicalGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self) -> '_2398.KlingelnbergCycloPalloidHypoidGear':
        '''KlingelnbergCycloPalloidHypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2398.KlingelnbergCycloPalloidHypoidGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidHypoidGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(self) -> '_2399.KlingelnbergCycloPalloidHypoidGearSet':
        '''KlingelnbergCycloPalloidHypoidGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2399.KlingelnbergCycloPalloidHypoidGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidHypoidGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> '_2400.KlingelnbergCycloPalloidSpiralBevelGear':
        '''KlingelnbergCycloPalloidSpiralBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2400.KlingelnbergCycloPalloidSpiralBevelGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidSpiralBevelGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self) -> '_2401.KlingelnbergCycloPalloidSpiralBevelGearSet':
        '''KlingelnbergCycloPalloidSpiralBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2401.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidSpiralBevelGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_planetary_gear_set(self) -> '_2402.PlanetaryGearSet':
        '''PlanetaryGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2402.PlanetaryGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to PlanetaryGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_spiral_bevel_gear(self) -> '_2403.SpiralBevelGear':
        '''SpiralBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2403.SpiralBevelGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to SpiralBevelGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_spiral_bevel_gear_set(self) -> '_2404.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2404.SpiralBevelGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to SpiralBevelGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_straight_bevel_diff_gear(self) -> '_2405.StraightBevelDiffGear':
        '''StraightBevelDiffGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2405.StraightBevelDiffGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelDiffGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_straight_bevel_diff_gear_set(self) -> '_2406.StraightBevelDiffGearSet':
        '''StraightBevelDiffGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2406.StraightBevelDiffGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelDiffGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_straight_bevel_gear(self) -> '_2407.StraightBevelGear':
        '''StraightBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2407.StraightBevelGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_straight_bevel_gear_set(self) -> '_2408.StraightBevelGearSet':
        '''StraightBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2408.StraightBevelGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_straight_bevel_planet_gear(self) -> '_2409.StraightBevelPlanetGear':
        '''StraightBevelPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2409.StraightBevelPlanetGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelPlanetGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_straight_bevel_sun_gear(self) -> '_2410.StraightBevelSunGear':
        '''StraightBevelSunGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2410.StraightBevelSunGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelSunGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_worm_gear(self) -> '_2411.WormGear':
        '''WormGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2411.WormGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to WormGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_worm_gear_set(self) -> '_2412.WormGearSet':
        '''WormGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2412.WormGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to WormGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_zerol_bevel_gear(self) -> '_2413.ZerolBevelGear':
        '''ZerolBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2413.ZerolBevelGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ZerolBevelGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_zerol_bevel_gear_set(self) -> '_2414.ZerolBevelGearSet':
        '''ZerolBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2414.ZerolBevelGearSet.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ZerolBevelGearSet. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_cycloidal_assembly(self) -> '_2428.CycloidalAssembly':
        '''CycloidalAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2428.CycloidalAssembly.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to CycloidalAssembly. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_cycloidal_disc(self) -> '_2429.CycloidalDisc':
        '''CycloidalDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2429.CycloidalDisc.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to CycloidalDisc. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_ring_pins(self) -> '_2430.RingPins':
        '''RingPins: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2430.RingPins.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to RingPins. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_belt_drive(self) -> '_2436.BeltDrive':
        '''BeltDrive: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2436.BeltDrive.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to BeltDrive. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_clutch(self) -> '_2438.Clutch':
        '''Clutch: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2438.Clutch.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Clutch. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_clutch_half(self) -> '_2439.ClutchHalf':
        '''ClutchHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2439.ClutchHalf.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ClutchHalf. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_concept_coupling(self) -> '_2441.ConceptCoupling':
        '''ConceptCoupling: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2441.ConceptCoupling.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConceptCoupling. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_concept_coupling_half(self) -> '_2442.ConceptCouplingHalf':
        '''ConceptCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2442.ConceptCouplingHalf.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConceptCouplingHalf. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_coupling(self) -> '_2443.Coupling':
        '''Coupling: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2443.Coupling.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Coupling. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_coupling_half(self) -> '_2444.CouplingHalf':
        '''CouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2444.CouplingHalf.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to CouplingHalf. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_cvt(self) -> '_2446.CVT':
        '''CVT: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2446.CVT.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to CVT. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_cvt_pulley(self) -> '_2447.CVTPulley':
        '''CVTPulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2447.CVTPulley.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to CVTPulley. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_part_to_part_shear_coupling(self) -> '_2448.PartToPartShearCoupling':
        '''PartToPartShearCoupling: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2448.PartToPartShearCoupling.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to PartToPartShearCoupling. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_part_to_part_shear_coupling_half(self) -> '_2449.PartToPartShearCouplingHalf':
        '''PartToPartShearCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2449.PartToPartShearCouplingHalf.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to PartToPartShearCouplingHalf. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_pulley(self) -> '_2450.Pulley':
        '''Pulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2450.Pulley.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Pulley. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_rolling_ring(self) -> '_2456.RollingRing':
        '''RollingRing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2456.RollingRing.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to RollingRing. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_rolling_ring_assembly(self) -> '_2457.RollingRingAssembly':
        '''RollingRingAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2457.RollingRingAssembly.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to RollingRingAssembly. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_shaft_hub_connection(self) -> '_2458.ShaftHubConnection':
        '''ShaftHubConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2458.ShaftHubConnection.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ShaftHubConnection. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_spring_damper(self) -> '_2460.SpringDamper':
        '''SpringDamper: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2460.SpringDamper.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to SpringDamper. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_spring_damper_half(self) -> '_2461.SpringDamperHalf':
        '''SpringDamperHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2461.SpringDamperHalf.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to SpringDamperHalf. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_synchroniser(self) -> '_2462.Synchroniser':
        '''Synchroniser: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2462.Synchroniser.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Synchroniser. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_synchroniser_half(self) -> '_2464.SynchroniserHalf':
        '''SynchroniserHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2464.SynchroniserHalf.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to SynchroniserHalf. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_synchroniser_part(self) -> '_2465.SynchroniserPart':
        '''SynchroniserPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2465.SynchroniserPart.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to SynchroniserPart. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_synchroniser_sleeve(self) -> '_2466.SynchroniserSleeve':
        '''SynchroniserSleeve: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2466.SynchroniserSleeve.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to SynchroniserSleeve. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_torque_converter(self) -> '_2467.TorqueConverter':
        '''TorqueConverter: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2467.TorqueConverter.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to TorqueConverter. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_torque_converter_pump(self) -> '_2468.TorqueConverterPump':
        '''TorqueConverterPump: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2468.TorqueConverterPump.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to TorqueConverterPump. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_torque_converter_turbine(self) -> '_2470.TorqueConverterTurbine':
        '''TorqueConverterTurbine: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2470.TorqueConverterTurbine.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to TorqueConverterTurbine. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def harmonic_analysis_of_single_excitation(self) -> '_5585.HarmonicAnalysisOfSingleExcitation':
        '''HarmonicAnalysisOfSingleExcitation: 'HarmonicAnalysisOfSingleExcitation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5585.HarmonicAnalysisOfSingleExcitation)(self.wrapped.HarmonicAnalysisOfSingleExcitation) if self.wrapped.HarmonicAnalysisOfSingleExcitation is not None else None

    @property
    def uncoupled_modal_analysis(self) -> '_5025.PartModalAnalysis':
        '''PartModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5025.PartModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to PartModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_abstract_assembly_modal_analysis(self) -> '_4940.AbstractAssemblyModalAnalysis':
        '''AbstractAssemblyModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4940.AbstractAssemblyModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to AbstractAssemblyModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_abstract_shaft_modal_analysis(self) -> '_4941.AbstractShaftModalAnalysis':
        '''AbstractShaftModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4941.AbstractShaftModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to AbstractShaftModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_abstract_shaft_or_housing_modal_analysis(self) -> '_4942.AbstractShaftOrHousingModalAnalysis':
        '''AbstractShaftOrHousingModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4942.AbstractShaftOrHousingModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to AbstractShaftOrHousingModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_agma_gleason_conical_gear_modal_analysis(self) -> '_4945.AGMAGleasonConicalGearModalAnalysis':
        '''AGMAGleasonConicalGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4945.AGMAGleasonConicalGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to AGMAGleasonConicalGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_agma_gleason_conical_gear_set_modal_analysis(self) -> '_4946.AGMAGleasonConicalGearSetModalAnalysis':
        '''AGMAGleasonConicalGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4946.AGMAGleasonConicalGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to AGMAGleasonConicalGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_assembly_modal_analysis(self) -> '_4947.AssemblyModalAnalysis':
        '''AssemblyModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4947.AssemblyModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to AssemblyModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_bearing_modal_analysis(self) -> '_4948.BearingModalAnalysis':
        '''BearingModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4948.BearingModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BearingModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_belt_drive_modal_analysis(self) -> '_4950.BeltDriveModalAnalysis':
        '''BeltDriveModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4950.BeltDriveModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BeltDriveModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_bevel_differential_gear_modal_analysis(self) -> '_4952.BevelDifferentialGearModalAnalysis':
        '''BevelDifferentialGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4952.BevelDifferentialGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BevelDifferentialGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_bevel_differential_gear_set_modal_analysis(self) -> '_4953.BevelDifferentialGearSetModalAnalysis':
        '''BevelDifferentialGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4953.BevelDifferentialGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BevelDifferentialGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_bevel_differential_planet_gear_modal_analysis(self) -> '_4954.BevelDifferentialPlanetGearModalAnalysis':
        '''BevelDifferentialPlanetGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4954.BevelDifferentialPlanetGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BevelDifferentialPlanetGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_bevel_differential_sun_gear_modal_analysis(self) -> '_4955.BevelDifferentialSunGearModalAnalysis':
        '''BevelDifferentialSunGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4955.BevelDifferentialSunGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BevelDifferentialSunGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_bevel_gear_modal_analysis(self) -> '_4957.BevelGearModalAnalysis':
        '''BevelGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4957.BevelGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BevelGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_bevel_gear_set_modal_analysis(self) -> '_4958.BevelGearSetModalAnalysis':
        '''BevelGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4958.BevelGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BevelGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_bolted_joint_modal_analysis(self) -> '_4959.BoltedJointModalAnalysis':
        '''BoltedJointModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4959.BoltedJointModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BoltedJointModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_bolt_modal_analysis(self) -> '_4960.BoltModalAnalysis':
        '''BoltModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4960.BoltModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to BoltModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_clutch_half_modal_analysis(self) -> '_4962.ClutchHalfModalAnalysis':
        '''ClutchHalfModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4962.ClutchHalfModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ClutchHalfModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_clutch_modal_analysis(self) -> '_4963.ClutchModalAnalysis':
        '''ClutchModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4963.ClutchModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ClutchModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_component_modal_analysis(self) -> '_4965.ComponentModalAnalysis':
        '''ComponentModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4965.ComponentModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ComponentModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_concept_coupling_half_modal_analysis(self) -> '_4967.ConceptCouplingHalfModalAnalysis':
        '''ConceptCouplingHalfModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4967.ConceptCouplingHalfModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ConceptCouplingHalfModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_concept_coupling_modal_analysis(self) -> '_4968.ConceptCouplingModalAnalysis':
        '''ConceptCouplingModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4968.ConceptCouplingModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ConceptCouplingModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_concept_gear_modal_analysis(self) -> '_4970.ConceptGearModalAnalysis':
        '''ConceptGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4970.ConceptGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ConceptGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_concept_gear_set_modal_analysis(self) -> '_4971.ConceptGearSetModalAnalysis':
        '''ConceptGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4971.ConceptGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ConceptGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_conical_gear_modal_analysis(self) -> '_4973.ConicalGearModalAnalysis':
        '''ConicalGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4973.ConicalGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ConicalGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_conical_gear_set_modal_analysis(self) -> '_4974.ConicalGearSetModalAnalysis':
        '''ConicalGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4974.ConicalGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ConicalGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_connector_modal_analysis(self) -> '_4976.ConnectorModalAnalysis':
        '''ConnectorModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4976.ConnectorModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ConnectorModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_coupling_half_modal_analysis(self) -> '_4979.CouplingHalfModalAnalysis':
        '''CouplingHalfModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4979.CouplingHalfModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to CouplingHalfModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_coupling_modal_analysis(self) -> '_4980.CouplingModalAnalysis':
        '''CouplingModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4980.CouplingModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to CouplingModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_cvt_modal_analysis(self) -> '_4982.CVTModalAnalysis':
        '''CVTModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4982.CVTModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to CVTModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_cvt_pulley_modal_analysis(self) -> '_4983.CVTPulleyModalAnalysis':
        '''CVTPulleyModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4983.CVTPulleyModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to CVTPulleyModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_cycloidal_assembly_modal_analysis(self) -> '_4984.CycloidalAssemblyModalAnalysis':
        '''CycloidalAssemblyModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4984.CycloidalAssemblyModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to CycloidalAssemblyModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_cycloidal_disc_modal_analysis(self) -> '_4986.CycloidalDiscModalAnalysis':
        '''CycloidalDiscModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4986.CycloidalDiscModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to CycloidalDiscModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_cylindrical_gear_modal_analysis(self) -> '_4989.CylindricalGearModalAnalysis':
        '''CylindricalGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4989.CylindricalGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to CylindricalGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_cylindrical_gear_set_modal_analysis(self) -> '_4990.CylindricalGearSetModalAnalysis':
        '''CylindricalGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4990.CylindricalGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to CylindricalGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_cylindrical_planet_gear_modal_analysis(self) -> '_4991.CylindricalPlanetGearModalAnalysis':
        '''CylindricalPlanetGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4991.CylindricalPlanetGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to CylindricalPlanetGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_datum_modal_analysis(self) -> '_4992.DatumModalAnalysis':
        '''DatumModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4992.DatumModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to DatumModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_external_cad_model_modal_analysis(self) -> '_4993.ExternalCADModelModalAnalysis':
        '''ExternalCADModelModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4993.ExternalCADModelModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ExternalCADModelModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_face_gear_modal_analysis(self) -> '_4995.FaceGearModalAnalysis':
        '''FaceGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4995.FaceGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to FaceGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_face_gear_set_modal_analysis(self) -> '_4996.FaceGearSetModalAnalysis':
        '''FaceGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4996.FaceGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to FaceGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_fe_part_modal_analysis(self) -> '_4997.FEPartModalAnalysis':
        '''FEPartModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4997.FEPartModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to FEPartModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_flexible_pin_assembly_modal_analysis(self) -> '_4998.FlexiblePinAssemblyModalAnalysis':
        '''FlexiblePinAssemblyModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4998.FlexiblePinAssemblyModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to FlexiblePinAssemblyModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_gear_modal_analysis(self) -> '_5001.GearModalAnalysis':
        '''GearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5001.GearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to GearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_gear_set_modal_analysis(self) -> '_5002.GearSetModalAnalysis':
        '''GearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5002.GearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to GearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_guide_dxf_model_modal_analysis(self) -> '_5003.GuideDxfModelModalAnalysis':
        '''GuideDxfModelModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5003.GuideDxfModelModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to GuideDxfModelModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_hypoid_gear_modal_analysis(self) -> '_5005.HypoidGearModalAnalysis':
        '''HypoidGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5005.HypoidGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to HypoidGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_hypoid_gear_set_modal_analysis(self) -> '_5006.HypoidGearSetModalAnalysis':
        '''HypoidGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5006.HypoidGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to HypoidGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_klingelnberg_cyclo_palloid_conical_gear_modal_analysis(self) -> '_5009.KlingelnbergCycloPalloidConicalGearModalAnalysis':
        '''KlingelnbergCycloPalloidConicalGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5009.KlingelnbergCycloPalloidConicalGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to KlingelnbergCycloPalloidConicalGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(self) -> '_5010.KlingelnbergCycloPalloidConicalGearSetModalAnalysis':
        '''KlingelnbergCycloPalloidConicalGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5010.KlingelnbergCycloPalloidConicalGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to KlingelnbergCycloPalloidConicalGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(self) -> '_5012.KlingelnbergCycloPalloidHypoidGearModalAnalysis':
        '''KlingelnbergCycloPalloidHypoidGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5012.KlingelnbergCycloPalloidHypoidGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to KlingelnbergCycloPalloidHypoidGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(self) -> '_5013.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis':
        '''KlingelnbergCycloPalloidHypoidGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5013.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to KlingelnbergCycloPalloidHypoidGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(self) -> '_5015.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis':
        '''KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5015.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(self) -> '_5016.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis':
        '''KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5016.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_mass_disc_modal_analysis(self) -> '_5017.MassDiscModalAnalysis':
        '''MassDiscModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5017.MassDiscModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to MassDiscModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_measurement_component_modal_analysis(self) -> '_5018.MeasurementComponentModalAnalysis':
        '''MeasurementComponentModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5018.MeasurementComponentModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to MeasurementComponentModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_mountable_component_modal_analysis(self) -> '_5022.MountableComponentModalAnalysis':
        '''MountableComponentModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5022.MountableComponentModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to MountableComponentModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_oil_seal_modal_analysis(self) -> '_5023.OilSealModalAnalysis':
        '''OilSealModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5023.OilSealModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to OilSealModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_part_to_part_shear_coupling_half_modal_analysis(self) -> '_5027.PartToPartShearCouplingHalfModalAnalysis':
        '''PartToPartShearCouplingHalfModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5027.PartToPartShearCouplingHalfModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to PartToPartShearCouplingHalfModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_part_to_part_shear_coupling_modal_analysis(self) -> '_5028.PartToPartShearCouplingModalAnalysis':
        '''PartToPartShearCouplingModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5028.PartToPartShearCouplingModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to PartToPartShearCouplingModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_planetary_gear_set_modal_analysis(self) -> '_5030.PlanetaryGearSetModalAnalysis':
        '''PlanetaryGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5030.PlanetaryGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to PlanetaryGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_planet_carrier_modal_analysis(self) -> '_5031.PlanetCarrierModalAnalysis':
        '''PlanetCarrierModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5031.PlanetCarrierModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to PlanetCarrierModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_point_load_modal_analysis(self) -> '_5032.PointLoadModalAnalysis':
        '''PointLoadModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5032.PointLoadModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to PointLoadModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_power_load_modal_analysis(self) -> '_5033.PowerLoadModalAnalysis':
        '''PowerLoadModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5033.PowerLoadModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to PowerLoadModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_pulley_modal_analysis(self) -> '_5034.PulleyModalAnalysis':
        '''PulleyModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5034.PulleyModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to PulleyModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_ring_pins_modal_analysis(self) -> '_5035.RingPinsModalAnalysis':
        '''RingPinsModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5035.RingPinsModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to RingPinsModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_rolling_ring_assembly_modal_analysis(self) -> '_5037.RollingRingAssemblyModalAnalysis':
        '''RollingRingAssemblyModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5037.RollingRingAssemblyModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to RollingRingAssemblyModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_rolling_ring_modal_analysis(self) -> '_5039.RollingRingModalAnalysis':
        '''RollingRingModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5039.RollingRingModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to RollingRingModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_root_assembly_modal_analysis(self) -> '_5040.RootAssemblyModalAnalysis':
        '''RootAssemblyModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5040.RootAssemblyModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to RootAssemblyModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_shaft_hub_connection_modal_analysis(self) -> '_5041.ShaftHubConnectionModalAnalysis':
        '''ShaftHubConnectionModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5041.ShaftHubConnectionModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ShaftHubConnectionModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_shaft_modal_analysis(self) -> '_5042.ShaftModalAnalysis':
        '''ShaftModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5042.ShaftModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ShaftModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_specialised_assembly_modal_analysis(self) -> '_5045.SpecialisedAssemblyModalAnalysis':
        '''SpecialisedAssemblyModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5045.SpecialisedAssemblyModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to SpecialisedAssemblyModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_spiral_bevel_gear_modal_analysis(self) -> '_5047.SpiralBevelGearModalAnalysis':
        '''SpiralBevelGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5047.SpiralBevelGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to SpiralBevelGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_spiral_bevel_gear_set_modal_analysis(self) -> '_5048.SpiralBevelGearSetModalAnalysis':
        '''SpiralBevelGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5048.SpiralBevelGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to SpiralBevelGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_spring_damper_half_modal_analysis(self) -> '_5050.SpringDamperHalfModalAnalysis':
        '''SpringDamperHalfModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5050.SpringDamperHalfModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to SpringDamperHalfModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_spring_damper_modal_analysis(self) -> '_5051.SpringDamperModalAnalysis':
        '''SpringDamperModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5051.SpringDamperModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to SpringDamperModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_straight_bevel_diff_gear_modal_analysis(self) -> '_5053.StraightBevelDiffGearModalAnalysis':
        '''StraightBevelDiffGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5053.StraightBevelDiffGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to StraightBevelDiffGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_straight_bevel_diff_gear_set_modal_analysis(self) -> '_5054.StraightBevelDiffGearSetModalAnalysis':
        '''StraightBevelDiffGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5054.StraightBevelDiffGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to StraightBevelDiffGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_straight_bevel_gear_modal_analysis(self) -> '_5056.StraightBevelGearModalAnalysis':
        '''StraightBevelGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5056.StraightBevelGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to StraightBevelGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_straight_bevel_gear_set_modal_analysis(self) -> '_5057.StraightBevelGearSetModalAnalysis':
        '''StraightBevelGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5057.StraightBevelGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to StraightBevelGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_straight_bevel_planet_gear_modal_analysis(self) -> '_5058.StraightBevelPlanetGearModalAnalysis':
        '''StraightBevelPlanetGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5058.StraightBevelPlanetGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to StraightBevelPlanetGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_straight_bevel_sun_gear_modal_analysis(self) -> '_5059.StraightBevelSunGearModalAnalysis':
        '''StraightBevelSunGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5059.StraightBevelSunGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to StraightBevelSunGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_synchroniser_half_modal_analysis(self) -> '_5060.SynchroniserHalfModalAnalysis':
        '''SynchroniserHalfModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5060.SynchroniserHalfModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to SynchroniserHalfModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_synchroniser_modal_analysis(self) -> '_5061.SynchroniserModalAnalysis':
        '''SynchroniserModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5061.SynchroniserModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to SynchroniserModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_synchroniser_part_modal_analysis(self) -> '_5062.SynchroniserPartModalAnalysis':
        '''SynchroniserPartModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5062.SynchroniserPartModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to SynchroniserPartModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_synchroniser_sleeve_modal_analysis(self) -> '_5063.SynchroniserSleeveModalAnalysis':
        '''SynchroniserSleeveModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5063.SynchroniserSleeveModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to SynchroniserSleeveModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_torque_converter_modal_analysis(self) -> '_5065.TorqueConverterModalAnalysis':
        '''TorqueConverterModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5065.TorqueConverterModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to TorqueConverterModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_torque_converter_pump_modal_analysis(self) -> '_5066.TorqueConverterPumpModalAnalysis':
        '''TorqueConverterPumpModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5066.TorqueConverterPumpModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to TorqueConverterPumpModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_torque_converter_turbine_modal_analysis(self) -> '_5067.TorqueConverterTurbineModalAnalysis':
        '''TorqueConverterTurbineModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5067.TorqueConverterTurbineModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to TorqueConverterTurbineModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_unbalanced_mass_modal_analysis(self) -> '_5068.UnbalancedMassModalAnalysis':
        '''UnbalancedMassModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5068.UnbalancedMassModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to UnbalancedMassModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_virtual_component_modal_analysis(self) -> '_5069.VirtualComponentModalAnalysis':
        '''VirtualComponentModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5069.VirtualComponentModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to VirtualComponentModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_worm_gear_modal_analysis(self) -> '_5076.WormGearModalAnalysis':
        '''WormGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5076.WormGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to WormGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_worm_gear_set_modal_analysis(self) -> '_5077.WormGearSetModalAnalysis':
        '''WormGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5077.WormGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to WormGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_zerol_bevel_gear_modal_analysis(self) -> '_5079.ZerolBevelGearModalAnalysis':
        '''ZerolBevelGearModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5079.ZerolBevelGearModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ZerolBevelGearModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def uncoupled_modal_analysis_of_type_zerol_bevel_gear_set_modal_analysis(self) -> '_5080.ZerolBevelGearSetModalAnalysis':
        '''ZerolBevelGearSetModalAnalysis: 'UncoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5080.ZerolBevelGearSetModalAnalysis.TYPE not in self.wrapped.UncoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast uncoupled_modal_analysis to ZerolBevelGearSetModalAnalysis. Expected: {}.'.format(self.wrapped.UncoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.UncoupledModalAnalysis.__class__)(self.wrapped.UncoupledModalAnalysis) if self.wrapped.UncoupledModalAnalysis is not None else None

    @property
    def harmonic_analysis_options(self) -> '_5866.HarmonicAnalysisOptions':
        '''HarmonicAnalysisOptions: 'HarmonicAnalysisOptions' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5866.HarmonicAnalysisOptions.TYPE not in self.wrapped.HarmonicAnalysisOptions.__class__.__mro__:
            raise CastException('Failed to cast harmonic_analysis_options to HarmonicAnalysisOptions. Expected: {}.'.format(self.wrapped.HarmonicAnalysisOptions.__class__.__qualname__))

        return constructor.new_override(self.wrapped.HarmonicAnalysisOptions.__class__)(self.wrapped.HarmonicAnalysisOptions) if self.wrapped.HarmonicAnalysisOptions is not None else None
