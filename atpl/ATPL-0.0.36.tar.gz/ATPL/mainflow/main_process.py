#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

from .comFunction import half_wave_file,set_mac_volume,recovery_mac_volume,str_2_bool,polqa_client_test,match_sig,play_and_rec
import os

class main_process():
    def __init__(self,UIsysConfig):
        """
        :param UIsysConfig:
        """
        self.__init_global_variable(UIsysConfig)
        pass

    def __init_global_variable(self,sysConfig):
        """
        testPaltform ：测试的Demo或者app
        version ： 版本信息
        最终根据这两个变量生成相应名称的报告和过程数据,不能用中文
        """
        self.inputFile = sys.prefix + '/speech.wav'
        self.outFile = sys.prefix + '/out.wav'
        self.inputDeviceId = self.__parse_id_from_str(sysConfig.inPutDivice)
        self.outputDeviceId = self.__parse_id_from_str(sysConfig.outPutDivice)
        self.mosSwitch = str_2_bool(sysConfig.mosSwitch)
        self.inVolume = sysConfig.inputVolume
        self.outVolume = sysConfig.outputVolume
        print("********************************************************************")
        print('当前选择的声卡输入为:{}'.format(sysConfig.inPutDivice))
        print('当前选择的声卡输出为:{}'.format(sysConfig.outPutDivice))

    def __parse_id_from_str(self,sdSTR):
        """
        :return:
        """
        return int(sdSTR.split(",")[0].split('(')[1])
    def run_all_process(self):
        """
        :return:
        """
        print('progress: {0}/100'.format(0))
        print("********************************************************************")
        print("开始测试")
        print("设置声卡音量")
        set_mac_volume(self.outVolume,self.inVolume)
        print('progress: {0}/100'.format(5))
        print('Done!')
        print("录制音频文件")
        play_and_rec(self.inputFile, self.outFile,[self.inputDeviceId,self.outputDeviceId])
        print('Done!')
        print('progress: {0}/100'.format(35))
        recovery_mac_volume()
        print("计算延时")
        MATCH = match_sig(self.inputFile,self.outFile)
        if MATCH is not None:
            print('当前的端到端延时:{}ms'.format(round(MATCH/48000 * 1000),2))
        else:
            print('端到端延时测试失败！')
            MATCH=0
        print('Done!')
        print('progress: {0}/100'.format(50))
        if self.mosSwitch:
            print("计算MOS分")
            ref = half_wave_file(self.inputFile,0,MATCH)
            test  = half_wave_file(self.outFile,1,MATCH)
            polqa_client_test(ref, test,48000)
            print('Done!')
            os.remove(ref)
            os.remove(test)
        print('progress: {0}/100'.format(100))
        #os.remove(self.outFile)



if __name__ == '__main__':
    pass