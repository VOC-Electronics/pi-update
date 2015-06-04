#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Martijn van Leeuwen'
# ==============================================================================
##
##  App name: pi-uptodate.py
##
##  Target system:  ARM
##
##  Descrption:
##
##    A 'possible collection of' python script(s) to maintain:
##    * Raspberry Pi's
##    * Banana Pi's
##    * Hummingboards
##
# ==============================================================================

#import subprocess
#import re
import sys
import time
import os
import ConfigParser

def usage():
  print "==========================================================================="
  print "App: pi-uptodate.py"
  print "==========================================================================="
  print
  print "Usage: system-backup.py -c <config file> -a action"
  print
  print "Actions:"
  print "==================================="
  print ""
  print ""
  print ""
  sys.exit(0)

def main():
  global action
  global configfile

  if not len(sys.argv[1:]):
    usage()


# ===========================================================================
# Main
# ===========================================================================
if __name__ == "__main__":
  main()