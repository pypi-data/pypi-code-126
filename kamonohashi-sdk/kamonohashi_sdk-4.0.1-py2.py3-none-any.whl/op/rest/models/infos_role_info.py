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


class InfosRoleInfo(object):
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
        'display_name': 'str',
        'id': 'int',
        'is_customed': 'bool',
        'is_origin': 'bool',
        'name': 'str',
        'sort_order': 'int',
        'user_group_tanant_map_id_lists': 'list[int]'
    }

    attribute_map = {
        'display_name': 'displayName',
        'id': 'id',
        'is_customed': 'isCustomed',
        'is_origin': 'isOrigin',
        'name': 'name',
        'sort_order': 'sortOrder',
        'user_group_tanant_map_id_lists': 'userGroupTanantMapIdLists'
    }

    def __init__(self, display_name=None, id=None, is_customed=None, is_origin=None, name=None, sort_order=None, user_group_tanant_map_id_lists=None):  # noqa: E501
        """InfosRoleInfo - a model defined in Swagger"""  # noqa: E501

        self._display_name = None
        self._id = None
        self._is_customed = None
        self._is_origin = None
        self._name = None
        self._sort_order = None
        self._user_group_tanant_map_id_lists = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id
        if is_customed is not None:
            self.is_customed = is_customed
        if is_origin is not None:
            self.is_origin = is_origin
        if name is not None:
            self.name = name
        if sort_order is not None:
            self.sort_order = sort_order
        if user_group_tanant_map_id_lists is not None:
            self.user_group_tanant_map_id_lists = user_group_tanant_map_id_lists

    @property
    def display_name(self):
        """Gets the display_name of this InfosRoleInfo.  # noqa: E501


        :return: The display_name of this InfosRoleInfo.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this InfosRoleInfo.


        :param display_name: The display_name of this InfosRoleInfo.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this InfosRoleInfo.  # noqa: E501


        :return: The id of this InfosRoleInfo.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InfosRoleInfo.


        :param id: The id of this InfosRoleInfo.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def is_customed(self):
        """Gets the is_customed of this InfosRoleInfo.  # noqa: E501


        :return: The is_customed of this InfosRoleInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_customed

    @is_customed.setter
    def is_customed(self, is_customed):
        """Sets the is_customed of this InfosRoleInfo.


        :param is_customed: The is_customed of this InfosRoleInfo.  # noqa: E501
        :type: bool
        """

        self._is_customed = is_customed

    @property
    def is_origin(self):
        """Gets the is_origin of this InfosRoleInfo.  # noqa: E501


        :return: The is_origin of this InfosRoleInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_origin

    @is_origin.setter
    def is_origin(self, is_origin):
        """Sets the is_origin of this InfosRoleInfo.


        :param is_origin: The is_origin of this InfosRoleInfo.  # noqa: E501
        :type: bool
        """

        self._is_origin = is_origin

    @property
    def name(self):
        """Gets the name of this InfosRoleInfo.  # noqa: E501


        :return: The name of this InfosRoleInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InfosRoleInfo.


        :param name: The name of this InfosRoleInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sort_order(self):
        """Gets the sort_order of this InfosRoleInfo.  # noqa: E501


        :return: The sort_order of this InfosRoleInfo.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this InfosRoleInfo.


        :param sort_order: The sort_order of this InfosRoleInfo.  # noqa: E501
        :type: int
        """

        self._sort_order = sort_order

    @property
    def user_group_tanant_map_id_lists(self):
        """Gets the user_group_tanant_map_id_lists of this InfosRoleInfo.  # noqa: E501


        :return: The user_group_tanant_map_id_lists of this InfosRoleInfo.  # noqa: E501
        :rtype: list[int]
        """
        return self._user_group_tanant_map_id_lists

    @user_group_tanant_map_id_lists.setter
    def user_group_tanant_map_id_lists(self, user_group_tanant_map_id_lists):
        """Sets the user_group_tanant_map_id_lists of this InfosRoleInfo.


        :param user_group_tanant_map_id_lists: The user_group_tanant_map_id_lists of this InfosRoleInfo.  # noqa: E501
        :type: list[int]
        """

        self._user_group_tanant_map_id_lists = user_group_tanant_map_id_lists

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
        if issubclass(InfosRoleInfo, dict):
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
        if not isinstance(other, InfosRoleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
