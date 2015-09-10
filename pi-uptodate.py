#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Martijn van Leeuwen'
# ==============================================================================
#
#  App name: pi-uptodate.py
#
#  Target system:  Linux
#
#  Description:
#
#    A 'possible collection of' python script(s) to maintain:
#    * Raspberry Pi's
#    * Banana Pi's
#    * Hummingboards
#
# ==============================================================================
#
# Todo:
#
# Get data from input parameters.
# Check connections
# Login
# Update
# ===========================================================================
# Imports
# ===========================================================================
#import re
import sys
import getopt
import threading
import paramiko
import subprocess
import time
import os
import ConfigParser

# ===========================================================================
# Global settings
# ===========================================================================
datestamp = ""
timestamp = ""
monthstamp = ""
yearstamp = ""
logdir = ""
logfile = ""
pid_file = ""
defuser = ""
defpwd = ""

def usage():
  print "==========================================================================="
  print "App: pi-uptodate.py"
  print "==========================================================================="
  print
  print "Usage: pi-uptodatep.py -c <config file> -a action"
  print
  print "Actions:"
  print "==================================="
  print ""
  print ""
  print ""
  sys.exit(0)

# ===========================================================================
# Settings, etc
# ===========================================================================


def init():
  config = ConfigParser.ConfigParser()
  config.read("pi-uptodate.cnf")

  datestamp = time.strftime("%Y-%m-%d")
  timestamp = time.strftime("%H:%M:%S")
  monthstamp = time.strftime("%m")
  yearstamp = time.strftime("%Y")

  logdir = config.get('System', 'logdir')
  pid_file = config.get('System', 'pid')
  logfile = config.get('System', 'logfile')
  defuser = config.get('Defaults', 'defuser')
  defpwd = config.get('Defaults', 'defpwd')

  if logdir == "" : logdir = "/var/log/"
  if pid_file == "" : pid_file = "/var/run/pi-uptodate.pid"
  if logfile == "" : logfile = "pi-utd.log"


#def get_selection():


def ssh_command(ip, user, passwrd, command, keyfile):
  client = paramiko.SSHClient()
  if keyfile:
    client.load_host_keys(keyfile)

  client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  client.connect(ip, username=user, password=passwd)
  ssh_session = client.get_transport().open_session()
  if ssh_session.active:
    ssh_session.send(command)
    print ssh_session.recv(1024)# Read banner
    while True:
      command = ssh_session.recv(1024) #Get the command from the SSH server
      try:
        cmd_output = subprocess.check_output(command, shell=true)
        ssh_session.send(cmd_output)
      except Exception,e:
        ssh_session.send(str(e))
    client.close()
  return


def main():
  #Initialise base and default parameters
  init()

  # Some global variables
  global action
  global configfile

  # Check if parameters where parsed. I not, display usage.
  if not len(sys.argv[1:]):
    usage()

  # Get input from command line.
  opts, args = getopt.getopt(sys.argv[1:], "AaCcDd")
  if not args:
    usage()


# ===========================================================================

# Main
# ===========================================================================
if __name__ == "__main__":
  main()