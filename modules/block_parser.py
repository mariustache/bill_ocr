#!/usr/local/bin/python3

import cv2 as cv
import numpy as np
import pytesseract

from utils import ASSERT


class BlockParser(object):
    """ """

    def __init__(self, img_path, block):
        self._img_path = img_path
        self._block = block
        self._img = None
    
    def block_image(self):
        """Uses block data to extract the corresponding image frame."""
        img = cv.imread(self._img_path)
        ASSERT(img.size != 0, "Image not loaded. Path: %s" % self._img_path)
        x, y, w, h = self._block.get_coord()
        gray_img = cv.cvtColor(img[y:y+h, x:x+w], cv.COLOR_BGR2GRAY)
        gray_img = self._remove_lines(gray_img)
        cv.imshow("Block", gray_img)
        cv.waitKey() & 0xFF
        print(pytesseract.image_to_string(gray_img, config='-psm 5'))
        return gray_img
    
    def _remove_lines(self, img):
        """Removes vertical lines from the block image."""
        edges = cv.Canny(img, 150, 500, apertureSize = 3)
        lines = cv.HoughLines(edges, 1, np.pi/180, 500)
        if lines is not None:
            for rho, theta in lines[0]:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho
                x1 = int(x0 + 1000*(-b))
                y1 = int(y0 + 1000*(a))
                x2 = int(x0 - 1000*(-b))
                y2 = int(y0 - 1000*(a))

            cv.line(img,(x1,y1),(x2,y2),(255,255,255),2)

        return img