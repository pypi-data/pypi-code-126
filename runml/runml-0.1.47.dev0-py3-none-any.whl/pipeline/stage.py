import abc
from typing import Type, Dict, Set, Iterable, Any

import pandas

from runml import ColumnMapping
from runml.analyzers.base_analyzer import Analyzer
from runml.options import OptionsProvider


class PipelineStage:
    _analyzers: Set[Type[Analyzer]]

    options_provider: OptionsProvider

    def __init__(self):
        self._analyzers = set()

    def add_analyzer(self, analyzer_type: Type[Analyzer]):
        self._analyzers.add(analyzer_type)

    def analyzers(self) -> Iterable[Type[Analyzer]]:
        return self._analyzers

    @abc.abstractmethod
    def calculate(self, reference_data: pandas.DataFrame,
                  current_data: pandas.DataFrame,
                  column_mapping: ColumnMapping,
                  analyzers_results: Dict[Type[Analyzer], Any]):
        raise NotImplementedError()
