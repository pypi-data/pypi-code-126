import torchvision
from torch import nn, optim
from torch.nn import *
from torch.optim.lr_scheduler import StepLR
from torch.utils.data import DataLoader
import torch
from torch.utils.tensorboard import SummaryWriter
from Model import *
import matplotlib.pyplot as plt

#定义训练的设备使用cuda训练
device = torch.device("cuda")

#导入数据集，如果没有数据集则Download=True
Train_Data = torchvision.datasets.CIFAR10(root="dataset",train=True,transform=torchvision.transforms.ToTensor(),download=True)
Test_Data = torchvision.datasets.CIFAR10(root="testset",train=False,transform=torchvision.transforms.ToTensor(),download=False)

#查看数据集长度
Train_Data_size = len(Train_Data)
Test_Data_size = len(Test_Data)
print("训练数据集的长度：{}".format(Train_Data_size))
print("测试数据集的长度：{}".format(Test_Data_size))

#Dataloder加载数据集
DataLoader_Train = DataLoader(Train_Data,batch_size=64)
DataLoader_Test = DataLoader(Test_Data,batch_size=64)

#搭建卷积神经网络
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

#创建网络模型
Lzz_model_1 =lzz()
Lzz_model_1.to(device)

#损失函数 误差验证
loss_fn = nn.CrossEntropyLoss()
loss_fn.to(device)

#优化器
#1e-2 = 1 x (10)^(-2) = 0.04
learning_rate = 1e-2
optim  = torch.optim.SGD(Lzz_model_1.parameters(),lr = learning_rate) #设置优化器
#scheduler = StepLR(optim,step_size=300,gamma=0.1)#优化器自动调优，优化器自动调优主要面对训练轮数大

#记录训练次数
Train_epoch = 0
#记录测试的次数
Test_epoch = 0
#训练的轮数
epoch = 40
#添加Tensorboard
writer = SummaryWriter("P28")
for i in range(epoch):
    print("----------第{}轮训练开始:----------".format(i+1))
    #训练开始
    for data in DataLoader_Train:
        #梯度归零
        optim.zero_grad()
        #读取数据并放入网络
        imgs,targets = data
        imgs = imgs.to(device)
        targets= targets.to(device)
        outputs = Lzz_model_1(imgs)
        #损失函数计算误差
        loss = loss_fn(outputs,targets)
        #用上一步损失函数计算值进行反向传播
        loss.backward()
        #自动调参优化器优化模型
        #在此版本中，设置自动调优后还需要将初始调优放上，否则会出错
        optim.step()
        #scheduler.step()#自动调优
        #------------------------------------------------------------------
        Train_epoch = Train_epoch + 1

    #设置测试步骤的loss总和
    Test_loss_len = 0

    #整体测试率
    Total_accuracy = 0

    # 测试步骤 以下一行代码代表着没有梯度
    with torch.no_grad():
        for data in DataLoader_Test:
            imgs,targets = data
            imgs = imgs.to(device)
            targets = targets.to(device)
            outputs = Lzz_model_1(imgs)
            loss = loss_fn(outputs,targets)
            Test_loss_len = Test_loss_len + loss.item()
            #计算正确的个数
            accuracy = (outputs.argmax(1) == targets).sum()
            Total_accuracy = Total_accuracy + accuracy


    print("整体测试集上的Loss:{}".format(Test_loss_len))
    print("整体测试集上的正确率:{}".format(Total_accuracy/Test_Data_size))
    writer.add_scalar("Test_loss:",Test_loss_len,Test_epoch)
    writer.add_scalar("测试正确率",Total_accuracy/Test_Data_size,Test_epoch)
    Test_epoch = Train_epoch + 1

    # 每40轮测试保存一次参数
    if Train_epoch % 40 == 0:
        #定义模型名称
        torch.save(Lzz_model_1, "Lzz_asd{}".format(i + 1))
        print("模型以保存")
    #结尾保存当前模型
    # torch.save(Lzz_model_1,"Lzz_11{}".format(i+1))
    # print("模型以保存")

writer.close()