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


class XGBoostModel(object):
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
        'n_estimators': 'int',
        'max_depth': 'int',
        'min_child_weight': 'int',
        'gamma': 'float',
        'subsample': 'float',
        'colsample_bytree': 'float',
        'reg_alpha': 'float',
        'learning_rate': 'float',
        'feature_selection': 'list[bool]'
    }

    attribute_map = {
        'n_estimators': 'nEstimators',
        'max_depth': 'maxDepth',
        'min_child_weight': 'minChildWeight',
        'gamma': 'gamma',
        'subsample': 'subsample',
        'colsample_bytree': 'colsampleBytree',
        'reg_alpha': 'regAlpha',
        'learning_rate': 'learningRate',
        'feature_selection': 'featureSelection'
    }

    def __init__(self, n_estimators=None, max_depth=None, min_child_weight=None, gamma=None, subsample=None, colsample_bytree=None, reg_alpha=None, learning_rate=None, feature_selection=None, local_vars_configuration=None):  # noqa: E501
        """XGBoostModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._n_estimators = None
        self._max_depth = None
        self._min_child_weight = None
        self._gamma = None
        self._subsample = None
        self._colsample_bytree = None
        self._reg_alpha = None
        self._learning_rate = None
        self._feature_selection = None
        self.discriminator = None

        if n_estimators is not None:
            self.n_estimators = n_estimators
        if max_depth is not None:
            self.max_depth = max_depth
        if min_child_weight is not None:
            self.min_child_weight = min_child_weight
        if gamma is not None:
            self.gamma = gamma
        if subsample is not None:
            self.subsample = subsample
        if colsample_bytree is not None:
            self.colsample_bytree = colsample_bytree
        if reg_alpha is not None:
            self.reg_alpha = reg_alpha
        if learning_rate is not None:
            self.learning_rate = learning_rate
        self.feature_selection = feature_selection

    @property
    def n_estimators(self):
        """Gets the n_estimators of this XGBoostModel.  # noqa: E501

        NEstimators  # noqa: E501

        :return: The n_estimators of this XGBoostModel.  # noqa: E501
        :rtype: int
        """
        return self._n_estimators

    @n_estimators.setter
    def n_estimators(self, n_estimators):
        """Sets the n_estimators of this XGBoostModel.

        NEstimators  # noqa: E501

        :param n_estimators: The n_estimators of this XGBoostModel.  # noqa: E501
        :type: int
        """

        self._n_estimators = n_estimators

    @property
    def max_depth(self):
        """Gets the max_depth of this XGBoostModel.  # noqa: E501

        MaxDepth  # noqa: E501

        :return: The max_depth of this XGBoostModel.  # noqa: E501
        :rtype: int
        """
        return self._max_depth

    @max_depth.setter
    def max_depth(self, max_depth):
        """Sets the max_depth of this XGBoostModel.

        MaxDepth  # noqa: E501

        :param max_depth: The max_depth of this XGBoostModel.  # noqa: E501
        :type: int
        """

        self._max_depth = max_depth

    @property
    def min_child_weight(self):
        """Gets the min_child_weight of this XGBoostModel.  # noqa: E501

        MinChildWeight  # noqa: E501

        :return: The min_child_weight of this XGBoostModel.  # noqa: E501
        :rtype: int
        """
        return self._min_child_weight

    @min_child_weight.setter
    def min_child_weight(self, min_child_weight):
        """Sets the min_child_weight of this XGBoostModel.

        MinChildWeight  # noqa: E501

        :param min_child_weight: The min_child_weight of this XGBoostModel.  # noqa: E501
        :type: int
        """

        self._min_child_weight = min_child_weight

    @property
    def gamma(self):
        """Gets the gamma of this XGBoostModel.  # noqa: E501

        Gamma  # noqa: E501

        :return: The gamma of this XGBoostModel.  # noqa: E501
        :rtype: float
        """
        return self._gamma

    @gamma.setter
    def gamma(self, gamma):
        """Sets the gamma of this XGBoostModel.

        Gamma  # noqa: E501

        :param gamma: The gamma of this XGBoostModel.  # noqa: E501
        :type: float
        """

        self._gamma = gamma

    @property
    def subsample(self):
        """Gets the subsample of this XGBoostModel.  # noqa: E501

        Subsample  # noqa: E501

        :return: The subsample of this XGBoostModel.  # noqa: E501
        :rtype: float
        """
        return self._subsample

    @subsample.setter
    def subsample(self, subsample):
        """Sets the subsample of this XGBoostModel.

        Subsample  # noqa: E501

        :param subsample: The subsample of this XGBoostModel.  # noqa: E501
        :type: float
        """

        self._subsample = subsample

    @property
    def colsample_bytree(self):
        """Gets the colsample_bytree of this XGBoostModel.  # noqa: E501

        ColsampleBytree  # noqa: E501

        :return: The colsample_bytree of this XGBoostModel.  # noqa: E501
        :rtype: float
        """
        return self._colsample_bytree

    @colsample_bytree.setter
    def colsample_bytree(self, colsample_bytree):
        """Sets the colsample_bytree of this XGBoostModel.

        ColsampleBytree  # noqa: E501

        :param colsample_bytree: The colsample_bytree of this XGBoostModel.  # noqa: E501
        :type: float
        """

        self._colsample_bytree = colsample_bytree

    @property
    def reg_alpha(self):
        """Gets the reg_alpha of this XGBoostModel.  # noqa: E501

        RegAlpha  # noqa: E501

        :return: The reg_alpha of this XGBoostModel.  # noqa: E501
        :rtype: float
        """
        return self._reg_alpha

    @reg_alpha.setter
    def reg_alpha(self, reg_alpha):
        """Sets the reg_alpha of this XGBoostModel.

        RegAlpha  # noqa: E501

        :param reg_alpha: The reg_alpha of this XGBoostModel.  # noqa: E501
        :type: float
        """

        self._reg_alpha = reg_alpha

    @property
    def learning_rate(self):
        """Gets the learning_rate of this XGBoostModel.  # noqa: E501

        LearningRate  # noqa: E501

        :return: The learning_rate of this XGBoostModel.  # noqa: E501
        :rtype: float
        """
        return self._learning_rate

    @learning_rate.setter
    def learning_rate(self, learning_rate):
        """Sets the learning_rate of this XGBoostModel.

        LearningRate  # noqa: E501

        :param learning_rate: The learning_rate of this XGBoostModel.  # noqa: E501
        :type: float
        """

        self._learning_rate = learning_rate

    @property
    def feature_selection(self):
        """Gets the feature_selection of this XGBoostModel.  # noqa: E501

        Feature selection list  # noqa: E501

        :return: The feature_selection of this XGBoostModel.  # noqa: E501
        :rtype: list[bool]
        """
        return self._feature_selection

    @feature_selection.setter
    def feature_selection(self, feature_selection):
        """Sets the feature_selection of this XGBoostModel.

        Feature selection list  # noqa: E501

        :param feature_selection: The feature_selection of this XGBoostModel.  # noqa: E501
        :type: list[bool]
        """

        self._feature_selection = feature_selection

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
        if not isinstance(other, XGBoostModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XGBoostModel):
            return True

        return self.to_dict() != other.to_dict()
