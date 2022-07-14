from enum import Enum


class TaskType(Enum):
    INSPECTION_ML = 'IN_ML'
    INSPECTION_IMAGE = 'IN_IMG'
    INSPECTION_NER = 'IN_NER'
    INSPECTION_CLASSIFY = 'IN_CLS'
    TEST = 'TEST'


class TaskConfigs(Enum):
    INSPECTION_ML = './config/ib.yml'
    INSPECTION_IMAGE = './config/ia.yml'
    INSPECTION_NER = './config/test.yml'
    INSPECTION_CLASSIFY = './config/test.yml'
    TEST = './config/test.yml'
