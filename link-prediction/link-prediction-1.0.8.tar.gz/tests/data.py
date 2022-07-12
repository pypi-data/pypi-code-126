"""Reusable variables containing test data."""

from link_prediction.datasets.rico import RicoDataPoint


rico_data_point: RicoDataPoint = RicoDataPoint(
    source=RicoDataPoint.RawSourceData(id=795, element_id="2e18ce7"),
    target=RicoDataPoint.RicoScreen(
        id=887,
    ),
    application_name="com.vzw.indycar",
    trace_id=0,
    data_type="link",
)
