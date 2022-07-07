import numpy as np
import cv2 as cv
import json
import unittest
import matplotlib.pyplot as plt
import pv_vision.transform_crop.perspective_transform as pt
import pv_vision.transform_crop.cell_crop as crop
from pathlib import Path


class TestPerspectiveTransform(unittest.TestCase):

    img_only = Path("testing/img_only")
    img_mask = Path("testing/img_mask")

    def testImageThreshold(self):
        image = cv.imread(str(self.img_only/"M2001-0013_48432mV_9135mA_19.2Sec.jpg"), 0)
        img_thre_ad = pt.image_threshold(image, adaptive=True)
        img_thre = pt.image_threshold(image, threshold=50, adaptive=False)

        plt.figure(figsize=(10, 15))
        plt.subplot(311)
        plt.imshow(image, "gray")
        plt.subplot(312)
        plt.imshow(img_thre_ad, "gray")
        plt.subplot(313)
        plt.imshow(img_thre, "gray")
        plt.show()
        plt.clf()
        self.assertEqual(255, img_thre_ad.max())
        self.assertEqual(255, img_thre.max())

class TestCellCrop(unittest.TestCase):
    img_only = Path("testing/img_only")
    img_mask = Path("testing/img_mask")

    def testLineDetection(self):
        image = cv.imread(str(self.img_only / "PA3.jpg"), 0)
        image_thre = pt.image_threshold(image, adaptive=True)
        plt.figure(figsize=(10, 15))
        plt.subplot(211)
        plt.imshow(image, "gray")
        plt.subplot(212)
        plt.imshow(image_thre, "gray")
        plt.show()
        plt.clf()

        vline_abs = crop.detect_vertical_lines(image_thre, column=12)
        hline_abs = crop.detect_horizon_lines(image_thre, row=6, busbar=4)



if __name__ == '__main__':
    unittest.main()
