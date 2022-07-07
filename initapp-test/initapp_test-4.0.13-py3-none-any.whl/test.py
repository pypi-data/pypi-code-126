import match_cost.get_start_time as get_start_time
from match_cost.match_conf import update_config_value
import constants
import os
import json
import match_cost.read_frame as read
if __name__ == '__main__':
    update_config_value('pkg_name', value=constants.KWAI_PACKAGENAME)
    update_config_value('test_platform', value=constants.YUNCE_TEST)
    startTime = get_start_time.StartTime(30)
    startTime.vediopath = './pro7.mp4'
    results = []
    result = startTime.getStartTime()
    # print(1)
    # a = {'a':'adf'}
