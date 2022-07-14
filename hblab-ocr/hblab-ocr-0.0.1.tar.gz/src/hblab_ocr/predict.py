import torch
from .structure.model import SegDetectorModel
from .utils.pre_process import load_image
from .utils.post_process import process
from .download_object import download_file_from_google_drive

BACKBONE_CONFIG = {'backbone': 'deformable_resnet50',
                   'decoder': 'SegDetector',
                   'decoder_args': {'adaptive': True, 'in_channels': [256, 512, 1024, 2048], 'k': 50},
                   'loss_class': 'L1BalanceCELoss'}
PRETRAINED = 'text_detection_weight'
link_id = "1OvP6erktLrV0AzBiJjuU9j1B7nyv7S5S"


class TextDetector:
    def __init__(self, config=None, is_pretrained=True):
        if config is None:
            config = BACKBONE_CONFIG
        self.init_torch_tensor()
        self.model = SegDetectorModel(config, self.device)
        self.is_pretrained = is_pretrained
        if self.is_pretrained:
            print('Download pretrained for prediction ....')
            download_file_from_google_drive(link_id, PRETRAINED)
            print('Done !!!')
            self.load_pretrained()

    def load_pretrained(self):
        self.model.load_state_dict(torch.load(PRETRAINED, map_location=self.device), strict=False)

    def init_torch_tensor(self):
        torch.set_default_tensor_type('torch.FloatTensor')
        if torch.cuda.is_available():
            self.device = torch.device('cuda')
            torch.set_default_tensor_type('torch.cuda.FloatTensor')
        else:
            self.device = torch.device('cpu')

    def predict(self, image_path):
        image, original_shape = load_image(image_path)
        predict = self.model(image)
        b, s = process(predict, original_shape)
        return b, s

#
# if __name__ == "__main__":
#     detector = TextDetector(BACKBONE_CONFIG, is_pretrained=True)
#     boxes, scores = detector.predict(image_path='/home/backtracking/Desktop/DB/7885334b83408e7619df46e9debb1783.jpeg')
#     print(boxes, scores)
