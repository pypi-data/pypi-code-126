'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1283 import ElectricMachineHarmonicLoadDataBase
    from ._1284 import HarmonicLoadDataBase
    from ._1285 import HarmonicLoadDataControlExcitationOptionBase
    from ._1286 import HarmonicLoadDataType
    from ._1287 import SpeedDependentHarmonicLoadData
