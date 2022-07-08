# pylint: disable=no-self-argument, no-self-use,

import enum
import re
from typing import ClassVar, List, Pattern, Tuple, TypeVar, Union

import numpy as np
from pydantic import ConstrainedList, conlist, root_validator, validator
from pydantic.fields import ModelField
from typing_extensions import TypedDict

from ts_ids_core.annotations import Nullable, Required
from ts_ids_core.base.ids_element import IdsElement, SchemaExtraMetadataType
from ts_ids_core.base.ids_field import IdsField
from ts_ids_core.formatting import format_multiline_string


class Firmware(IdsElement):
    """
    See https://developers.tetrascience.com/docs/ids-design-conventions-schema-templates#firmware
    for specification.
    """

    name: Required[Nullable[str]]
    version: Required[Nullable[str]]


class Software(IdsElement):
    """
    See https://developers.tetrascience.com/docs/ids-design-conventions-schema-templates#software
    for specification.
    """

    name: Required[Nullable[str]]
    version: Required[Nullable[str]]


class System(IdsElement):
    """
    See https://developers.tetrascience.com/docs/ids-design-conventions-schema-templates#systems
    for specification of "systems". An instance of this class is one item in the
    `systems` array.
    """

    class Id(IdsElement):
        """System ID

        This globally shared `systems` field is not mandatory to use in all
        IDS models, which is why it's not defined as a field in the System
        object.

        To create a custom System model which uses this field, inherit from
        both the System class and this class.
        For example, the model below would have all the fields from System,
        Id, and Software: `vendor`, `model`, `type_`, `id_` and `software`.

        ```python
        class MySystem(System, System.Id, System.Software):
            pass
        ```

        This approach of using multiple inheritance reduces the opportunities
        for making mistakes compared with manually defining an "id" field in
        a custom System object, where the field name or type are open to
        mistakes.
        """

        id_: Nullable[str] = IdsField(alias="id")

    class Name(IdsElement):
        """System name

        This globally shared `systems` field is not mandatory to use in all
        IDS models, which is why it's not defined as a field in the System
        object.

        See `System.Id` for a general usage example
        """

        name: Nullable[str]

    class SerialNumber(IdsElement):
        """System serial number

        This globally shared `systems` field is not mandatory to use in all
        IDS models, which is why it's not defined as a field in the System
        object.

        See `System.Id` for a general usage example
        """

        serial_number: Nullable[str]

    class Firmware(IdsElement):
        """System firmware

        This globally shared `systems` field is not mandatory to use in all
        IDS models, which is why it's not defined as a field in the System
        object.

        See `System.Id` for a general usage example
        """

        firmware: List[Firmware]

    class Software(IdsElement):
        """System software

        This globally shared `systems` field is not mandatory to use in all
        IDS models, which is why it's not defined as a field in the System
        object.

        See `System.Id` for a general usage example
        """

        software: List[Software]

    vendor: Required[Nullable[str]]
    model: Required[Nullable[str]]
    type_: Required[Nullable[str]] = IdsField(alias="type")


class User(IdsElement):
    """
    See https://developers.tetrascience.com/docs/ids-design-conventions-schema-templates#users
    for specification of "users". An instance of this class is one item in the
    `users` array.
    """

    id_: Nullable[str] = IdsField(alias="id")
    name: Nullable[str]
    type_: Nullable[str] = IdsField(alias="type")


class ValueUnit(IdsElement):
    """
    See https://developers.tetrascience.com/docs/ids-design-conventions-schema-templates#value-unit-object
    for specification.
    """

    value: Required[Nullable[float]]
    unit: Required[Nullable[str]]


class RawTime(IdsElement):
    start: Nullable[str]
    created: Nullable[str]
    stop: Nullable[str]
    duration: Nullable[str]
    last_updated: Nullable[str]
    acquired: Nullable[str]
    modified: Nullable[str]
    lookup: Nullable[str]


class Time(RawTime):
    raw: RawTime


class RawSampleTime(RawTime):
    lookup: Required[Nullable[str]]


class SampleTime(RawSampleTime):
    raw: RawSampleTime


class Batch(IdsElement):
    id_: Nullable[str] = IdsField(alias="id")
    name: Nullable[str]
    barcode: Nullable[str]


