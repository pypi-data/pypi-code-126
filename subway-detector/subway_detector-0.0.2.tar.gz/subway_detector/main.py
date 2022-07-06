import cv2
from easydict import EasyDict
import yaml
import argparse
from subway_detector import detector
from utils.visualization import visualize_results

def test(img_path,config):
    vis_config = config.visualize
    img = cv2.imread(img_path)
    detec = detector(config)
    result = detec.detect(img)
    if(vis_config.vis):
        visualize_results(img.copy(),result,vis_config.output_dir)

parser = argparse.ArgumentParser(description='Pytorch Testing')
parser.add_argument('--image_path',default='/media/a/新加卷1/Download/Programs/detector-master/detector/img/0_358.png')
parser.add_argument('--config_path', default='/media/a/新加卷1/Download/Programs/detector-master/subway_detector/config')
if __name__ == '__main__':
    args = parser.parse_args()
    with open(args.config_path) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    config = EasyDict(config)
    test(args.image_path,config)
