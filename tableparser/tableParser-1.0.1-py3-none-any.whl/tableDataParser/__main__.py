import matplotlib.pyplot as plt
# %matplotlib inline 
# import numpy as np
# import pandas as pd
from pdf2image import convert_from_bytes, convert_from_path
import cv2
import layoutparser as lp
import pytesseract
from detectron2 import model_zoo
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
import os
import sys

file_name = sys.argv[1]
# print(file_name)

images = convert_from_path(file_name)
# os.makedirs(os.path.join(os.getcwd(), "images"))
for i in range(len(images)):
#   images[i].save('images/'+'page'+ str(i) +'.jpg', 'JPEG')
  images[i].save('page'+ str(i) +'.jpg', 'JPEG')

model = lp.Detectron2LayoutModel(
            config_path ='lp://PubLayNet/mask_rcnn_X_101_32x8d_FPN_3x/config', # In model catalog
            label_map   = {0: "Text", 1: "Title", 2: "List", 3:"Table", 4:"Figure"}, # In model`label_map`
            extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.8] # Optional
        )

for filename in os.listdir(os.getcwd()):
  if filename.endswith(".jpg"):
    image = cv2.imread(os.path.join(os.getcwd(), filename))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    layout = model.detect(image)
    text_blocks = lp.Layout([b for b in layout if b.type=='Table'])
    figure_blocks = lp.Layout([b for b in layout if b.type=='Figure'])
    text_blocks = lp.Layout([b for b in text_blocks \
                   if not any(b.is_in(b_fig) for b_fig in figure_blocks)])
    # print(text_blocks)
    ocr_agent = lp.TesseractAgent(languages='eng')
    
    for block in text_blocks:
      segment_image = (block
                       .pad(left=5, right=5, top=5, bottom=5)
                       .crop_image(image))
      text = ocr_agent.detect(segment_image)
      block.set(text=text, inplace=True)
    
    for i, txt in enumerate(text_blocks.get_texts()):
        my_file = open("output.txt","a+")
        my_file.write(txt)

