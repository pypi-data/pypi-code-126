# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""
XceptionNet class is a wrapper for the Xception implementation of keras.application.xception.

The net class initializes the model architecture according to the specified parameters.
The respective parameters are read from the provided configuration files.
A model can be initialized with pre-trained weights or random weights.
The class also allows to add a custom top layer.
"""
import logging
import os
from typing import Optional

import tensorflow as tf
from mlcvzoo_base.api.net import Net, NetConfiguration
from tensorflow.keras.applications.xception import Xception

from mlcvzoo_tf_classification.base_net import BaseNet
from mlcvzoo_tf_classification.configuration import NetConfig

logger = logging.getLogger(__name__)


class XceptionNet(Net, BaseNet):
    """
    Here, the specific layer and weight parameters are specified.
    """

    def __init__(self, net_config: NetConfig):

        self.net_config: NetConfig = net_config
        self.net: tf.keras.Model

        Net.__init__(self)
        BaseNet.__init__(self, net=self.net, net_config=net_config)

    def initialize(self) -> str:
        """
        Initializes the networks architecture and sets the instance's attribute self.net
        to a keras model which is initialized with the first and last layers of
        the defined architecture.
        """

        input_shape_config = tuple(self.net_config.input_shape)

        weights_config = None
        # check both, as model_path can be either the preconfigured keras weights or
        # pretrained weights at path
        if self.net_config.model_path == "imagenet" or os.path.isfile(
            self.net_config.model_path
        ):
            weights_config = self.net_config.model_path

        self.net = Xception(
            # custom_net implies (not include_top)
            include_top=not self.net_config.build_custom_net,
            weights=weights_config,
            input_tensor=None,
            input_shape=input_shape_config,
            pooling=None,
            classes=self.net_config.number_classes,
            classifier_activation="softmax",
        )

        if self.net_config.build_custom_net:
            self.net.trainable = False
            # set input shape
            inputs = tf.keras.Input(shape=self.net.input_shape[1:])

            # set custom top
            previous_net_output = self.net(inputs, training=False)
            in_between_layer = tf.keras.layers.Flatten()(previous_net_output)
            outputs = tf.keras.layers.Dense(self.net_config.number_classes)(
                in_between_layer
            )

            self.net = tf.keras.Model(inputs, outputs)

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
