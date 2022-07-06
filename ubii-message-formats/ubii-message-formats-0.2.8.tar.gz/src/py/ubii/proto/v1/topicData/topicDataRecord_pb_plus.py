"""
@generated by codestare-proto-plus.  Do not edit manually!
"""
from builtins import (
    bool,
    float,
    int,
    str,
)

from proto import (
    BOOL,
    DOUBLE,
    FLOAT,
    Field,
    INT32,
    MESSAGE,
    RepeatedField,
    STRING,
    module,
)

from proto.message import (
    Message,
)

from typing import (
    Iterable,
)

from ubii.proto.v1.dataStructure.color_pb_plus import (
    Color,
)

from ubii.proto.v1.dataStructure.image_pb_plus import (
    Image2D,
    Image2DList,
)

from ubii.proto.v1.dataStructure.keyEvent_pb_plus import (
    KeyEvent,
)

from ubii.proto.v1.dataStructure.lists_pb_plus import (
    BoolList,
    DoubleList,
    FloatList,
    Int32List,
    StringList,
)

from ubii.proto.v1.dataStructure.matrix3x2_pb_plus import (
    Matrix3x2,
)

from ubii.proto.v1.dataStructure.matrix4x4_pb_plus import (
    Matrix4x4,
)

from ubii.proto.v1.dataStructure.mouseEvent_pb_plus import (
    MouseEvent,
)

from ubii.proto.v1.dataStructure.myoEvent_pb_plus import (
    MyoEvent,
)

from ubii.proto.v1.dataStructure.object2d_pb_plus import (
    Object2D,
    Object2DList,
)

from ubii.proto.v1.dataStructure.object3d_pb_plus import (
    Object3D,
    Object3DList,
)

from ubii.proto.v1.dataStructure.pose2d_pb_plus import (
    Pose2D,
)

from ubii.proto.v1.dataStructure.pose3d_pb_plus import (
    Pose3D,
)

from ubii.proto.v1.dataStructure.quaternion_pb_plus import (
    Quaternion,
)

from ubii.proto.v1.dataStructure.touchEvent_pb_plus import (
    TouchEvent,
    TouchEventList,
)

from ubii.proto.v1.dataStructure.vector2_pb_plus import (
    Vector2,
    Vector2List,
)

from ubii.proto.v1.dataStructure.vector3_pb_plus import (
    Vector3,
    Vector3List,
)

from ubii.proto.v1.dataStructure.vector4_pb_plus import (
    Vector4,
    Vector4List,
)

from ubii.proto.v1.sessions.session_pb_plus import (
    Session,
)

from ubii.proto.v1.topicData.timestamp_pb_plus import (
    Timestamp,
)


__protobuf__ = module(
    package="ubii.proto.v1.topicData",
    marshal="ubii.proto.v1",
    manifest={
        "TopicDataRecord",
        "TopicDataRecordList",
    }
)


