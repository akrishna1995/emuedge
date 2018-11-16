#! /usr/bin/python

import logging
import os

path = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(filename=os.path.join(path, 'logs', 'emuedge.log'),level=logging.INFO)


