from enum import Enum
from typing import List, Optional, Union


class STRUCTURAL_TYPE(str, Enum):
    """structuralの一覧"""

    ABSTRACT = "ABSTRACT"
    STRUCTURAL = "STRUCTURAL"
    AUXILIARY = "AUXILIARY"


class ObjectClass:
    """ObjectClassの情報を保持するクラス

    :param str oid: ObjectClassのOID。
    :param Union[str, List[str]] name:
        ObjectClassの属性名(NAME)。
        文字列で指定するか、文字列のリストで複数指定する。
        デフォルト値はNone
    :param str description: ObjectClassの説明(DESC)。デフォルト値はNone。
    :param bool obsolete: ObjectClassのOBSOLETE。デフォルト値はNone。
    :param List[str] sup: ObjectClassのSUP。デフォルト値はNone。
    :param STRUCTURAL_TYPE structural_type: ObjectClassのstructural情報。デフォルト値はNone。
    :param List[str] must: ObjectClassのMUST属性。デフォルト値は空リスト。
    :param List[str] may: ObjectClassのMAY属性。デフォルト値は空リスト。
    """

    def __init__(
        self,
        oid: str,
        name: Union[str, List[str]] = None,
        description: str = None,
        obsolete: bool = False,
        sup: List[str] = None,
        structural_type: STRUCTURAL_TYPE = None,
        must: List[str] = None,
        may: List[str] = None,
        **kwargs,
    ):
        self.oid = oid
        self.alias: Optional[List[str]] = None
        self.name: Optional[str] = None
        if isinstance(name, list):
            self.name = name[0]
            if 1 < len(name):
                self.alias = name[1:]
        else:
            self.name = name
        self.description = description
        self.obsolete = obsolete
        self.sup = sup
        self.structural_type = structural_type
        if must is None:
            must = []
        self.must = must
        if may is None:
            may = []
        self.may = may
        self.user_attrs = kwargs

    def __repr__(self):
        args = [
            f"oid={repr(self.oid)}",
            f"name={repr(self.name)}",
            f"alias={repr(self.alias)}",
            f"description={repr(self.description)}",
            f"obsolete={repr(self.obsolete)}",
            f"sup={repr(self.sup)}",
            f"structural_type={repr(self.structural_type)}",
            f"must={repr(self.must)}",
            f"may={repr(self.may)}",
        ]
        return f"ObjectClass({','.join(args)})"
