import torchvision
from torch import nn, optim
from torch.nn import *
from torch.optim.lr_scheduler import StepLR
from torch.utils.data import DataLoader
import torch

#搭建神经网络
class lzz(nn.Module):
    def __init__(self):
        super(lzz,self).__init__()
        self.model1 = Sequential(
            Conv2d(in_channels=3,out_channels=32,kernel_size=5,padding=2),
            MaxPool2d(2),
            Conv2d(in_channels=32,out_channels=32,kernel_size=5,padding=2),
            MaxPool2d(2),
            Conv2d(in_channels=32,out_channels=64,kernel_size=5,padding=2),
            MaxPool2d(2),
            Flatten(),
            Linear(64*4*4,64),
            Linear(64,10))
    def forward(self,x):
        x = self.model1(x)
        return x

if __name__ == '__main__':
    lzz = lzz()
    #input = torch.ones((64,3,32,32))
    #output = Lzz_model(input)
    #print(output.size)