from detector.detect import subway_det
from classifier.class_net_test import class_net_test
from utils.transform import data_detile
import cv2
import numpy as np
from PIL import Image

class detector(object):
    def __init__(self,config):
        self.config=config
        self.transform=data_detile(self.config.preprocess).transforms
        # 加载检测模块
        self.sud_det=subway_det(self.config.detect_model)

        # 加载粗粒度分类模块
        self.Coarse_grained_class = class_net_test(self.config.coarse_model,self.transform)

        # 加载细粒度分类模块
        self.fine_grained_class=class_net_test(self.config.fine_model,self.transform)

    def detect(self,img):
        self.result = []
        # 检测模块
        self.roi_list = self.sud_det.detector(img)
        # 将每一个roi输入分类网络
        for i in range(self.roi_list.shape[0]):
            box=self.roi_list[i,0:4]
            confidence=self.roi_list[i,-2]
            class_name=self.roi_list[i,-1]
            # 这里只对低分框进行再分类
            if float(confidence)>0.05:
                self.result.append(self.roi_list[i])
                continue
            else:
                box=box.astype(np.int)
                img_test=img[box[1]:box[3],box[0]:box[2],:]
                img_test = Image.fromarray(cv2.cvtColor(img_test,cv2.COLOR_BGR2RGB))

                # 粗粒度分类
                class_name=self.Coarse_grained_class.test_img(img_test,score_thr=0.5)
                if class_name[0][0]!=0:
                    continue
                else:
                    # 细粒度分类
                    class_name=self.fine_grained_class.test_img(img_test,score_thr=0.5)
                    if class_name[0][0]!=0:
                        continue
                    else:
                        # 将检测结果输出为类别
                        self.roi_list[i, 0]=class_name[0][0]
                        self.result.append(self.roi_list[i])
        return self.result
