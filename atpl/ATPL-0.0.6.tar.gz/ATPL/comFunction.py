import os,time
import paramiko
from ctypes import Structure,POINTER,c_double,c_int,c_uint,CDLL,byref
import wave
import applescript
import socket,json
import shutil,copy
import sounddevice as sd
import numpy as np
import sys


def get_audio_devices_all_msg_dict():
    """
    :return: audio_devices_all_msg_dict
    """
    # 使用sounddevice 获取电脑连接的声卡以及系统自带的所有音频驱动信息(驱动, 声道名, id)
    audio_drivers_and_channels_msg_dict = {}
    audio_input_channels_msg_dict = {}
    audio_output_channels_msg_dict = {}
    this_tmp_dict = {}
    host_api_tuple = sd.query_hostapis()
    for temp_dict in host_api_tuple:
        this_tmp_dict[temp_dict["name"]] = temp_dict["devices"]

    channels_list = sd.query_devices()
    for driver_name in this_tmp_dict:
        audio_drivers_and_channels_msg_dict[driver_name] = []
        audio_input_channels_msg_dict[driver_name] = []
        audio_output_channels_msg_dict[driver_name] = []

        for id in this_tmp_dict[driver_name]:
            audio_drivers_and_channels_msg_dict[driver_name].append("("+str(id)+","+ str(channels_list[id]["name"])+")")

            if channels_list[id]["max_input_channels"] > 0:
                audio_input_channels_msg_dict[driver_name].append("("+str(id)+","+ str(channels_list[id]["name"])+")")

            if channels_list[id]["max_output_channels"] > 0:
                audio_output_channels_msg_dict[driver_name].append("("+str(id)+","+ str(channels_list[id]["name"])+")")

    return audio_drivers_and_channels_msg_dict, audio_input_channels_msg_dict, audio_output_channels_msg_dict

def get_list():
    """
    :return:
    """
    alldevices, indevices, outdevices = get_audio_devices_all_msg_dict()
    firsrtkey = list(alldevices.keys())[0]
    input_core = list(indevices[firsrtkey])
    out_core = list(outdevices[firsrtkey])
    return  firsrtkey,input_core,out_core

def play_and_rec(infile,outfile,devicetuple):
    """
    :param infile:
    :param outfile:
    :return:
    """
    sd.default.device = devicetuple
    datacur,framerate,nchannels = get_data_array(infile)
    dataout = sd.playrec(data=datacur,samplerate=framerate,channels=1,blocking=True,dtype=np.int16)
    make_out_file(outfile,dataout.astype(np.int16),framerate,1)


def match_sig(refFile=None,testFile=None,audioType=0):
    """
    Parameters
    ----------
    refFile
    testFile
    outFile
    audioType  0:speech,1:music

    Returns
    -------

    """

    refstruct, refsamplerate,reflen = get_data_of_ctypes_(refFile)
    teststruct, testsamplerate,testlen = get_data_of_ctypes_(testFile)
    outlen = max(reflen,testlen)

    outStruct = get_none_data_of_ctypes_(outlen)
    if refsamplerate != testsamplerate :
        raise TypeError('Different format of ref and test files!')

    mydll = CDLL(sys.prefix+ '/matchsig.dylib')

    mydll.matchsig_2.argtypes = [POINTER(emxArray_real_T), POINTER(emxArray_real_T), POINTER(emxArray_real_T),c_double,c_double,
                                     POINTER(c_double), POINTER(c_double)]
    delay, err = c_double(0.0), c_double(0.0)
    mydll.matchsig_2(byref(refstruct), byref(teststruct), byref(outStruct),c_double(refsamplerate),c_double(audioType),byref(delay), byref(err))
    if err.value > 0.0:
        return None
    else:
        return delay.value





def polqa_client_test(src,test,samplerate):
    """
    :param src:
    :param test:
    :param samplerate:
    :return:
    """
    curip = getip()
    curtime = log_time()
    curpath = str(curip) + '_'+str(curtime)
    os.mkdir(curpath)

    curdata = global_result.get_data()
    curdata['module'] = 'clientA'
    curdata['method'] = 'requestA'
    curdata['samplerate'] = samplerate
    curdata['token'] = curpath
    curdata['srcFile'] = os.path.basename(src)
    curdata['testFile'] = os.path.basename(test)

    #ssh
    shutil.copy(src,curpath)
    shutil.copy(test, curpath)

    dstpath = '/home/netease/polqa'


    # stfp
    client,sftp = sftp_connect(global_result.username,global_result.password,global_result.HOST,port=global_result.sftpPort)
    sftp_put(sftp,curpath, dstpath)
    sftp_disconnect(client)

    shutil.rmtree(curpath)
    # get result
    socket = SocketClient(global_result.machost,global_result.PORT)
    try:
        result = socket.sender(curdata)
        print(result['result'])
    except:
        socket.close()
        return None
    return  result['result']




