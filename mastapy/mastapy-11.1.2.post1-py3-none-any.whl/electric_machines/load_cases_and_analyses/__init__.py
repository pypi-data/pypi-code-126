'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1264 import DynamicForceAnalysis
    from ._1265 import DynamicForceLoadCase
    from ._1266 import EfficiencyMapAnalysis
    from ._1267 import EfficiencyMapLoadCase
    from ._1268 import ElectricMachineAnalysis
    from ._1269 import ElectricMachineFEAnalysis
    from ._1270 import ElectricMachineLoadCase
    from ._1271 import ElectricMachineLoadCaseBase
    from ._1272 import ElectricMachineLoadCaseGroup
    from ._1273 import LoadCaseType
    from ._1274 import LoadCaseTypeSelector
    from ._1275 import NonLinearDQModelMultipleOperatingPointsLoadCase
    from ._1276 import NumberOfStepsPerOperatingPointSpecificationMethod
    from ._1277 import OperatingPointsSpecificationMethod
    from ._1278 import SingleOperatingPointAnalysis
    from ._1279 import SpecifyTorqueOrCurrent
    from ._1280 import SpeedPointsDistribution
    from ._1281 import TorqueSpeedLoadCase
    from ._1282 import TorqueSpeedOperatingPoint
