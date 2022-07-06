# coding: utf-8

"""
    KAMONOHASHI API

    A platform for deep learning  # noqa: E501

    OpenAPI spec version: v2
    Contact: kamonohashi-support@jp.nssol.nipponsteel.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DataSetApiModelsCreateInputModel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'entries': 'dict(str, list[DataSetApiModelsCreateInputModelEntry])',
        'flat_entries': 'list[DataSetApiModelsCreateInputModelEntry]',
        'is_flat': 'bool',
        'memo': 'str',
        'name': 'str'
    }

    attribute_map = {
        'entries': 'entries',
        'flat_entries': 'flatEntries',
        'is_flat': 'isFlat',
        'memo': 'memo',
        'name': 'name'
    }

    def __init__(self, entries=None, flat_entries=None, is_flat=None, memo=None, name=None):  # noqa: E501
        """DataSetApiModelsCreateInputModel - a model defined in Swagger"""  # noqa: E501

        self._entries = None
        self._flat_entries = None
        self._is_flat = None
        self._memo = None
        self._name = None
        self.discriminator = None

        self.entries = entries
        if flat_entries is not None:
            self.flat_entries = flat_entries
        if is_flat is not None:
            self.is_flat = is_flat
        if memo is not None:
            self.memo = memo
        self.name = name

    @property
    def entries(self):
        """Gets the entries of this DataSetApiModelsCreateInputModel.  # noqa: E501


        :return: The entries of this DataSetApiModelsCreateInputModel.  # noqa: E501
        :rtype: dict(str, list[DataSetApiModelsCreateInputModelEntry])
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this DataSetApiModelsCreateInputModel.


        :param entries: The entries of this DataSetApiModelsCreateInputModel.  # noqa: E501
        :type: dict(str, list[DataSetApiModelsCreateInputModelEntry])
        """
        if entries is None:
            raise ValueError("Invalid value for `entries`, must not be `None`")  # noqa: E501

        self._entries = entries

    @property
    def flat_entries(self):
        """Gets the flat_entries of this DataSetApiModelsCreateInputModel.  # noqa: E501


        :return: The flat_entries of this DataSetApiModelsCreateInputModel.  # noqa: E501
        :rtype: list[DataSetApiModelsCreateInputModelEntry]
        """
        return self._flat_entries

    @flat_entries.setter
    def flat_entries(self, flat_entries):
        """Sets the flat_entries of this DataSetApiModelsCreateInputModel.


        :param flat_entries: The flat_entries of this DataSetApiModelsCreateInputModel.  # noqa: E501
        :type: list[DataSetApiModelsCreateInputModelEntry]
        """

        self._flat_entries = flat_entries

    @property
    def is_flat(self):
        """Gets the is_flat of this DataSetApiModelsCreateInputModel.  # noqa: E501


        :return: The is_flat of this DataSetApiModelsCreateInputModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_flat

    @is_flat.setter
    def is_flat(self, is_flat):
        """Sets the is_flat of this DataSetApiModelsCreateInputModel.


        :param is_flat: The is_flat of this DataSetApiModelsCreateInputModel.  # noqa: E501
        :type: bool
        """

        self._is_flat = is_flat

    @property
    def memo(self):
        """Gets the memo of this DataSetApiModelsCreateInputModel.  # noqa: E501


        :return: The memo of this DataSetApiModelsCreateInputModel.  # noqa: E501
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this DataSetApiModelsCreateInputModel.


        :param memo: The memo of this DataSetApiModelsCreateInputModel.  # noqa: E501
        :type: str
        """

        self._memo = memo

    @property
    def name(self):
        """Gets the name of this DataSetApiModelsCreateInputModel.  # noqa: E501


        :return: The name of this DataSetApiModelsCreateInputModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataSetApiModelsCreateInputModel.


        :param name: The name of this DataSetApiModelsCreateInputModel.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DataSetApiModelsCreateInputModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DataSetApiModelsCreateInputModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
