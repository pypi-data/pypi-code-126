from mavtel_models.mavlink.base_metric_model import MAVLinkMetricBaseModel


class Heading(MAVLinkMetricBaseModel):
    heading_deg: float

    def get_mavlink_data_class_name(self) -> str:
        return 'mavsdk.telemetry.Heading'
