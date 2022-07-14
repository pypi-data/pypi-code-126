from mavtel_models.mavlink.base_metric_model import MAVLinkMetricBaseModel


class InAir(MAVLinkMetricBaseModel):
    in_air: bool

    @classmethod
    def from_mavlink(cls, mavlink_object: int):
        return cls(in_air=mavlink_object)

    def get_mavlink_data_class_name(self) -> str:
        return 'bool'
