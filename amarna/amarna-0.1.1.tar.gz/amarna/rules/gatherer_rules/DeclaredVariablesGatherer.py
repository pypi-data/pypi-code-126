from dataclasses import dataclass
from typing import Optional, List

from lark import Tree
from amarna.rules.GenericGatherer import GenericGatherer
from amarna.Result import getPosition, PositionType


@dataclass
class LocalVariableType:
    """Represents a variable declaration."""

    name: str
    position: PositionType
    file_location: str


class DeclaredVariablesGatherer(GenericGatherer):
    """
    Gather all declared local variables.
    """

    GATHERER_NAME = "DeclaredVariablesGatherer"

    def __init__(self) -> None:
        super().__init__()
        self.declared_variables: List[LocalVariableType] = []

    def get_gathered_data(self) -> List[LocalVariableType]:
        return self.declared_variables

    def code_element_local_var(self, tree: Tree) -> None:
        variable_name: Optional[str] = None

        for child in tree.children:
            if child.data == "identifier_def":
                variable_name = str(child.children[0])
                break

        # assert variable_name

        var = LocalVariableType(variable_name, getPosition(tree), self.fname)
        self.declared_variables.append(var)
