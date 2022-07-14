from mavtel_models.mavlink.base_metric_model import MAVLinkMetricBaseModel


class Armed(MAVLinkMetricBaseModel):
    armed: bool

    @classmethod
    def from_mavlink(cls, mavlink_object: bool):
        return cls(armed=mavlink_object)

    def get_mavlink_data_class_name(self) -> str:
        return 'bool'