class Set(IdsElement):
    id_: Nullable[str] = IdsField(alias="id")
    name: Nullable[str]


class Lot(IdsElement):
    id_: Nullable[str] = IdsField(alias="id")
    name: Nullable[str]


class Holder(IdsElement):
    name: Nullable[str]
    type_: Nullable[str] = IdsField(alias="type")
    barcode: Nullable[str]


class Location(IdsElement):
    position: Nullable[str]
    row: Nullable[float]
    column: Nullable[float]
    index: Nullable[float]
    holder: Holder


class Source(IdsElement):
    name: Required[Nullable[str]]
    type_: Required[Nullable[str]] = IdsField(alias="type")


# pylint: disable=invalid-name
class ValueDataType(str, enum.Enum):
    string = "string"
    number = "number"
    boolean = "boolean"


class Property(IdsElement):
    source: Required[Source]
    name: Required[str] = IdsField(description="This is the property name")
    value: Required[str] = IdsField(
        description="The original string value of the parameter"
    )
    value_data_type: Required[ValueDataType] = IdsField(
        description="This is the type of the original value"
    )
    string_value: Required[Nullable[str]] = IdsField(
        description=format_multiline_string(
            """
            If string_value has a value, then numerical_value,
            numerical_value_unit, and boolean_value all have to be null
            """
        )
    )
    numerical_value: Required[Nullable[float]] = IdsField(
        description=format_multiline_string(
            """
            If numerical_value has a value, then string_value and
            boolean_value both have to be null
            """
        )
    )
    numerical_value_unit: Required[Nullable[str]]
    boolean_value: Required[Nullable[bool]] = IdsField(
        description=format_multiline_string(
            """
            If boolean_value has a value, then numerical_value, numerical_value_unit,
            and string_value all have to be null
            """
        )
    )
    time: Required[SampleTime]


class Label(IdsElement):
    source: Required[Source]
    name: Required[str]
    value: Required[str]
    time: Required[SampleTime]


class Sample(IdsElement):
    """
    See [here](https://developers.tetrascience.com/docs/ids-design-conventions-schema-templates#samples)
    for specification of "samples". An instance of this class is one item in the
    `samples` array.
    """

    id_: Nullable[str] = IdsField(alias="id")
    name: Nullable[str]
    barcode: Nullable[str]
    batch: Batch
    set_: Set = IdsField(alias="set")
    lot: Lot
    location: Location
    properties: List[Property]
    labels: List[Label]


class Checksum(IdsElement):
    value: str
    algorithm: Nullable[str]


class Pointer(IdsElement):
    fileKey: Required[str]
    version: Required[str]
    bucket: Required[str]
    type_: Required[str] = IdsField(alias="type")
    fileId: Required[str]


class RelatedFile(IdsElement):
    """
    See https://developers.tetrascience.com/docs/ids-design-conventions-schema-templates#related-files
    for specification of "related_files". One instance of this class is an item in
    the `related_files` array.
    """

    name: Nullable[str]
    path: Nullable[str]
    size: ValueUnit
    checksum: Checksum
    pointer: Required[Pointer]


MeasureValue = TypeVar("MeasureValue")


class Measure(IdsElement):
    name: Required[Nullable[str]]
    unit: Required[Nullable[str]]
    # Override this list nesting level to match the number of dimensions
    value: Required[List[List[float]]]

    @validator("value")
    def validate_value_shape(cls, value: MeasureValue) -> MeasureValue:
        """
        Validate shape of multi-dimensional array stored in Measure.value
        """
        try:
            np.array(value, dtype=float)
        except ValueError as error:
            raise ValueError(
                "Measure values could not be converted to a valid multidimensional array. "
                "Nested sequences may have inconsistent length or shape, making this a ragged array."
            ) from error

        return value

    @property
    def shape(self) -> Tuple[int, ...]:
        """
        Return shape of the multi-dimensional stored in Measure.value
        """
        return np.array(self.value).shape

    @property
    def size(self) -> Tuple[int, ...]:
        """
        Return size of the multi-dimensional stored in Measure.value
        """
        return np.array(self.value).size


class Dimension(IdsElement):
    name: Required[Nullable[str]]
    unit: Required[Nullable[str]]
    scale: Required[List[Nullable[float]]]


