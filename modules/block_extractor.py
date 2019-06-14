#!/usr/local/bin/python3

import cv2 as cv

from utils import OPEN
from utils import ASSERT
from utils import cfg_path
from utils import BlockData
from utils import Configurator

from modules.factura_standard import FacturaStandard


class BlockExtractor(object):

    def __init__(self, img_path):
        self._img_path = img_path
        self._img = None
        self._cfg_path = cfg_path + img_path.split('/')[-1].split('.')[0] + ".cfg"
        self._block_data = list()  # list of BlockData elements
        self._configurator = Configurator()

    def _get_image(self):
        """Open input image and set format to HSV."""
        self._img = cv.imread(self._img_path)

        ASSERT(self._img.size != 0, "Image not loaded. Path: %s" % self._img_path)
        
        hsv_img = cv.cvtColor(self._img, cv.COLOR_BGR2HSV)

        return hsv_img

    def _white_blocks(self, hsv_image):
        """Get data blocks from input image.
        
        Returns a black image with white contours representing the blocks.
        """
        lower_mask = cv.inRange(hsv_image, BlockData.lower_red[0], BlockData.lower_red[1])
        upper_mask = cv.inRange(hsv_image, BlockData.upper_red[0], BlockData.upper_red[1])
        bw_img = lower_mask + upper_mask
        
        return bw_img
    
    def _get_wb(self, bw_img):
        """Identify white blocks and save their coordinates."""
        _, contours, _ = cv.findContours(bw_img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        ASSERT(len(contours) != 0, "No contours found. Check template image.")

        for c in contours:
            x, y, w, h = cv.boundingRect(c)
            self._block_data.append(BlockData(x, y, w, h))

    def get_blocks(self):
        """Functionality wrapper that returns a list of BlockData objects."""
        hsv_img = self._get_image()
        bw_img = self._white_blocks(hsv_img)
        self._get_wb(bw_img)

        return self._block_data

    def get_cfg(self):
        out_cfg = OPEN(self._cfg_path, "w")
        [out_cfg.write(key + ":" + value + "\n") for key, value in self._configurator.get_dict().items()]
        out_cfg.close()

