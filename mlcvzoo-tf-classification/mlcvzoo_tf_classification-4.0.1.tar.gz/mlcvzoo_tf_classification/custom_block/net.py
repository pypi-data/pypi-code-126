# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
The net class is a wrapper for the Model class offered by keras.models.
CustomBlockNet builds a custom architecture inspired by VGG16.

The net class initializes the model architecture according to the specified parameters.
The respective parameters are read from the provided net_config.
A model can be initialized with pre-trained weights or random weights.
"""

import logging
import os
from typing import Optional

import tensorflow as tf
from mlcvzoo_base.api.net import Net, NetConfiguration
from tensorflow.keras.layers import Conv2D, Dense, Dropout, Flatten, Input, MaxPooling2D

from mlcvzoo_tf_classification.base_net import BaseNet
from mlcvzoo_tf_classification.configuration import NetConfig

logger = logging.getLogger(__name__)


class CustomBlockNet(Net, BaseNet):
    """
    Here, the specific layer and weight parameters are specified.
    """

    def __init__(self, net_config: NetConfig):

        self.net_config: NetConfig = net_config
        self.net: tf.keras.Model = None

        Net.__init__(self)

    def initialize(self) -> str:
        """
        Initializes the networks architecture and sets the instance's attribute self.net
        to a keras model which is initialized with the first and last layers of
        the defined architecture.

        Idea of using building blocks is inspired by VGG16.
        See respective arXiv paper: https://arxiv.org/pdf/1409.1556.pdf
        """

        # 1st block
        input1 = Input(shape=self.net_config.input_shape)  # (100, 100, 3))
        conv1_1 = Conv2D(
            filters=32,
            kernel_size=3,
            activation="relu",
            kernel_initializer="he_uniform",
            padding="same",
        )(input1)
        maxpool_1 = MaxPooling2D(pool_size=2)(conv1_1)
        drop_1 = Dropout(0.2)(maxpool_1)  # learns slower, but breaks in at end

        # 2nd block
        conv2_1 = Conv2D(
            filters=64,
            kernel_size=3,
            activation="relu",
            kernel_initializer="he_uniform",
            padding="same",
        )(drop_1)
        maxpool_2 = MaxPooling2D(pool_size=2)(conv2_1)
        drop_2 = Dropout(0.2)(maxpool_2)

        # 3rd block
        conv3_1 = Conv2D(
            filters=128,
            kernel_size=3,
            activation="relu",
            kernel_initializer="he_uniform",
            padding="same",
        )(drop_2)
        maxpool_3 = MaxPooling2D(pool_size=2)(conv3_1)
        drop_3 = Dropout(0.2)(maxpool_3)

        flatten = Flatten()(drop_3)
        dense_1 = Dense(units=128, activation="relu", kernel_initializer="he_uniform")(
            flatten
        )
        drop_4 = Dropout(0.5)(dense_1)
        dense_2 = Dense(units=self.net_config.number_classes, activation="softmax")(
            drop_4
        )

        if os.path.isfile(self.net_config.model_path):
            # Where to add weights into the custom model?
            self.restore(net_path=self.net_config.model_path)

        self.net = tf.keras.Model(inputs=input1, outputs=dense_2, name="custom_model")

        # TODO: what to return here?
        return ""

    def store(
        self,
        configuration: Optional[NetConfiguration] = None,
        net_path: Optional[str] = None,
    ) -> None:
        BaseNet.store(self, configuration=configuration, net_path=net_path)

    def restore(
        self,
        configuration: Optional[NetConfiguration] = None,
        net_path: Optional[str] = None,
    ) -> None:
        BaseNet.restore(self, configuration=configuration, net_path=net_path)
