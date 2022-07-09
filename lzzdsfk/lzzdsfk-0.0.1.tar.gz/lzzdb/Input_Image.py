import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import torch
from PIL import Image
import torchvision
from torch._C.cpp import nn
from torch.nn import *
import torchvision
from torch import nn, optim
from torch.nn import *
from torch.optim.lr_scheduler import StepLR
from torch.utils.data import DataLoader
import torch
from torch.utils.tensorboard import SummaryWriter
from Model import *
device = torch.device("cuda")


class filedialogdemo(QWidget):

    def __init__(self, parent=None):
        super(filedialogdemo, self).__init__(parent)
        layout = QVBoxLayout()

        self.btn = QPushButton()
        self.btn.clicked.connect(self.loadFile)
        self.btn.setText("选择照片")
        layout.addWidget(self.btn)



        self.label = QLabel()
        layout.addWidget(self.label)

        self.content = QTextEdit()
        self.content.setPlainText("只可以放飞机, 汽车, 鸟, 猫, 鹿, 狗, 青蛙, 马, 船, 卡车")
        layout.addWidget(self.content)
        self.setWindowTitle("识别图片")

        self.setLayout(layout)

    def loadFile(self):
        print("load--file")
        fname, _ = QFileDialog.getOpenFileName(self, '选择图片', 'E:\\Python Test\\Torch Test', 'Image files(*.jpg *.gif *.png)')

        Train = ['飞机', '汽车', '鸟', '猫', '鹿', '狗', '青蛙', '马', '船', '卡车']
        target = {}
        epoch = 0
        for i in Train:
            target[epoch] = i
            epoch = epoch + 1
        img = fname
        imgs = Image.open(img)
        transform = torchvision.transforms.Compose([torchvision.transforms.Resize((32, 32)),
                                                    torchvision.transforms.ToTensor()])
        imgs = transform(imgs)
        imgs = torch.reshape(imgs, (1, 3, 32, 32))

        # 创建网络模型
        lzz = torch.load("Lzz_111000")
        # print(lzz)
        imgs = imgs.to(device)
        output = lzz(imgs)

        print(output)
        max = output.max()

        i = output.argmax(1)
        i = i.item()
        self.content.setText(str("这是"+target.get(i)))
        self.label.setPixmap(QPixmap(fname))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fileload =  filedialogdemo()
    fileload.show()
    sys.exit(app.exec_())
