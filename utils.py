#!/usr/local/bin/python3

import os
import sys
import numpy as np

from collections import OrderedDict

template_path = "./templates/"
cfg_path = "./cfg/"

def get_template_paths():
    template_list = list()
    for img_path in LISTDIR(template_path):
        template_list.append(JOIN(template_path, img_path))
    
    return template_list

def LISTDIR(path):
    ASSERT(os.path.isdir(path), "%s does not exist or is not a directory." % path)

    return os.listdir(path)

def OPEN(file_path, mode):
    try:
        file_handler = open(file_path, mode)
    except (EnvironmentError, IOError) as e:
        print("Exception: %s" % str(e))
        sys.exit()
    
    return file_handler

def JOIN(path1, path2):
    ret_path = os.path.join(path1, path2)
    # TODO check existance
    return ret_path

def ASSERT(condition, message):
    if not condition:
        print("Error: %s" % message)
        sys.exit()


class Configurator:

    def __init__(self):
        self._data = OrderedDict()
        self._data["Furnizor"] = ""
        self._data["Numar"] = ""
        self._data["Data"] = ""
        self._data["Cota tva"] = ""
        self._data["Produse"] = ""
    
    def get_dict(self):
        return self._data


class BlockData:
    # Color range for the bounding box.
    lower_red = (np.array([0, 120, 70]), np.array([10, 255, 255]))
    upper_red = (np.array([170, 120, 70]), np.array([180, 255, 255]))
    """TODO """
    def __init__(self, x=0, y=0, w=0, h=0):
        self._x = x
        self._y = y
        self._w = w
        self._h = h 

    def get_coord(self):
        return self._x, self._y, self._w, self._h
    
