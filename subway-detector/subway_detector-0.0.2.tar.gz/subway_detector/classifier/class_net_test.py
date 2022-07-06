import torch
import heapq
from model import build_model



class class_net_test(object):
    def __init__(self, config,transform):
        self.config = config
        self.creat_model(self.config)
        self.load_model(self.config.model_path)
        self.transform = transform

    def creat_model(self, config):
        self.model = build_model(config.arch,config.kwargs)
        if torch.cuda.is_available():
            self.model.cuda()

    def load_model(self,model_path):
        dic = torch.load(model_path, map_location=lambda storage, loc: storage)
        self.model.load_state_dict(dic)
        self.model.cuda()
        self.model.eval()


    def test_img(self, img, score_thr):
        img = self.transform(img)
        img = torch.unsqueeze(img, 0).cuda()
        output = self.model(img)
        output_max = torch.max(torch.softmax(output, 1), 1)
        comp = output_max[0] < score_thr
        doubt = comp.cpu().numpy()

        # _, predicted = torch.max(output.data, 1)

        all_top3 = []
        for idx in range(output.size(0)):
            output3 = output[idx].cpu().data.numpy()
            top3 = heapq.nlargest(3, range(len(output3)), output3.take)
            all_top3.append(top3)

        return all_top3, doubt
