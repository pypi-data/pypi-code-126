from datetime import datetime, timedelta
from typing import Optional

import prefect
from prefect.engine.signals import VALIDATIONFAIL

dt_fmt = "%Y-%m-%d"


class DefineTargetDate(prefect.Task):
    def __init__(
        self,
        timedelta_from_today: Optional[timedelta] = timedelta(days=-1),
        allow_today: Optional[bool] = False,
        allow_future_dates: bool = False,
        **kwargs,
    ):
        # self.target_datetime = target_datetime
        self.timedelta_from_today = timedelta_from_today
        self.allow_today = allow_today
        self.allow_future_dates = allow_future_dates
        super().__init__(**kwargs)

    def run(self, target_datetime: Optional[datetime] = None):
        if target_datetime:
            target_date = target_datetime.date()
            self.logger.info(
                f"target date provided as a parameter: "
                f"{target_date.strftime(dt_fmt)}"
            )
            today_date = prefect.context.date.date()
            if not self.allow_future_dates and target_date > today_date:
                raise VALIDATIONFAIL(
                    f"provided target date={target_date} needs to be <=today"
                )
            if not self.allow_today and target_date == today_date:
                raise VALIDATIONFAIL(
                    f"provided target date={target_date} needs to be <=yesterday"
                )
            return target_date

        self.logger.info(
            "target date not provided as a parameter -> "
            "determining from `scheduled_start_time`"
        )
        scheduled_date = prefect.context.scheduled_start_time
        # running flow for the previous complete day
        set_date = (scheduled_date + self.timedelta_from_today).date()
        self.logger.info(
            f"scheduled date={scheduled_date.strftime(dt_fmt)} -> "
            f"target date={set_date.strftime(dt_fmt)}"
        )

        return set_date


class DefineTargetDatetime(prefect.Task):
    def __init__(
        self,
        timedelta_from_today: Optional[timedelta] = timedelta(days=-1),
        allow_today: Optional[bool] = False,
        allow_future_dates: bool = False,
        **kwargs,
    ):
        # self.target_datetime = target_datetime
        self.timedelta_from_today = timedelta_from_today
        self.allow_today = allow_today
        self.allow_future_dates = allow_future_dates
        super().__init__(**kwargs)

    def run(self, target_datetime: Optional[datetime] = None):
        if target_datetime:
            self.logger.info(
                f"target date provided as a parameter: "
                f"{target_datetime.strftime(datetime_fmt)}"
            )
            today_date = prefect.context.date.date()
            if not self.allow_future_dates and target_datetime.date() > today_date:
                raise VALIDATIONFAIL(
                    f"provided target date={target_datetime} needs to be <=today"
                )
            if not self.allow_today and target_datetime.date() == today_date:
                raise VALIDATIONFAIL(
                    f"provided target date={target_datetime} needs to be <=yesterday"
                )
            return target_datetime

        self.logger.info(
            "target_datetime not provided as a parameter -> "
            "determining from `scheduled_start_time`"
        )
        scheduled_datetime = prefect.context.scheduled_start_time
        # running flow for the previous complete day
        scheduled_datetime_midnight = datetime(scheduled_datetime.year,
                                               scheduled_datetime.month,
                                               scheduled_datetime.day)
        set_datetime = scheduled_datetime_midnight + self.timedelta_from_today
        self.logger.info(
            f"scheduled date={scheduled_datetime_midnight.strftime(datetime_fmt)} -> "
            f"target date={set_datetime.strftime(datetime_fmt)}"
        )

        return set_datetime