class DataCubeDict(TypedDict):
    """Type hint for the dictionary form of `DataCube`."""

    name: Nullable[str]
    measures: List[Measure]
    dimensions: List[Dimension]


class DataCube(IdsElement):
    """
    See https://developers.tetrascience.com/docs/ids-design-conventions-schema-templates#datacubes-pattern
    for specification of "datacubes". One instance of this class is an item in
    the `datacubes` array.
    """

    name: Required[Nullable[str]]
    # Override min_items and max_items with the required number of measures
    measures: Required[conlist(Measure, min_items=1, max_items=1)]
    # Override min_items and max_items with the required number of dimensions
    dimensions: Required[conlist(Dimension, min_items=2, max_items=2)]

    @validator("measures", "dimensions", pre=True)
    def validate_min_max_items_are_equal(
        cls, value: Union[List[Measure], List[Dimension]], field: ModelField
    ) -> Union[List[Measure], List[Dimension]]:
        """
        Make sure min_items and max_items are equal for
        measures and dimension respectively
        """
        if not issubclass(field.outer_type_, ConstrainedList):
            raise TypeError(
                f"{cls.__name__}.{field.name} is {field.outer_type_}. Instead it must be a 'Constrained List' type"
            )

        if not field.outer_type_.min_items == field.outer_type_.max_items:
            raise ValueError(
                f"{cls.__name__}.{field.name}: min_items and max_items must be equal"
            )

        # Here min_items and max_items are equal.
        # Just make sure they are not zero
        if field.outer_type_.min_items == 0:
            raise ValueError(
                f"{cls.__name__}.{field.name}: min_items and max_items can not be 0."
            )

        return value

    @root_validator(skip_on_failure=True)
    def consistent_number_of_dimensions(cls, values: DataCubeDict) -> DataCubeDict:
        """
        Make sure for each measure, the dimensionality of its `value`
        is equal to the length of `dimensions`

        `skip_on_failure=True` means this validator will be run after field validation.
        Thus, the `values` arg (dict) is guaranteed to contain all field names and values.
        """
        dimensions = values["dimensions"]
        measures = values["measures"]

        # Filter out non empty measures[*].value
        measures = [measure for measure in measures if measure.size > 0]

        expected_dimensions = len(dimensions)
        expected_shape = tuple((len(dimension.scale) for dimension in dimensions))

        shape_of_measures = [measure.shape for measure in measures]
        dimensions_of_measures = [len(shape) for shape in shape_of_measures]

        invalid_measures_dimensions = [
            index
            for index, dimension in enumerate(dimensions_of_measures)
            if dimension != expected_dimensions
        ]

        if len(invalid_measures_dimensions) > 0:
            raise ValueError(
                f"Items in the measures[*].value lists are expected to have dimesions '{expected_dimensions}'. "
                f"Invalid dimensions detected at measures{invalid_measures_dimensions}."
            )

        invalid_measures_shape = [
            index
            for index, shape in enumerate(shape_of_measures)
            if shape != expected_shape
        ]

        if len(invalid_measures_shape) > 0:
            raise ValueError(
                f"Items in the measures[*].value lists are expected to have shape '{expected_shape}'. "
                f"Invalid shapes detected at measures{invalid_measures_shape}."
            )

        return values


class Parameter(IdsElement):
    """
    See https://developers.tetrascience.com/docs/ids-design-conventions-schema-templates#parameter-pattern
    for specification. An instance of this class is the value in the JSON object
    specified in "Parameter Pattern".
    """

    key: str = IdsField(description="This is the property name")
    value: str = IdsField(
        description="The original string value of the parameter from the raw file"
    )
    value_data_type: ValueDataType = IdsField(
        description="This is the true type of the original value"
    )
    string_value: Nullable[str] = IdsField(
        description=format_multiline_string(
            """
            If string_value has a value, then numerical_value, numerical_value_unit
            and boolean_value have to be null"""
        )
    )
    numerical_value: Nullable[float] = IdsField(
        description=format_multiline_string(
            """
            If numerical_value has a value, then string_value and boolean_value
            have to be null
            """
        )
    )
    numerical_value_unit: Nullable[str]
    boolean_value: Nullable[bool] = IdsField(
        description=format_multiline_string(
            """
            If boolean_value has a value, then numerical_value,
            numerical_value_unit and string_value have to be null
            """
        )
    )