def str_2_bool(str):
    """
    :param str:
    :return:
    """
    if str == 'True':
        return True
    else:
        return False

class SocketClient:
    def __init__(self, ip: str, port: int):
        """
        :param ip:
        :param port:
        """
        time.sleep(2)
        self.s = socket.socket()
        self.s.connect((ip, port))
        self.recv_data = b''

    def sender(self, data: dict) -> json:
        """
        :param data:
        :return:
        """
        data = json.dumps(data)
        self.s.send(bytes(data.encode("utf-8")))
        return json.loads(str(self.s.recv(1024), encoding="utf-8"))


    def close(self):
        """
        :return:
        """
        self.s.close()


def set_mac_volume(outputVolume,inputVolume):
    """
    :param outputVolume:
    :param inputVolume:
    :return:
    """
    applescript.run("set volume output volume {}".format(outputVolume))# 设置音量为50
    applescript.run("set volume input volume {}".format(inputVolume))# 设置音量为10

def recovery_mac_volume():
    """
    :return:
    """
    applescript.run('set volume output volume 80')# 设置音量为80
    applescript.run('set volume input volume 50')# 设置音量为50

def half_wave_file(wavfile, type, delay):
    """
    :return:
    """
    newFileName = wavfile[:-4] + str(type) + '_aligned_.wav'
    data, fs, _ = get_data_array(wavfile)
    wavefile = wave.open(newFileName, 'wb')  # open for writing
    # 读取wav文件的四种信息的函数。期中numframes表示一共读取了几个frames，在后面要用到滴。
    if type == 0:
        data = data[int(delay + 100):]
    if type == 1:
        data = data[:-int(delay + 100)]
    wavefile.setnchannels(1)
    wavefile.setsampwidth(2)
    wavefile.setframerate(fs)
    wavefile.writeframes(data)
    wavefile.close()
    return newFileName


class emxArray_real_T(Structure):
 _fields_ = [
          ("pdata", POINTER(c_double)),  # c_byte
          ("psize", POINTER(c_int)),  # c_byte
          ("allocSize", c_int),  #  c_byte
          ("NumDimensions", c_int),  # c_byte
          ("canFreeData", c_uint),
]



def get_data_array(filename):
    """
    :param filename:
    :return:
    """
    f = wave.open(filename, "rb")
    # 读取格式信息
    # 一次性返回所有的WAV文件的格式信息，它返回的是一个组元(tuple)：声道数, 量化位数（byte单位）, 采样频率, 采样点数, 压缩类型, 压缩类型的描述。wave模块只支持非压缩的数据，因此可以忽略最后两个信息
    params = f.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    # 读取波形数据
    # 读取声音数据，传递一个参数指定需要读取的长度（以取样点为单位）
    str_data = f.readframes(nframes)
    f.close()
    return np.frombuffer(str_data, dtype=np.int16),framerate,nchannels

def get_data_of_ctypes_(inWaveFile=None,int2float=False):
    """
    :param inWaveFile:
    :param int2float:
    :return:
    """
    wavf = wave.open(inWaveFile, 'rb')
    refChannel,refsamWidth,refsamplerate,refframeCount = wavf.getnchannels(),wavf.getsampwidth(),wavf.getframerate(),wavf.getnframes()

    if (refChannel,refsamWidth) != (1,2):
        raise TypeError('Different format of ref and test files!')
    pcmdata = wavf.readframes(refframeCount)

    ref = np.frombuffer(pcmdata,dtype=np.int16)

    ref = ref.astype(np.float64)
    if int2float:
        ref = ref/32768
    datastruct = emxArray_real_T()
    datastruct.pdata = (c_double * refframeCount)(*ref)
    datastruct.psize = (c_int * 1)(*[refframeCount])
    wavf.close()
    return  datastruct,refsamplerate,refframeCount

