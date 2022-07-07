from io import BytesIO, StringIO

from prefect.engine.serializers import PandasSerializer, Serializer

PandasCSVSerializer = PandasSerializer(
    file_type="csv", serialize_kwargs={"index": False}
)

PandasParquetSerializer = PandasSerializer(
    file_type="parquet",
    serialize_kwargs={
        "index": False,
        "compression": "snappy",
        # "allow_truncated_timestamps": True,
        # "coerce_timestamps": "ms"
    },
)


class BytesSerializer(Serializer):
    """Serializer for saving/retrieving bytes from/to files"""

    def serialize(self, value: bytes) -> bytes:
        return value

    def deserialize(self, value: bytes) -> bytes:
        return value


class BytesIOSerializer(Serializer):
    """Serializer for saving/retrieving BytesIO objects"""

    def serialize(self, value: BytesIO) -> bytes:
        return value.getvalue()

    def deserialize(self, value: bytes) -> BytesIO:
        return BytesIO(value)


class StringIOSerializer(Serializer):
    """Serializer for saving/retrieving StringIO objects"""

    def serialize(self, value: StringIO) -> bytes:
        value.seek(0)
        return value.getvalue().encode()

    def deserialize(self, value: bytes) -> StringIO:
        return StringIO(value.decode("UTF-8"))
