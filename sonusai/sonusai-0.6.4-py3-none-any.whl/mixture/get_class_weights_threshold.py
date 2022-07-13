from typing import Dict
from typing import List
from typing import Union

from sonusai import SonusAIError
from sonusai.mixture.mixdb import MixtureDatabase


def get_class_weights_threshold(mixdb: Union[MixtureDatabase, Dict]) -> List[float]:
    """Get the class weights threshold from a mixture database or a config."""
    if isinstance(mixdb, dict):
        class_weights_threshold = mixdb['class_weights_threshold']
        num_classes = mixdb['num_classes']
    else:
        class_weights_threshold = mixdb.class_weights_threshold
        num_classes = mixdb.num_classes

    if not isinstance(class_weights_threshold, list):
        class_weights_threshold = [class_weights_threshold] * num_classes

    if len(class_weights_threshold) != num_classes:
        raise SonusAIError(f'invalid class_weights_threshold length: {len(class_weights_threshold)}')

    return class_weights_threshold