class TopicDataRecord(Message):
    """
    continuous index: 38

    .. admonition:: One Ofs

        This message defines the following *oneof* group[s]

        .. attribute:: type

            - 	:attr:`.double`
            - 	:attr:`.bool`
            - 	:attr:`.string`
            - 	:attr:`.int32`
            - 	:attr:`.float`
            - 	:attr:`.vector2`
            - 	:attr:`.vector2_list`
            - 	:attr:`.vector3`
            - 	:attr:`.vector3_list`
            - 	:attr:`.vector4`
            - 	:attr:`.vector4_list`
            - 	:attr:`.quaternion`
            - 	:attr:`.quaternion_list`
            - 	:attr:`.matrix3x2`
            - 	:attr:`.matrix4x4`
            - 	:attr:`.color`
            - 	:attr:`.touch_event`
            - 	:attr:`.touch_event_list`
            - 	:attr:`.key_event`
            - 	:attr:`.mouse_event`
            - 	:attr:`.myo_event`
            - 	:attr:`.pose2D`
            - 	:attr:`.pose3D`
            - 	:attr:`.object2D`
            - 	:attr:`.object3D`
            - 	:attr:`.object2D_list`
            - 	:attr:`.object3D_list`
            - 	:attr:`.int32_list`
            - 	:attr:`.float_list`
            - 	:attr:`.double_list`
            - 	:attr:`.string_list`
            - 	:attr:`.bool_list`
            - 	:attr:`.image2D`
            - 	:attr:`.image2D_list`
            - 	:attr:`.session`

    Attributes:
        topic (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~proto.primitives.ProtoType.STRING`
        timestamp (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.topicData.timestamp_pb_plus.Timestamp`
        client_id (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~proto.primitives.ProtoType.STRING`
        double (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~proto.primitives.ProtoType.DOUBLE` -- *oneof* :attr:`.type`
        bool (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~proto.primitives.ProtoType.BOOL` -- *oneof* :attr:`.type`
        string (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~proto.primitives.ProtoType.STRING` -- *oneof* :attr:`.type`
        int32 (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~proto.primitives.ProtoType.INT32` -- *oneof* :attr:`.type`
        float (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~proto.primitives.ProtoType.FLOAT` -- *oneof* :attr:`.type`
        vector2 (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.vector2_pb_plus.Vector2` -- *oneof* :attr:`.type`
        vector2_list (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.vector2_pb_plus.Vector2List` -- *oneof* :attr:`.type`
        vector3 (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.vector3_pb_plus.Vector3` -- *oneof* :attr:`.type`
        vector3_list (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.vector3_pb_plus.Vector3List` -- *oneof* :attr:`.type`
        vector4 (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.vector4_pb_plus.Vector4` -- *oneof* :attr:`.type`
        vector4_list (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.vector4_pb_plus.Vector4List` -- *oneof* :attr:`.type`
        quaternion (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.quaternion_pb_plus.Quaternion` -- *oneof*
            :attr:`.type`
        quaternion_list (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.quaternion_pb_plus.Quaternion` -- *oneof*
            :attr:`.type`
        matrix3x2 (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.matrix3x2_pb_plus.Matrix3x2` -- *oneof* :attr:`.type`
        matrix4x4 (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.matrix4x4_pb_plus.Matrix4x4` -- *oneof* :attr:`.type`
        color (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.color_pb_plus.Color` -- *oneof* :attr:`.type`
        touch_event (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.touchEvent_pb_plus.TouchEvent` -- *oneof*
            :attr:`.type`
        touch_event_list (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.touchEvent_pb_plus.TouchEventList` -- *oneof*
            :attr:`.type`
        key_event (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.keyEvent_pb_plus.KeyEvent` -- *oneof* :attr:`.type`
        mouse_event (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.mouseEvent_pb_plus.MouseEvent` -- *oneof*
            :attr:`.type`
        myo_event (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.myoEvent_pb_plus.MyoEvent` -- *oneof* :attr:`.type`
        pose2D (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.pose2d_pb_plus.Pose2D` -- *oneof* :attr:`.type`
        pose3D (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.pose3d_pb_plus.Pose3D` -- *oneof* :attr:`.type`
        object2D (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.object2d_pb_plus.Object2D` -- *oneof* :attr:`.type`
        object3D (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.object3d_pb_plus.Object3D` -- *oneof* :attr:`.type`
        object2D_list (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.object2d_pb_plus.Object2DList` -- *oneof*
            :attr:`.type`
        object3D_list (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.object3d_pb_plus.Object3DList` -- *oneof*
            :attr:`.type`
        int32_list (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.lists_pb_plus.Int32List` -- *oneof* :attr:`.type`
        float_list (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.lists_pb_plus.FloatList` -- *oneof* :attr:`.type`
        double_list (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.lists_pb_plus.DoubleList` -- *oneof* :attr:`.type`
        string_list (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.lists_pb_plus.StringList` -- *oneof* :attr:`.type`
        bool_list (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.lists_pb_plus.BoolList` -- *oneof* :attr:`.type`
        image2D (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.image_pb_plus.Image2D` -- *oneof* :attr:`.type`
        image2D_list (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.dataStructure.image_pb_plus.Image2DList` -- *oneof* :attr:`.type`
        session (proto.fields.Field): :obj:`~proto.fields.Field` of type
            :obj:`~ubii.proto.v1.sessions.session_pb_plus.Session` -- *oneof* :attr:`.type`
    """

    topic: str = Field(
        STRING,
        number=1,
    )
    timestamp: Timestamp = Field(
        MESSAGE,
        number=2,
        message=Timestamp,
    )
    client_id: str = Field(
        STRING,
        number=33,
    )
    double: float = Field(
        DOUBLE,
        number=3,
        oneof='type',
    )
    bool: bool = Field(
        BOOL,
        number=4,
        oneof='type',
    )
    string: str = Field(
        STRING,
        number=5,
        oneof='type',
    )
    int32: int = Field(
        INT32,
        number=23,
        oneof='type',
    )
    float: float = Field(
        FLOAT,
        number=24,
        oneof='type',
    )
    vector2: Vector2 = Field(
        MESSAGE,
        number=6,
        message=Vector2,
        oneof='type',
    )
    vector2_list: Vector2List = Field(
        MESSAGE,
        number=35,
        message=Vector2List,
        oneof='type',
    )
    vector3: Vector3 = Field(
        MESSAGE,
        number=7,
        message=Vector3,
        oneof='type',
    )
    vector3_list: Vector3List = Field(
        MESSAGE,
        number=36,
        message=Vector3List,
        oneof='type',
    )
    vector4: Vector4 = Field(
        MESSAGE,
        number=8,
        message=Vector4,
        oneof='type',
    )
    vector4_list: Vector4List = Field(
        MESSAGE,
        number=37,
        message=Vector4List,
        oneof='type',
    )
    quaternion: Quaternion = Field(
        MESSAGE,
        number=9,
        message=Quaternion,
        oneof='type',
    )
    quaternion_list: Quaternion = Field(
        MESSAGE,
        number=38,
        message=Quaternion,
        oneof='type',
    )
    matrix3x2: Matrix3x2 = Field(
        MESSAGE,
        number=10,
        message=Matrix3x2,
        oneof='type',
    )
    matrix4x4: Matrix4x4 = Field(
        MESSAGE,
        number=11,
        message=Matrix4x4,
        oneof='type',
    )
    color: Color = Field(
        MESSAGE,
        number=12,
        message=Color,
        oneof='type',
    )
    touch_event: TouchEvent = Field(
        MESSAGE,
        number=13,
        message=TouchEvent,
        oneof='type',
    )
    touch_event_list: TouchEventList = Field(
        MESSAGE,
        number=34,
        message=TouchEventList,
        oneof='type',
    )
    key_event: KeyEvent = Field(
        MESSAGE,
        number=14,
        message=KeyEvent,
        oneof='type',
    )
    mouse_event: MouseEvent = Field(
        MESSAGE,
        number=15,
        message=MouseEvent,
        oneof='type',
    )
    myo_event: MyoEvent = Field(
        MESSAGE,
        number=16,
        message=MyoEvent,
        oneof='type',
    )
    pose2D: Pose2D = Field(
        MESSAGE,
        number=17,
        message=Pose2D,
        oneof='type',
    )
    pose3D: Pose3D = Field(
        MESSAGE,
        number=18,
        message=Pose3D,
        oneof='type',
    )
    object2D: Object2D = Field(
        MESSAGE,
        number=19,
        message=Object2D,
        oneof='type',
    )
    object3D: Object3D = Field(
        MESSAGE,
        number=20,
        message=Object3D,
        oneof='type',
    )
    object2D_list: Object2DList = Field(
        MESSAGE,
        number=21,
        message=Object2DList,
        oneof='type',
    )
    object3D_list: Object3DList = Field(
        MESSAGE,
        number=22,
        message=Object3DList,
        oneof='type',
    )
    int32_list: Int32List = Field(
        MESSAGE,
        number=25,
        message=Int32List,
        oneof='type',
    )
    float_list: FloatList = Field(
        MESSAGE,
        number=26,
        message=FloatList,
        oneof='type',
    )
    double_list: DoubleList = Field(
        MESSAGE,
        number=27,
        message=DoubleList,
        oneof='type',
    )
    string_list: StringList = Field(
        MESSAGE,
        number=28,
        message=StringList,
        oneof='type',
    )
    bool_list: BoolList = Field(
        MESSAGE,
        number=29,
        message=BoolList,
        oneof='type',
    )
    image2D: Image2D = Field(
        MESSAGE,
        number=30,
        message=Image2D,
        oneof='type',
    )
    image2D_list: Image2DList = Field(
        MESSAGE,
        number=31,
        message=Image2DList,
        oneof='type',
    )
    session: Session = Field(
        MESSAGE,
        number=32,
        message=Session,
        oneof='type',
    )


class TopicDataRecordList(Message):
    """
    Attributes:
        elements (proto.fields.RepeatedField): :obj:`~proto.fields.RepeatedField` of type
            :obj:`~.TopicDataRecord`
    """

    elements: Iterable[TopicDataRecord] = RepeatedField(
        MESSAGE,
        number=1,
        message=TopicDataRecord,
    )

