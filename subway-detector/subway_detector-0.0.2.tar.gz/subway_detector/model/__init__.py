from model.net import *

__all__=['ResNet','resnet34', 'resnet50', 'resnet101', 'resnet152']

def build_model(model_arch,kwargs):
    return globals()[model_arch](**kwargs)