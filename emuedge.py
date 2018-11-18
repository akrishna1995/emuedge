#This is the main entry point for emuegde
#! /usr/bin/python

import os
import sys
import bin.mxen as xen
import logging 
import logging.handlers

LOG_FILE= "emuedge.log"
path_to_log_file= os.path.join ( os.path.dirname(os.path.abspath(__file__)), "logs",LOG_FILE)

def main():
    print "Starting EmuEdge v2.0.0"
    logger = logging.getLogger("emuedge")
    logger.setLevel(logging.INFO)
    handler = logging.handlers.RotatingFileHandler(path_to_log_file, maxBytes=5242880, backupCount=10)
    formatter = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logging.info("Basic Test Message")
    xnet=xen.test_topo(topo='exps/twoway_simple.topo', start=True, nolog=False)
    
if __name__ == "__main__" :
    sys.exit(main());