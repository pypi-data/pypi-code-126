"""
This meta package is used to import the protobuf message types.

Note:
    Only import from :mod:`ubii.proto`, not directly from the module set in :obj:`ubii.proto.__proto_module__`
"""

try:
    from importlib.metadata import distribution, version, PackageNotFoundError
except ImportError:  # for Python<3.8
    from importlib_metadata import distribution, version, PackageNotFoundError

import proto
from more_itertools import take, pad_none

from .v1 import (
    Client,
    ClientList,
    ButtonEventType,
    HandGestureType,
    Color,
    Image2D,
    Image2DList,
    KeyEvent,
    StringList,
    DoubleList,
    FloatList,
    BoolList,
    Int32List,
    Matrix3x2,
    Matrix4x4,
    MouseEvent,
    MyoEvent,
    Object2D,
    Object2DList,
    Object3D,
    Object3DList,
    Pose2D,
    Pose3D,
    Quaternion,
    QuaternionList,
    TouchEvent,
    TouchEventList,
    Vector2,
    Vector2List,
    Vector3,
    Vector3List,
    Vector4,
    Vector4List,
    Vector8,
    Vector8List,
    Component,
    ComponentList,
    Device,
    DeviceList,
    TopicDemux,
    TopicDemuxList,
    TopicMux,
    TopicMuxList,
    Error,
    ErrorList,
    Success,
    SuccessList,
    LockstepProcessingRequest,
    LockstepProcessingReply,
    ProcessingMode,
    ModuleIO,
    ProcessingModule,
    ProcessingModuleList,
    Constants,
    Server,
    Service,
    ServiceList,
    ServiceReply,
    ServiceRequest,
    TopicSubscription,
    SessionStatus,
    TopicInputMapping,
    TopicInputMappingList,
    TopicOutputMapping,
    TopicOutputMappingList,
    IOMapping,
    IOMappingList,
    Session,
    SessionList,
    Timestamp,
    TopicData,
    TopicDataRecord,
    TopicDataRecordList,
)

__proto_types__ = (
    "Client",
    "ClientList",
    "ButtonEventType",
    "HandGestureType",
    "Color",
    "Image2D",
    "Image2DList",
    "KeyEvent",
    "StringList",
    "DoubleList",
    "FloatList",
    "BoolList",
    "Int32List",
    "Matrix3x2",
    "Matrix4x4",
    "MouseEvent",
    "MyoEvent",
    "Object2D",
    "Object2DList",
    "Object3D",
    "Object3DList",
    "Pose2D",
    "Pose3D",
    "Quaternion",
    "QuaternionList",
    "TouchEvent",
    "TouchEventList",
    "Vector2",
    "Vector2List",
    "Vector3",
    "Vector3List",
    "Vector4",
    "Vector4List",
    "Vector8",
    "Vector8List",
    "Component",
    "ComponentList",
    "Device",
    "DeviceList",
    "TopicDemux",
    "TopicDemuxList",
    "TopicMux",
    "TopicMuxList",
    "Error",
    "ErrorList",
    "Success",
    "SuccessList",
    "LockstepProcessingRequest",
    "LockstepProcessingReply",
    "ProcessingMode",
    "ModuleIO",
    "ProcessingModule",
    "ProcessingModuleList",
    "Constants",
    "Server",
    "Service",
    "ServiceList",
    "ServiceReply",
    "ServiceRequest",
    "TopicSubscription",
    "SessionStatus",
    "TopicInputMapping",
    "TopicInputMappingList",
    "TopicOutputMapping",
    "TopicOutputMappingList",
    "IOMapping",
    "IOMappingList",
    "Session",
    "SessionList",
    "Timestamp",
    "TopicData",
    "TopicDataRecord",
    "TopicDataRecordList",
)

from .util import (
    ProtoMeta,
    ProtoEncoder,
)

__all__ = __proto_types__ + (
    'ProtoMeta',
    'ProtoEncoder',
    '__protobuf__',
    '__proto_module__',
    '__proto_package__'
)

_pkg_name = 'ubii-message-formats'
try:
    __version__ = version(_pkg_name)
    info = take(2, pad_none(distribution(_pkg_name)
                            .read_text('proto_package.txt')
                            .split('='))
                )
except PackageNotFoundError as e:
    raise PackageNotFoundError(f"{_pkg_name} is not found, did the package name change?") from e
del _pkg_name

__proto_module__ = info[0]
"""
The actual import path of the module that contains the autogenerated protobuf code. Users are supposed to import from
:mod:`ubii.proto` instead.
"""
__proto_package__ = info[1]
"""
The name used for the :class:`~proto.marshal.Marshal`.
"""
__protobuf__ = proto.module(
    package=__proto_package__ or __proto_module__,
    manifest=set(__proto_types__)
)
"""
Used by :doc:`plus:index` to aggregate defined protobuf message in the same descriptor
pool. You need to import this attribute in every module that extends an existing protobuf wrapper class using
:class:`ubii.proto.ProtoMeta`. In essence this is a named tuple with attributes ``package`` and ``marshal`` containing 
the name for the :class:`~proto.marshal.Marshal` used by this package and ``manifest`` containing a set of all
:class:`~proto.message.Message` available from this module.

Example:
    You may want to create a extension to the wrapper around :class:`ubii.proto.Error`
    to be able to raise the error as an exception::

        from functools import lru_cache
        from proto.marshal import Marshal
        from proto.marshal.rules.message import MessageRule

        import ubii.proto as ub
        __protobuf__ = ub.__protobuf__


        class BaseError(ub.Error, Exception, metaclass=ub.ProtoMeta):
            @classmethod
            @lru_cache
            def rule(cls):
                return MessageRule(ub.Error.pb(), cls)

            @property
            def args(self):
                return self.title, self.message, self.stack

        class SessionRuntimeStopServiceError(BaseError):
            pass

        class OtherError(BaseError):
            pass

        class ErrorRule(MessageRule):
            def to_python(self, value, *, absent: bool | None = None):
                title = value.title or ''
                rule = None

                if title.startswith('SessionRuntimeStopService'):
                    rule = SessionRuntimeStopServiceError.rule()
                elif title.startswith('Other'):
                    rule = OtherError.rule()
                else:
                    rule = BaseError.rule()

                return rule.to_python(value, absent=absent)

            def to_proto(self, value):
                return super().to_proto(value)

        # register the new marshal rule to automatically convert errors

        Marshal(name=__protobuf__.marshal).register(ub.Error.pb(), ErrorRule(ub.Error.pb(), BaseError))
"""

if __proto_package__ is None:
    raise ImportError("package is not set in proto_package.txt from ubii-message-formats."
                      " This is unexpected, make sure you compiled the ubii-message-formats with a recent"
                      " version of the proto-plus-plugin. For more info resort to the documentation of the"
                      " proto-plus plugin")
