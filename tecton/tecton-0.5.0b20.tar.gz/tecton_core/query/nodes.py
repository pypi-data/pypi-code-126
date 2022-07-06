from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple

import pendulum

from tecton_core.feature_definition_wrapper import FeatureDefinitionWrapper
from tecton_core.pipeline_common import get_time_window_from_data_source_node
from tecton_core.query.node_interface import NodeRef
from tecton_core.query.node_interface import QueryNode
from tecton_proto.args.pipeline_pb2 import DataSourceNode
from tecton_proto.args.pipeline_pb2 import Pipeline
from tecton_proto.data.feature_view_pb2 import MaterializationTimeRangePolicy
from tecton_proto.data.virtual_data_source_pb2 import VirtualDataSource


class FeatureViewPipelineNode(QueryNode):
    def __init__(
        self,
        pipeline: Pipeline,
        inputs_map: Dict[str, NodeRef],
        feature_definition_wrapper: FeatureDefinitionWrapper,
        feature_time_limits: Optional[pendulum.Period],
    ):
        self.pipeline = pipeline
        self.feature_definition_wrapper = feature_definition_wrapper
        self.inputs_map = inputs_map
        # Needed for correct behavior by tecton_sliding_window udf if it exists in the pipeline
        self.feature_time_limits = feature_time_limits
        # Note: elsewhere we set this to pendulum.Duration(seconds=fv_proto.materialization_params.schedule_interval.ToSeconds())
        # but that seemed wrong for bwafv
        self.schedule_interval = feature_definition_wrapper.batch_materialization_schedule

    @property
    def inputs(self) -> Tuple[NodeRef]:
        return tuple(self.inputs_map.values())

    def as_str(self, verbose: bool):
        return f"Evaluate Pipeline: {self.feature_definition_wrapper.name}\n"

    # overwrite pretty_print because we have named inputs
    def pretty_print(self, verbose: bool = False, indents=0) -> str:
        s = "  " * indents + self.as_str(verbose)
        for k in self.inputs_map:
            s += "  " * (indents) + f"- PipelineInput: {k}\n"
            s += self.inputs_map[k].pretty_print(verbose, indents + 1)
        return s


class DataSourceScanNode(QueryNode):
    """
    DataSource + Filter
    We don't have a separate filter node to hide away the filter/partition interaction with raw_batch_translator
    """

    def __init__(
        self, ds: VirtualDataSource, ds_node: DataSourceNode, raw_data_time_filter: Optional[pendulum.Period] = None
    ):
        self.ds = ds
        self.ds_node = ds_node
        self.time_filter = raw_data_time_filter

    @property
    def inputs(self) -> Tuple[NodeRef]:
        return tuple()

    def with_feature_time_filter(
        self, feature_time_range: pendulum.Period, schedule_interval: Optional[pendulum.Period]
    ) -> QueryNode:
        """Returns a new node with raw data time filter computed based on the passed-in feature data time filter."""
        time_filter = get_time_window_from_data_source_node(feature_time_range, schedule_interval, self.ds_node)
        return DataSourceScanNode(self.ds, self.ds_node, time_filter)

    def as_str(self, verbose: bool):
        s = ""
        if self.time_filter is not None:
            s += f"TimeFilter: {self.time_filter}\n"
        s += f"Scan DataSource: {self.ds.fco_metadata.name}\n"
        return s


class OfflineStoreScanNode(QueryNode):
    """
    Fetch values from offline store
    """

    def __init__(self, feature_definition_wrapper: FeatureDefinitionWrapper):
        self.feature_definition_wrapper = feature_definition_wrapper

    def as_str(self, verbose: bool):
        return f"Scan OfflineStore: {self.feature_definition_wrapper.name}"

    @property
    def inputs(self) -> Tuple[NodeRef]:
        return tuple()


class JoinNode(QueryNode):
    """
    A basic left join on 2 inputs
    """

    def __init__(self, left: NodeRef, right: NodeRef, join_cols: List[str], how: str):
        self.left = left
        self.right = right
        self.join_cols = join_cols
        self.how = how

    @property
    def inputs(self) -> Tuple[NodeRef]:
        return (self.left, self.right)

    def as_str(self, verbose: bool):
        # TODO: this is gonna look ugly
        return f"{self.how} Join" + (f" on {self.join_cols}:" if verbose else ":")


class AsofJoinNode(QueryNode):
    """
    A "basic" asof join on 2 inputs
    """

    def __init__(self, left: NodeRef, right: NodeRef, join_cols: List[str], timestamp_field: str, right_prefix: str):
        self.left = left
        self.right = right
        self.join_cols = join_cols
        self.timestamp_field = timestamp_field
        self.right_prefix = right_prefix

    @property
    def inputs(self) -> Tuple[NodeRef]:
        return (self.left, self.right)

    def as_str(self, verbose: bool):
        # TODO: this is gonna look ugly
        return "Asof Join:"


class FullAggNode(QueryNode):
    """
    Performs full aggregations for each of the aggregates in fdw.trailing_time_window_aggregation.
    The full aggregations are applied for all the join keys in spine; otherwise new aggregations changed via
    expiring windows will not be generated.

    The resulting dataframe with contain all join keys in the spine.
    """

    def __init__(
        self, input_node: NodeRef, fdw: FeatureDefinitionWrapper, spine: Optional[Any], spine_time_field: Optional[str]
    ):
        self.input_node = input_node
        self.fdw = fdw
        self.spine = spine
        self.spine_time_field = spine_time_field

    @property
    def inputs(self) -> Tuple[NodeRef]:
        return (self.input_node,)

    def as_str(self, verbose: bool):
        if verbose:
            return (
                "FullAggNode: Set any feature values for rows with time < feature_start_time to null\n"
                + "Use window function to perform full aggregations; window range = agg.time_range range preceding -> current row\n"
                + "right-join against spine, with _anchor_time = aligned_spine_timestamp - 1 window, because raw data in a given time will only be accessible for retrieval by the end of the window. We also do some stuff to account for upstream_lateness, but we don't do anything to account for differences in slide_window and batch_schedule. And also this kind of assumes materialization happens instantaneously."
                if self.spine
                else ""
            )
        else:
            return "Perform Full Aggregates"


