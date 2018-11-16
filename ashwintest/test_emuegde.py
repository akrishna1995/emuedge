#! /usr/bin/python

import sys
import os
from .. import xen
def main():
   print "Hello World"
   xnet=xen.test_topo(topo='exps/twoway_simple.topo', start=True, nolog=False)

if __name__ == "__main__" :
    sys.exit(main())
