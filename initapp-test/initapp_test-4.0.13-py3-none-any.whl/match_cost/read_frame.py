import ffmpeg._ffmpeg as ffmpeg
import ffmpeg._probe as ffprobe
from ffmpeg._run import Error
import numpy
import cv2
import os,sys
import match_cost.match_conf as match_conf
from constants import YUNCE_TEST

import json
import subprocess
from ffmpeg._run import Error
from ffmpeg._utils import convert_kwargs_to_cmd_line_args

def read_frame_by_time(in_file, time):
    """
    指定时间节点读取任意帧
    """
    if match_conf.test_platform == YUNCE_TEST and match_conf.type == 'android':
        parmas = {
            'ss': time,
            'vframes':1,
            'f':'image2',
            'vcodec':'mjpeg'
        }
        return __peg_cmd(in_file, **parmas)
    else:
        out, err = (
            ffmpeg.input(in_file, ss=time)
                  .output('pipe:', vframes=1, format='image2', vcodec='mjpeg')
                  .run(capture_stdout=True)
        )
        return out

def scale_video(in_file, out_file):
    if match_conf.test_platform == YUNCE_TEST and match_conf.type == 'android':
        return __peg_cmd(in_file, out_file)
    else:
        try:
            out, err = (
                ffmpeg.input(in_file)
                    .output(out_file)
                    .run(capture_stdout=True)
            )
            return out, err
        except Error as e:
            print("output")
            print(e.stdout)
            print("err")
            print(e.stderr)


def read_frame_by_time1(in_file, time, out_file):
    """
    指定时间节点读取任意帧
    """
    if match_conf.test_platform == YUNCE_TEST and match_conf.type == 'android':
        params = {
            'ss':time,
            'vframes':1,
            'f':'image2',
            'vcodec':'mjpeg'
        }
        return __peg_cmd(in_file, out_file, **params)
    else:
        out, err = (
            ffmpeg.input(in_file, ss=time)
                .output(out_file, vframes='1', f='image2', vcodec='mjpeg')
                .run(capture_stdout=True)
        )
        return out, err


def get_video_info(in_file):
    """
    获取视频基本信息
    """
    try:
        probe = __probe(in_file)
        video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
        if video_stream is None:
            print('No video stream found', file=sys.stderr)
            sys.exit(1)
        return video_stream
    except ffprobe.Error as err:
        print(str(err.stderr, encoding='utf8'))
        sys.exit(1)


def __get_env():
    env = os.environ.copy()
    if match_conf.type == 'android' and env.get('LD_LIBRARY_PATH'):
        del env['LD_LIBRARY_PATH']
    return env


def __probe(filename, cmd='ffprobe', **kwargs):
    """Run ffprobe on the specified file and return a JSON representation of the output.

    Raises:
        :class:`ffmpeg.Error`: if ffprobe returns a non-zero exit code,
            an :class:`Error` is returned with a generic error message.
            The stderr output can be retrieved by accessing the
            ``stderr`` property of the exception.
    """
    args = [cmd, '-show_format', '-show_streams', '-of', 'json']
    args += convert_kwargs_to_cmd_line_args(kwargs)
    args += [filename]

    env1 = __get_env()

    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env1)
    out, err = p.communicate()
    if p.returncode != 0:
        raise Error('ffprobe', out, err)
    return json.loads(out.decode('utf-8'))

def __peg_cmd(input, output, **kwargs):
    """Run ffprobe on the specified file and return a JSON representation of the output.

    Raises:
        :class:`ffmpeg.Error`: if ffprobe returns a non-zero exit code,
            an :class:`Error` is returned with a generic error message.
            The stderr output can be retrieved by accessing the
            ``stderr`` property of the exception.
    """
    cmd='ffmpeg'
    args = [cmd, '-i', input, '-y']
    args += convert_kwargs_to_cmd_line_args(kwargs)
    args.append(output)

    env1 = __get_env()

    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env1)
    out, err = p.communicate()
    if p.returncode != 0:
        raise Error('ffprobe', out, err)
    return out, err

if __name__ == '__main__':
    file_path = "555.mp4"
    video_info = get_video_info(file_path)
    total_duration = video_info['duration']
    float_time = float(total_duration)
    print('总时间：' + total_duration + 's')
    cut_couts = int(float_time * 10)
    time_offset = 0
    for index in range(cut_couts):
        time_offset += float(total_duration)/10
    # random_time = random.randint(1, int(float(total_duration)) - 1) + random.random()
    # print('随机时间：' + str(random_time) + 's')
        out = read_frame_by_time(file_path, time_offset)
        image_array = numpy.asarray(bytearray(out), dtype="uint8")
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    #cv2.imshow('frame', image)
    #cv2.waitKey()
        cv2.imwrite("{}.jpg".format(str(index)), image)
