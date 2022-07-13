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
from typing import Optional

import tensorflow as tf
from mlcvzoo_base.api.net import NetConfiguration

from mlcvzoo_tf_classification.configuration import NetConfig

logger = logging.getLogger(__name__)


class BaseNet:
    def __init__(self, net: tf.keras.Model, net_config: NetConfig):
        self.net: tf.keras.Model = net
        self.net_config: NetConfig = net_config

    def store(
        self,
        configuration: Optional[NetConfiguration] = None,
        net_path: Optional[str] = None,
    ) -> None:
        """
        Stores net if a net_path is given

        Note:
        When model weights are stored, two files are generated
        by tf.keras.Model.save_weights: net_path.index and net_path.data-XXXXX-of-YYYYY.

        When a full model is stored, tf.keras.models.save_model generates a directory
        at net_path, that contains all accompanying files.

        Arguments:
            configuration: Optional value for the net's configuration
            net_path: Optional path to where the net is saved
        """

        if net_path is not None:
            if self.net_config.save_weights_only:
                self.net.save_weights(net_path)
            else:
                tf.keras.models.save_model(self.net, filepath=net_path)
        else:
            logger.warning("net_path is None, could not store weights")

    def restore(
        self,
        configuration: Optional[NetConfiguration] = None,
        net_path: Optional[str] = None,
    ) -> None:
        """
        Restores a net (loads weights) from a net_path if given.

        Note:
        When model weights are stored, two files are generated
        by tensorflow: net_path.index and net_path.data-XXXXX-of-YYYYY.
        If the config parameter "save_weights_only" is set to True, restore() calls
        the respective tensorflow function, which collects and loads these two files
        related to net_path.

        When a full model is stored, tensorflow generates a directory at net_path,
        that contains all accompanying files.
        If the config parameter "save_weights_only" is set to False, restore() calls
        the respective tensorflow function, which collects and loads the files
        within the directory at net_path.

        Arguments:
            configuration: Optional value for the net's configuration
            net_path: Optional path from where the net is loaded
        """

        if net_path is not None:
            if self.net_config.save_weights_only:
                self.net.load_weights(net_path)
            else:
                self.net = tf.keras.models.load_model(filepath=net_path)
        else:
            logger.warning("net_path is None, could not restore weights")
