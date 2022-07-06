import marshmallow_dataclass
from marshmallow import pre_load

from datagen.modalities.textual.identities.keypoints import base


@marshmallow_dataclass.dataclass(base_schema=base.KeypointsSchema)
class SceneKeypoints(base.SceneKeypoints):
    ...
