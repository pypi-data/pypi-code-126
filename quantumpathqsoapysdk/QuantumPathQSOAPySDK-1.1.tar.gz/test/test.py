import sys
sys.path.append('C:\PROYECTOSAQ\QPATHPySDK\src')

from QuantumPathQSOAPySDK import QSOAPlatform

qsoa = QSOAPlatform(configFile=True)

solutionList = qsoa.getQuantumSolutionList()

activeEnvironment = qsoa.setActiveEnvironment('lab')

print('Solution List:', solutionList)