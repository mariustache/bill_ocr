#!/usr/local/bin/python3

import os
import cv2 as cv

from utils import LISTDIR
from utils import JOIN
from utils import cfg_path
from utils import get_template_paths

from modules.block_parser import BlockParser
from modules.block_extractor import BlockExtractor

def generate_cfg():
    """Generate/update .cfg files for each bill template."""
    
    if not os.path.exists(cfg_path):
        os.mkdir(cfg_path)
        
    for img_path in get_template_paths():
        extractor = BlockExtractor(img_path)
        extractor.get_cfg()
        for block in extractor.get_blocks():
            img = BlockParser(img_path, block).block_image()
            #cv.imshow("Block", img)
            #cv.waitKey() & 0xFF

if __name__ == '__main__':
    generate_cfg()
