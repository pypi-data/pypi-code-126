# Copyright 2021 Open Logistics Foundation
#
# Licensed under the Open Logistics License 1.0.
# For details on the licensing terms, see the LICENSE file.

"""Module for building BaseAnnotation objects"""
from abc import ABC, abstractmethod

from mlcvzoo_base.api.data.annotation import BaseAnnotation


class AnnotationBuilder(ABC):

    """
    Super class for defining the methods that are needed to build a single
    instance of an BaseAnnotation.
    """

    @abstractmethod
    def build(
        self,
        image_path: str,
        annotation_path: str,
        image_dir: str,
        annotation_dir: str,
        replacement_string: str,
    ) -> BaseAnnotation:
        """
        Builds a BaseAnnotation object by the given parameters

        Args:
            image_path: String, points to an annotated image
            annotation_path: String, points to the respective annotation
            image_dir: String, points to the dir where the annotated image is stored
            annotation_dir: String, points to the dir where the respective annotation is stored
            replacement_string: String, part of the paths that is a placeholder

        Returns: a BaseAnnotation object

        """

        raise NotImplementedError()
