LugwitPath=r'Z:\plug_in\Lugwit_plug'
plug_inPath=r'Z:\plug_in'
import sys
print (sys.version[0]+sys.version[2])
sys.path.append(plug_inPath+'/Python/Python{}/Lib/site-packages'.format(sys.version[0]+sys.version[2]))
sys.path.append(LugwitPath+r'\Python\PythonLib')