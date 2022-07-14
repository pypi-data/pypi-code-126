from mavtel_models.mavlink.base_metric_model import MAVLinkMetricBaseModel


class UnixEpochTime(MAVLinkMetricBaseModel):
    unix_epoch_time: int

    @classmethod
    def from_mavlink(cls, mavlink_object: int):
        return cls(unix_epoch_time=mavlink_object)

    def get_mavlink_data_class_name(self) -> str:
        return 'int'
