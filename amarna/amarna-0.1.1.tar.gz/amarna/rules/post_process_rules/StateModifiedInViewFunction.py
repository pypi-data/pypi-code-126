from typing import Dict, List
from amarna.Result import Result, create_result

from amarna.rules.gatherer_rules.DeclaredFunctionsGatherer import (
    DeclaredFunctionsGatherer,
    FunctionType,
)


class UnenforcedViewRule:
    """
    Find state modifications in functions with @view decorator.
    """

    RULE_TEXT = "This function modifies state but is declared @view."
    RULE_NAME = "unenforced-view"

    def run_rule(self, gathered_data: Dict) -> List[Result]:
        declared_functions: List[FunctionType] = gathered_data[
            DeclaredFunctionsGatherer.GATHERER_NAME
        ]
        results = []

        for func in declared_functions:
            # ignore if it was called
            if func.name in all_called:
                continue

            # ignore cairo standard lib functions
            if "starkware/cairo/common/" in func.file_location:
                continue

            # ignore if it has a decorator that means it is not supposed to be called directly
            if any(decorator in self.UNUSED_FP_DECORATORS for decorator in func.decorators):
                continue

            result = create_result(
                func.file_location,
                self.RULE_NAME,
                self.RULE_TEXT,
                func.position,
            )
            results.append(result)

        return results
