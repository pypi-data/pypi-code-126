from gooey import Gooey, GooeyParser
from .comFunction import  get_list
from .main_process import  main_process


@Gooey(
       target=None,
       program_name='Audio Test Lite v1.0',
       progress_regex=r"^progress: (?P<current>\d+)/(?P<total>\d+)$",
       progress_expr="current / total * 100",
       )

def register():
    firsrtkey,input_core,out_core = get_list()
    parser = GooeyParser()
    paltform = parser.add_argument_group('Params config page')
    paltform.add_argument('driverType',
                        metavar='driverType',
                        default=firsrtkey,
                        choices=[firsrtkey],
                        help='choose one of the driver types',
                          )
    paltform.add_argument('mosSwitch',
                        metavar='mosSwitch',
                        default='False',
                        choices=['True','False'],
                        help='MOS test takes another 10 seconds',
                          )
    paltform.add_argument('inPutDivice',
                        metavar='inPutDivice',
                        default=input_core[0],
                        choices=input_core,
                        help='choose one of the inPutDivices',
                          )
    paltform.add_argument('outPutDivice',
                        metavar='outPutDivice',
                        default=out_core[0],
                        choices=out_core,
                        help='choose one of the outPutDivices',
                          )
    paltform.add_argument('inputVolume',
                        metavar='inputVolume',
                        default= '100',
                        choices=['10','20','30','40','50','60','70','80','90','100'],
                        help='do not adjust volume unless necessary！',
                          )
    paltform.add_argument('outputVolume',
                        metavar='outputVolume',
                        default= '100',
                        choices=['10','20','30','40','50','60','70','80','90','100'],
                        help='do not adjust volume unless necessary！',
                          )
    args = parser.parse_args()
    mp = main_process(args)
    mp.run_all_process()







if __name__ == '__main__':
    register()

