LugwitPath=r'Z:\plug_in\Lugwit_plug'
LugwitPath_ip=r'\\172.21.1.79\z\plug_in\Lugwit_plug'
plug_inPath=r'Z:\plug_in'
plug_inPath_ip=r'\\172.21.1.79\z\plug_in'
import sys
print (sys.version[0]+sys.version[2])

sys.path.append(r'\\172.21.1.2\P4Triggers\DeadLinePy3')

sys.path.append(plug_inPath+'/Python/Python{}/Lib/site-packages'.format(sys.version[0]+sys.version[2]))
sys.path.append(LugwitPath+r'\Python\PythonLib')