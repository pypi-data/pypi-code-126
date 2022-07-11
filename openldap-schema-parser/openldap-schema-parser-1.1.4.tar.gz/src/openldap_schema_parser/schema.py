from typing import List, Union

from openldap_schema_parser.attribute import Attribute
from openldap_schema_parser.objectclass import ObjectClass
from openldap_schema_parser.objectidentifier import ObjectIdentifier


class Schema:
    """Schema情報を保持するクラス

    :param str name: スキーマ名
    :param List[openldap_schema_parser.ObjectIdentifier] objectidentifier_list:
        スキーマで定義されているObjectIdentifierのリスト
    :param List[openldap_schema_parser.Attribute] attribute_list:
        スキーマで定義されているAttributeTypeのリスト
    :param List[openldap_schema_parser.ObjectClass] objectclass_list:
        スキーマで定義されているObjectClassのリスト
    """

    def __init__(self, name: str):
        self.name = name
        self.objectidentifier_list: List[ObjectIdentifier] = []
        self.attribute_list: List[Attribute] = []
        self.objectclass_list: List[ObjectClass] = []

    def __str__(self):
        args = [
            f"name={self.name}",
            f"objectidentifier_list={self.objectidentifier_list}",
            f"attribute_list={self.attribute_list}",
            f"objectclass_list={self.objectclass_list}",
        ]
        return f"Schema({', '.join(args)})"

    def __repr__(self):
        args = [
            f"name={self.name}",
        ]
        return f"Schema({', '.join(args)})"

    def expand_oid(self):
        """ObjectIdentifierの展開

        Schemaクラス内でObjectIdentifierを利用して表現されているOIDの値を、
        すべて実際のOIDの値に変換する
        """
        self.expand_oid_list(self.objectidentifier_list, self.objectidentifier_list)
        self.expand_oid_list(self.attribute_list, self.objectidentifier_list)
        self.expand_oid_list(self.objectclass_list, self.objectidentifier_list)

    def expand_oid_list(
        self,
        obj_list: List[Union[Attribute, ObjectClass, ObjectIdentifier]],
        macrooid_list: List[ObjectIdentifier],
    ):
        """任意のObjectIdentifierの展開

        Attribute, ObjectClass, ObjectIdentifier のリストを受け取り、
        ObjectIdentifierを利用して表現されているOIDの値を、
        実際のOIDの値に変換する。

        :param List[Union[Attribute, ObjectClass, ObjectIdentifier]] obj_list:
            OIDを変換したいAttribute, ObjectClass, ObjectIdentifierのリスト
        :param List[ObjectIdentifier] macrooid_list:
            OIDの変換に利用するObjectIdentifierのリスト
        """
        for target in obj_list:
            self._expand_oid_list(target, macrooid_list)

    def _expand_oid_list(
        self,
        obj: Union[Attribute, ObjectClass, ObjectIdentifier],
        macrooid_list: List[ObjectIdentifier],
    ):
        for macro in macrooid_list:
            self._expand_oid(obj, macro)

    def _expand_oid(
        self,
        obj: Union[Attribute, ObjectClass, ObjectIdentifier],
        macrooid: ObjectIdentifier,
    ) -> None:
        _oid = obj.oid.split(":")
        if len(_oid) == 2:
            key, suffix = _oid
            if macrooid.key == key:
                obj.oid = macrooid.get_oid(suffix)
