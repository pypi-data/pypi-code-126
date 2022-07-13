from typing import Set

from lark import Tree, Token
from amarna.rules.GenericRule import GenericRule
from amarna.Result import create_result_token


class RevokedReferenceRule(GenericRule):
    """
    Check for usage of potentially revoked references.
    """

    RULE_TEXT = "Potentially revoked reference in use because of a function call inbetween reference declaration and usage."
    RULE_NAME = "revoked-reference"

    def code_block(self, tree: Tree) -> None:
        references_ap = ()
        func_calls = set()

        # gather all references that depend on ap
        for reference in tree.find_data("code_element_reference"):
            if list(reference.scan_values(lambda v: isinstance(v, Token) and (str(v) == "ap"))):
                for children_id in reference.children[0].find_data("identifier_def"):
                    references_ap.add(children_id.children[0], tree.index(reference))

        # gather all function calls
        for func in tree.find_data("function_call"):
            func_calls.add(func)

        used_ids: Set[Token] = set()
        # gather identifiers used in the code
        for code_child in tree.find_data("identifier"):
            print(code_child.children[0])
            used_ids.add(code_child.children[0])  # type: ignore

        # uninitialized_locals = local_variables - assigned_variables
        # if not uninitialized_locals:
        #     return

        # # gather all hint code and check if the variables are there
        # all_hints = ""
        # for hint in self.original_tree.find_data("code_element_hint"):
        #     all_hints += hint.children[0]

        # # for now just ignore if they're in a hint
        # used_in_hints = set()
        # for uninitialized in uninitialized_locals:
        #     if uninitialized.value in all_hints:
        #         used_in_hints.add(uninitialized)

        # uninitialized_locals = uninitialized_locals - used_in_hints

        # for tok in uninitialized_locals:
        #     result = create_result_token(
        #         self.fname,
        #         self.RULE_NAME,
        #         self.RULE_TEXT,
        #         tok,
        #     )
        #     self.results.append(result)
