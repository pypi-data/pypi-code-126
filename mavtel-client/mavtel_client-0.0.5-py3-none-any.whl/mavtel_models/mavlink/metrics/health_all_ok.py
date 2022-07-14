from mavtel_models.mavlink.base_metric_model import MAVLinkMetricBaseModel


class HealthAllOk(MAVLinkMetricBaseModel):
    health_all_ok: bool

    @classmethod
    def from_mavlink(cls, mavlink_object: bool):
        return cls(health_all_ok=mavlink_object)

    def get_mavlink_data_class_name(self) -> str:
        return 'bool'
