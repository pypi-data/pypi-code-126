import numpy as np
import cv2 as cv
import json
import unittest
import matplotlib.pyplot as plt
from pv_vision.transform_crop.solarmodule import AbstractModule, MaskModule, SplitModule


class TestSolarModule(unittest.TestCase):

    def testSize(self):
        raw_image = cv.imread("img_mask/1-15-A6CB2-39-08_07_09_06_10.png", cv.IMREAD_UNCHANGED)
        raw_module = AbstractModule(raw_image, 8, 16, 0)
        self.assertEqual(raw_image.shape, raw_module.size, "Wrong module size")
        self.assertEqual(raw_image.shape, raw_module.image.shape, "Wrong module size")
        self.assertEqual([8, 16], [raw_module.row, raw_module.col], "Wrong row/col")

    def testResize(self):
        raw_image = cv.imread("img_mask/1-15-A6CB2-39-08_07_09_06_10.png", cv.IMREAD_UNCHANGED)
        raw_module = AbstractModule(raw_image, 8, 16, 0)
        img_resize = raw_module.resize((100, 200))
        self.assertEqual((100, 200), img_resize.shape)
        raw_module.resize((100, 200), in_place=True)
        self.assertEqual((100, 200), raw_module.size)

    def testRotate(self):
        raw_image = cv.imread("img_mask/1-15-A6CB2-39-08_07_09_06_10.png", cv.IMREAD_UNCHANGED)
        raw_module = AbstractModule(raw_image, 8, 16, 0)
        img_rotate = raw_module.rotate(0)
        self.assertEqual((raw_image.shape[1], raw_image.shape[0]), img_rotate.shape)
        raw_module.rotate(0, in_place=True)
        self.assertEqual([16, 8], [raw_module.row, raw_module.col])

    def testCopyChannel(self):
        raw_image = cv.imread("img_mask/1-15-A6CB2-39-08_07_09_06_10.png", cv.IMREAD_UNCHANGED)
        raw_module = AbstractModule(raw_image, 8, 16, 0)
        img_duplicate = raw_module.copy_channel()
        self.assertEqual(3, img_duplicate.shape[-1])
        self.assertEqual(img_duplicate[:, :, 0].tolist(), img_duplicate[:, :, 1].tolist())

    def testSave(self):
        raw_image = cv.imread("img_mask/1-15-A6CB2-39-08_07_09_06_10.png", cv.IMREAD_UNCHANGED)
        raw_module = AbstractModule(raw_image, 8, 16, 0)
        raw_module.resize((100, 200), in_place=True)
        raw_module.save_fig("img_mask/raw_resize.png")
        img_resize = cv.imread('img_mask/raw_resize.png', cv.IMREAD_UNCHANGED)
        self.assertEqual((100, 200), img_resize.shape)


class TestModule(unittest.TestCase):
    def testCase1(self):
        # test maskModule property
        raw_image = cv.imread("img_mask/1-15-A6CB2-39-08_07_09_06_10.png", cv.IMREAD_UNCHANGED)
        raw_module = MaskModule(raw_image, 8, 16, 0)
        self.assertEqual(raw_image.shape, raw_module.size, "Wrong module size")
        self.assertEqual(raw_image.shape, raw_module.image.shape, "Wrong module size")
        self.assertEqual([8, 16], [raw_module.row, raw_module.col], "Wrong row/col")
        self.assertIsNone(raw_module.mask)
        self.assertIsNone(raw_module.corners)
        self.assertIsNone(raw_module.corner_detection_line())
        self.assertIsNone(raw_module.corner_detection_cont())
        self.assertIsNone(raw_module.transform())
        # test load mask
        raw_module.load_mask("img_mask/1-15-A6CB2-39-08_07_09_06_10.png.json")
        self.assertIsNotNone(raw_module.mask)
        # test corner detection method contour
        corners_cnt = raw_module.corner_detection_cont(output=True)
        self.assertIsNotNone(raw_module.corners)
        # test transformed module
        transformed_module = raw_module.transform(600, 300, img_only=False)
        self.assertTrue(transformed_module.is_transformed(14, 6))
        self.assertEqual((300, 600), transformed_module.size, "Wrong module size")
        self.assertEqual([8, 16], [transformed_module.row, transformed_module.col], "Wrong row/col")
        plt.imshow(transformed_module.image, "gray")
        plt.show()
        plt.clf()
        transformed_module.save_fig("img_mask/transform.png")
        # test another corner detection method
        corners_line = raw_module.corner_detection_line(output=True)
        self.assertNotEqual(corners_line.tolist(), corners_cnt.tolist())
        self.assertEqual(corners_line.tolist(), raw_module.corners.tolist())
        transformed_module = raw_module.transform(600, 300, img_only=True)
        self.assertTrue(raw_module.is_transformed(14, 6))
        plt.imshow(transformed_module, "gray")
        plt.show()
        plt.clf()
        # test crop cells
        cells = raw_module.crop_cell(cellsize=32, vl_interval=25, vl_split_size=32,
                                     hl_interval=25, hl_split_size=32, margin=16)
        self.assertEqual(16*8, len(cells))
        plt.imshow(cells[56], "gray")
        plt.show()
        plt.clf()

    def testCase2(self):
        # test SplitModule
        raw_image = cv.imread("img_only/ELH7.jpg", cv.IMREAD_GRAYSCALE)
        module = SplitModule(raw_image, 6, 10, 3)
        cells = module.crop_cell(cellsize=250)
        plt.imshow(cells[14], "gray")
        plt.show()
        plt.clf()
        module.plot_edges()
        plt.show()
        plt.clf()

    def testCase2(self):
        #test MaskModule
        raw_image = cv.imread("img_only/FSEC_8GC14.jpg", cv.IMREAD_GRAYSCALE)
        module = MaskModule(raw_image, 6, 12, 4)
        mask = module.load_mask(thre=0.1, output=True)
        plt.imshow(mask, "gray")
        plt.show()
        plt.clf()
        module.corner_detection_cont(mode=1)
        transformed = module.transform(cellsize=250)
        plt.imshow(transformed, "gray")
        plt.show()
        plt.clf()
        cells = module.crop_cell(cellsize=250, vl_interval=200, vl_split_size=250,
                                 hl_interval=200, hl_split_size=250, margin=100)
        plt.imshow(cells[0], "gray")
        plt.show()
        plt.clf()

if __name__ == '__main__':
    unittest.main()