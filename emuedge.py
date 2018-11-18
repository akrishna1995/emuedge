#This is the main entry point for emuegde
#! /usr/bin/python

import os
import sys
import bin.mxen as xen
import logging 

LOG_FILE= "emuedge.log"
path_to_log_file= os.path.join ( os.path.dirname(os.path.abspath(__file__)), "logs",LOG_FILE)

def main():
    print "Starting EmuEdge v2.0.0"
    logging.basicConfig(filename=path_to_log_file, level=logging.INFO)
    #handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=20, backupCount=5)
    #my_logger.addHandler(handler)
    logging.info("Basic Test Message")
    xnet=xen.test_topo(topo='exps/twoway_simple.topo', start=True, nolog=False)
    
if __name__ == "__main__" :
    sys.exit(main());