class PartialAggNode(QueryNode):
    """
    Performs partial aggregations for each of the aggregates in fdw.trailing_time_window_aggregation
    """

    def __init__(self, input_node: NodeRef, fdw: FeatureDefinitionWrapper):
        self.input_node = input_node
        self.fdw = fdw

    @property
    def inputs(self) -> Tuple[NodeRef]:
        return (self.input_node,)

    def as_str(self, verbose: bool):
        if verbose:
            return (
                'Add column "_anchor_time" as the start of aggregation window\n'
                + "Perform partial-aggregate group by aggregation window\n"
                + "Align timestamp_key to aggregation_slide_period to create aggregation window"
            )
        else:
            return "Perform Partial Aggregates"


class SetAnchorTimeNode(QueryNode):
    """
    Augment a dataframe with an anchor time based on batch schedule (BFV) or slide window (WAFV)
    """

    def __init__(
        self,
        input_node: NodeRef,
        offline: bool,
        feature_store_format_version: int,
        batch_schedule_in_feature_store_specific_version_units: int,
        timestamp_field: str,
        retrieval: bool,
    ):
        self.input_node = input_node
        self.offline = offline
        self.feature_store_format_version = feature_store_format_version
        self.batch_schedule_in_feature_store_specific_version_units = (
            batch_schedule_in_feature_store_specific_version_units
        )
        self.timestamp_field = timestamp_field
        self.for_retrieval = retrieval

    @property
    def inputs(self) -> Tuple[NodeRef]:
        return (self.input_node,)

    def as_str(self, verbose: bool):
        if not verbose:
            return ""
        if self.for_retrieval:
            return "Add anchor time column _anchor_time: timestamp_col-timestamp_col%batch_schedule - batch_schedule, because if you're querying at t, you would only see the data for the previous window"
        elif self.offline:
            return "Add anchor time column _anchor_time: timestamp_col-timestamp_col%batch_schedule"
        else:
            return "Add raw data end time column _materialized_raw_data_end_time: timestamp_col-timestamp_col%batch_schedule + batch_schedule. We assume feature_end_time==raw_data_end_time"


class RenameColsNode(QueryNode):
    """
    Rename some columns. Maybe you want to join on the columns.
    """

    def __init__(self, input_node: NodeRef, mapping: Dict[str, str]):
        self.input_node = input_node
        self.mapping = mapping

    @property
    def inputs(self) -> Tuple[NodeRef]:
        return (self.input_node,)

    def as_str(self, verbose: bool):
        return f"Rename {self.mapping}"


class DataNode(QueryNode):
    """
    Currently used for testing, but could be used for run_api(mock_inputs). The executor node will need to typecheck and know how to handle the type of mock data.
    """

    data: Any

    def __init__(self, data: Any):
        self.data = data

    @property
    def inputs(self) -> Tuple[NodeRef]:
        return tuple()

    def as_str(self, verbose: bool):
        if verbose:
            return f"Mock Data: type:{self.data.__class__}"
        else:
            return "Mock Data"


class RespectFSTNode(QueryNode):
    """
    Null out all features outside of feature start time
    """

    def __init__(
        self,
        input_node: NodeRef,
        retrieval_time_col: str,
        feature_start_time: pendulum.datetime,
        features: List[str],
    ):
        self.input_node = input_node
        self.retrieval_time_col = retrieval_time_col
        self.feature_start_time = feature_start_time
        self.features = features

    @property
    def inputs(self) -> Tuple[NodeRef]:
        return (self.input_node,)

    def as_str(self, verbose: bool):
        return f"Null out any values based on a FeatureStartTime of {self.feature_start_time}"


class RespectTTLNode(QueryNode):
    """
    Null out all features outside of ttl
    """

    def __init__(
        self,
        input_node: NodeRef,
        retrieval_time_col: str,
        source_time_col: str,
        ttl: pendulum.Period,
        features: List[str],
    ):
        self.input_node = input_node
        self.retrieval_time_col = retrieval_time_col
        self.source_time_col = source_time_col
        self.ttl = ttl
        self.features = features

    @property
    def inputs(self) -> Tuple[NodeRef]:
        return (self.input_node,)

    def as_str(self, verbose: bool):
        return f"Null out any values based on a TTL of {self.ttl}"


class FeatureTimeFilterNode(QueryNode):
    """
    Ensure the data being written by a materialization job to offline/online store only contains
    feature timestamps in the feature_data_time_limits range.
    """

    def __init__(
        self,
        input_node: NodeRef,
        feature_data_time_limits: pendulum.Period,
        policy: MaterializationTimeRangePolicy,
        timestamp_field: str,
    ):
        self.input_node = input_node
        self.time_filter = feature_data_time_limits
        self.policy = policy
        self.timestamp_field = timestamp_field

    @property
    def inputs(self) -> Tuple[NodeRef]:
        return (self.input_node,)

    def as_str(self, verbose: bool):
        if self.policy == MaterializationTimeRangePolicy.MATERIALIZATION_TIME_RANGE_POLICY_FAIL_IF_OUT_OF_RANGE:
            policy_str = "Assert time in range:"
        else:
            policy_str = "Apply:"
        return f"{policy_str} TimeFilter: {self.time_filter}"
