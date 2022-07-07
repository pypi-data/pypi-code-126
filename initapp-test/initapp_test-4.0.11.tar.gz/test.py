# import match_cost.get_start_time as get_start_time
# from match_cost.match_conf import update_config_value
# import constants
import os
import json
if __name__ == '__main__':
    # update_config_value('pkg_name', value=constants.KWAI_PACKAGENAME)
    # startTime = get_start_time.StartTime(30)
    # startTime.vediopath = './pro7.mp4'
    # results = []
    # result = startTime.getStartTime()
    # print(1)
    a = {'a':'adf'}
    del a['b']
    print(a)
    t = os.popen("ffprobe -v quiet -of json -i ./pro7.mp4 -show_streams")
    # infos = json.loads(t.read())
    # video_stream = next((stream for stream in infos['streams'] if stream['codec_type'] == 'video'), None)
    # print(video_stream)