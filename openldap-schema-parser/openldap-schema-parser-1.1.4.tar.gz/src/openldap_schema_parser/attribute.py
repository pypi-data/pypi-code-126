from enum import Enum
from typing import List, Optional, Union


class ATTRIBUTE_USAGE(str, Enum):
    """AttributeUsage一覧"""

    USER_APPLICATIONS = "userApplications"
    DIRECTORY_OPERATION = "directoryOperation"
    DISTRIBUTED_OPERATION = "distributedOperation"
    DSA_OPERATION = "dSAOperation"


class Attribute:
    """AttributeTypeの情報を保持するクラス

    :param str oid: AttributeTypeのOID
    :param List[str]] name:
        AttributeTypeの属性名(NAME)。
        文字列で指定するか、文字列のリストで複数指定する。
        デフォルト値はNone
    :param str description: AttributeTypeの説明(DESC)。デフォルト値はNone。
    :param bool obsolete: AttributeTypeのOBSOLETE。デフォルト値はFalse。
    :param str sup: AttributeTypeのSUP。デフォルト値はNone。
    :param str equality: AttributeTypeのEQUALITY。デフォルト値はNone。
    :param str ordering: AttributeTypeのORDERING。デフォルト値はNone。
    :param str substr: AttributeTypeのSUBSTR。デフォルト値はNone。
    :param str syntax: AttributeTypeのSYNTAX。デフォルト値はNone。
    :param bool single_value: AttributeTypeのSINGLE-VALUE。デフォルト値はFalse。
    :param bool collective: AttributeTypeのCOLLECTIVE。デフォルト値はFalse。
    :param bool no_user_modification: AttributeTypeのNO-USER-MODIFICATION。デフォルト値はFalse。
    :param ATTRIBUTE_USAGE usage: AttributeTypeのUSAGE。デフォルト値はNone。
    """

    def __init__(
        self,
        oid: str,
        name: Union[str, List[str]] = None,
        description: str = None,
        obsolete: bool = False,
        sup: str = None,
        equality: str = None,
        ordering: str = None,
        substr: str = None,
        syntax: str = None,
        single_value: bool = False,
        collective: bool = False,
        no_user_modification: bool = False,
        usage: ATTRIBUTE_USAGE = None,
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
        self.equality = equality
        self.ordering = ordering
        self.substr = substr
        self.syntax = syntax
        self.single_value = single_value
        self.collective = collective
        self.no_user_modification = no_user_modification
        self.usage = usage
        self.user_attrs = kwargs

    def _get_args_dict(self):
        result = {
            "oid": self.oid,
            "alias": self.alias,
            "name": self.name,
            "description": self.description,
            "obsolete": self.obsolete,
            "sup": self.sup,
            "equality": self.equality,
            "ordering": self.ordering,
            "substr": self.substr,
            "syntax": self.syntax,
            "single_value": self.single_value,
            "collective": self.collective,
            "no_user_modification": self.no_user_modification,
            "usage": self.usage,
        }
        return {k: v for k, v in result.items() if v is not None}

    def __repr__(self):
        args_dict = self._get_args_dict()
        args_list = [f"{k}={repr(v)}" for k, v in args_dict.items()]

        return f"Attribute({', '.join(args_list)})"