class ModifierType(enum.Enum):
    """
    See the "modifier" schema specification [here](https://developers.tetrascience.com/docs/ids-design-conventions-schemajson#modifier-pattern).
    """

    LESS_THAN = "<"
    GREATER_THAN = ">"
    LESS_THAN_OR_EQUAL = "<="
    GREATER_THAN_OR_EQUAL = ">="
    NULL = None


class Modifier(IdsElement):
    """
    See the specification [here](https://developers.tetrascience.com/docs/ids-design-conventions-schemajson#modifier-pattern).
    """

    value: float
    modifier: ModifierType


class SchemaValidationError(ValueError):
    """Raised when a value is not consistent with the schema."""


class NotSemanticVersionError(SchemaValidationError):
    """Raised when a string does not conform to semantic versioning."""


class InstrumentStatus(IdsElement):
    """
    See the "instrument_status" field description [here](https://developers.tetrascience.com/docs/ids-design-conventions-schemajson#ids-fields).
    """

    name: str = IdsField(
        description=format_multiline_string(
            """
            Name of the status. If there is a general instrument status,
            you can use "general".
            """
        )
    )
    value: str


class Experiment(IdsElement):
    """
    See the "experiment" field description [here](https://developers.tetrascience.com/docs/ids-design-conventions-schemajson#ids-fields).
    """

    logs: List[str]
    instrument_status: List[InstrumentStatus]


class Run(IdsElement):
    """
    See the "runs" field description [here](https://developers.tetrascience.com/docs/ids-design-conventions-schemajson#ids-fields).
    A `Run` instance is one element in the `runs` array.
    """

    name: str
    experiment: Experiment


IdsSchemaVersion = TypeVar("IdsSchemaVersion", str, type(None))


class IdsSchema(IdsElement):
    """
    Top-level schema.
    """

    _version_regex: ClassVar[Pattern] = re.compile(r"^v\d{1,2}\.\d{1,2}\.\d{1,2}")
    #: '$id' and '$schema' are required fields in the IDS JSON schema. Their values are
    #:    the URL where the IDS is published and the JSON Schema version, respectively.
    #:    The former must be overridden in the child class but the latter should not.
    #:    for example:
    #:
    #:    .. code::
    #:
    #:        from typing import ClassVar, Dict, Union
    #:
    #:        from ts_ids_core.schema import IdsSchema
    #:
    #:        class MyIdsSchema(IdsSchema):
    #:            schema_extra_metadata: ClassVar[Dict[str, Union[str, int, float]]] = {
    #:                **IdsSchema.schema_extra_metadata,
    #:                "$id": "https://ids.tetrascience.com/common/instrument-a/v1.0.0/schema.json"
    #:            }
    #:
    #:    Note that the `ClassVar` type hint must be provided in order to indicate that
    #:    `schema_extra_metadata` is not an IDS Field.

    schema_extra_metadata: SchemaExtraMetadataType = {
        "$id": NotImplemented,
        "$schema": "http://json-schema.org/draft-07/schema#",
    }

    ids_type: Required[str] = IdsField(
        default=NotImplemented, alias="@idsType", const=True
    )
    ids_version: Required[str] = IdsField(
        default=NotImplemented, alias="@idsVersion", const=True
    )
    ids_convention_version: str = IdsField(
        alias="@idsConventionVersion",
        const=True,
        default="v1.0.0",
    )
    ids_namespace: Required[str] = IdsField(
        default=NotImplemented, alias="@idsNamespace", const=True
    )

    @validator("ids_version", "ids_convention_version")
    def is_valid_version_string(
        cls, value: IdsSchemaVersion, field: ModelField
    ) -> IdsSchemaVersion:
        """
        Assert that the passed-in value conforms to semantic versioning if the value
        is not `None`.

        :param value: The passed-in value to be validated.
        :param field: The field definition.
        :return:
            The passed-in value, unchanged.
        """
        if not field.required and value is None:
            return value
        if not cls._version_regex.search(value):
            raise NotSemanticVersionError(f"'{value}' is not a valid semantic version.")
        return value