def get_none_data_of_ctypes_(dataLength=0):
    """
    :param dataLength:
    :return:
    """
    data =  np.array([0.0 for _ in range(dataLength)])
    data = data.astype(np.float64)

    outStruct = emxArray_real_T()
    #outStruct = create_string_buffer(20)
    outStruct.pdata =  (c_double * dataLength)(*data)
    outStruct.psize = (c_int * 1)(*[dataLength])
    outStruct.allocSize = dataLength
    outStruct.NumDimensions = 1
    outStruct.canFreeData = 1
    return outStruct

constMosResult = {'delay':'No Result','mos':'-0.0','Speech Level Gain':'','Noise Level Gain':''}

class commondata():
    def __init__(self):
        self.mosResult = copy.deepcopy(constMosResult)
        self.HOST = '10.219.33.45'
        self.machost = '10.219.33.45' #'10.242.167.159'
        self.username = 'netease'
        self.password = 'Netease163'
        self.PORT = 2159
        self.sftpPort = 22
    @staticmethod
    def get_data():
        return {"type": "command",
        "module": "clientA",
        "method": "requestA",
        "samplerate":16000,
        "token": "",
        "job":None,
        "srcFile":'',
        "testFile":'',
        "result":{},
        "err":"No error"}

global_result = commondata()

def log_time():
    """
    :return:
    """
    time_tup = time.localtime(time.time())
    # format_time = '%Y-%m-%d_%a_%H-%M-%S'
    format_time = '%Y-%m-%d-%H-%M-%S'

    cur_time = time.strftime(format_time, time_tup)
    return cur_time

def getip():
    """
    :return:
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        vqtip = s.getsockname()[0]
    finally:
        s.close()
    return vqtip






def sftp_connect(username,password,host,port=22):
    """
    :param username:
    :param password:
    :param host:
    :param port:
    :return:
    """
    client = None
    sftp = None
    try:
        client = paramiko.Transport((host,port))
    except Exception as error:
        print(error)
    else:
        try:
            client.connect(username=username, password=password)
        except Exception as error:
            print(error)
        else:
            sftp = paramiko.SFTPClient.from_transport(client)
    return client,sftp


def sftp_disconnect(client):
    """
    :param client:
    :return:
    """
    try:
        client.close()
    except Exception as error:
        print(error)








def sftp_put(sftp, local, remote):
    # 检查路径是否存在
    def _is_exists(path, function):
        path = path.replace('\\', '/')
        try:
            function(path)
        except Exception as error:
            return False
        else:
            return True

    # 拷贝文件
    def _copy(sftp, local, remote):
        # 判断remote是否是目录
        if _is_exists(remote, function=sftp.chdir):
            # 是，获取local路径中的最后一个文件名拼接到remote中
            filename = os.path.basename(os.path.normpath(local))
            remote = os.path.join(remote, filename).replace('\\', '/')
        # 如果local为目录
        if os.path.isdir(local):
            # 在远程创建相应的目录
            _is_exists(remote, function=sftp.mkdir)
            # 遍历local
            for file in os.listdir(local):
                # 取得file的全路径
                localfile = os.path.join(local, file).replace('\\', '/')
                # 深度递归_copy()
                _copy(sftp=sftp, local=localfile, remote=remote)
        # 如果local为文件
        if os.path.isfile(local):
            try:
                sftp.put(local, remote)
            except Exception as error:
                print(error)
                print('[put]', local, '==>', remote, 'FAILED')
            else:
                pass
                #print('[put]', local, '==>', remote, 'SUCCESSED')

    # 检查local
    if not _is_exists(local, function=os.stat):
        print("'" + local + "': No such file or directory in local")
        return False
    # 检查remote的父目录
    remote_parent = os.path.dirname(os.path.normpath(remote))
    if not _is_exists(remote_parent, function=sftp.chdir):
        print("'" + remote + "': No such file or directory in remote")
        return False
    # 拷贝文件
    _copy(sftp=sftp, local=local, remote=remote)




def make_out_file(tarFile,data,fs,channel):
    """

    """
    outData = data.astype(np.int16)
    wavfile = wave.open(tarFile, 'wb')
    wavfile.setnchannels(channel)
    wavfile.setsampwidth(2)
    wavfile.setframerate(fs)
    wavfile.writeframes(outData.tobytes())
    wavfile.close()



if __name__ == '__main__':
    str = \
"""tell application "System Events"
     tell window "iTunes" of process "iTunes"
        set chbtn to first UI element whose help is "Choose which speakers to use."
        tell chbtn
            click
            -- tell menu 1 to get every menu item
        end tell
     end tell
end tell"""
    err = applescript.run(str)# 设置音量为50
    print(err.err)
    pass


