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


class DataApiModelsDataFileOutputModel(object):
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
        'file_id': 'int',
        'file_name': 'str',
        'file_size': 'int',
        'id': 'int',
        'key': 'str',
        'url': 'str'
    }

    attribute_map = {
        'file_id': 'fileId',
        'file_name': 'fileName',
        'file_size': 'fileSize',
        'id': 'id',
        'key': 'key',
        'url': 'url'
    }

    def __init__(self, file_id=None, file_name=None, file_size=None, id=None, key=None, url=None):  # noqa: E501
        """DataApiModelsDataFileOutputModel - a model defined in Swagger"""  # noqa: E501

        self._file_id = None
        self._file_name = None
        self._file_size = None
        self._id = None
        self._key = None
        self._url = None
        self.discriminator = None

        if file_id is not None:
            self.file_id = file_id
        if file_name is not None:
            self.file_name = file_name
        if file_size is not None:
            self.file_size = file_size
        if id is not None:
            self.id = id
        if key is not None:
            self.key = key
        if url is not None:
            self.url = url

    @property
    def file_id(self):
        """Gets the file_id of this DataApiModelsDataFileOutputModel.  # noqa: E501


        :return: The file_id of this DataApiModelsDataFileOutputModel.  # noqa: E501
        :rtype: int
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this DataApiModelsDataFileOutputModel.


        :param file_id: The file_id of this DataApiModelsDataFileOutputModel.  # noqa: E501
        :type: int
        """

        self._file_id = file_id

    @property
    def file_name(self):
        """Gets the file_name of this DataApiModelsDataFileOutputModel.  # noqa: E501


        :return: The file_name of this DataApiModelsDataFileOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this DataApiModelsDataFileOutputModel.


        :param file_name: The file_name of this DataApiModelsDataFileOutputModel.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def file_size(self):
        """Gets the file_size of this DataApiModelsDataFileOutputModel.  # noqa: E501


        :return: The file_size of this DataApiModelsDataFileOutputModel.  # noqa: E501
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this DataApiModelsDataFileOutputModel.


        :param file_size: The file_size of this DataApiModelsDataFileOutputModel.  # noqa: E501
        :type: int
        """

        self._file_size = file_size

    @property
    def id(self):
        """Gets the id of this DataApiModelsDataFileOutputModel.  # noqa: E501


        :return: The id of this DataApiModelsDataFileOutputModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataApiModelsDataFileOutputModel.


        :param id: The id of this DataApiModelsDataFileOutputModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def key(self):
        """Gets the key of this DataApiModelsDataFileOutputModel.  # noqa: E501


        :return: The key of this DataApiModelsDataFileOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this DataApiModelsDataFileOutputModel.


        :param key: The key of this DataApiModelsDataFileOutputModel.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def url(self):
        """Gets the url of this DataApiModelsDataFileOutputModel.  # noqa: E501


        :return: The url of this DataApiModelsDataFileOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DataApiModelsDataFileOutputModel.


        :param url: The url of this DataApiModelsDataFileOutputModel.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(DataApiModelsDataFileOutputModel, dict):
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
        if not isinstance(other, DataApiModelsDataFileOutputModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
