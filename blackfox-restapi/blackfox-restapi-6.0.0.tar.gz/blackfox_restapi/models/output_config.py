# coding: utf-8

"""
    BlackFox

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from blackfox_restapi.configuration import Configuration


class OutputConfig(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'range': 'Range',
        'encoding': 'bool'
    }

    attribute_map = {
        'range': 'range',
        'encoding': 'encoding'
    }

    def __init__(self, range=None, encoding=False, local_vars_configuration=None):  # noqa: E501
        """OutputConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._range = None
        self._encoding = None
        self.discriminator = None

        self.range = range
        if encoding is not None:
            self.encoding = encoding

    @property
    def range(self):
        """Gets the range of this OutputConfig.  # noqa: E501


        :return: The range of this OutputConfig.  # noqa: E501
        :rtype: Range
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this OutputConfig.


        :param range: The range of this OutputConfig.  # noqa: E501
        :type: Range
        """

        self._range = range

    @property
    def encoding(self):
        """Gets the encoding of this OutputConfig.  # noqa: E501


        :return: The encoding of this OutputConfig.  # noqa: E501
        :rtype: bool
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this OutputConfig.


        :param encoding: The encoding of this OutputConfig.  # noqa: E501
        :type: bool
        """

        self._encoding = encoding

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OutputConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OutputConfig):
            return True

        return self.to_dict() != other.to_dict()
