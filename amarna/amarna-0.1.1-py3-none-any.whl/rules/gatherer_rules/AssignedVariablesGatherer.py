from dataclasses import dataclass
from typing import Optional, List

from lark import Tree
from amarna.rules.GenericGatherer import GenericGatherer
from amarna.Result import getPosition, PositionType


@dataclass
class LocalVariableAssignmentType:
    """Represents a variable assignment."""

    name: str
    position: PositionType
    file_location: str


class AssignedVariablesGatherer(GenericGatherer):
    """
    Gather all assigned variables.
    """

    GATHERER_NAME = "AssignedVariablesGatherer"

    def __init__(self) -> None:
        super().__init__()
        self.assigned_variables: List[LocalVariableAssignmentType] = []

    def get_gathered_data(self) -> List[LocalVariableAssignmentType]:
        return self.assigned_variables

    def code_element_local_var(self, tree: Tree) -> None:
        variable_name: Optional[str] = None

        for child in tree.children:
            if child.data == "identifier_def":
                variable_name = str(child.children[0])
                break

        assert variable_name

        var = LocalVariableType(variable_name, getPosition(tree), self.fname)
        self.assigned_variables.append(var)
