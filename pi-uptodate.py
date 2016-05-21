#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Martijn van Leeuwen'
__description__ = "Keep your Raspberry Pi up to date. "
"""
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
"""
# Todo:Update the list with actions taken and to implement
"""
# Get data from input parameters.
# Check connections
# Login
# Update
# ===========================================================================
# Imports
# ===========================================================================
"""
# import re
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
  global datestamp
  global timestamp
  global monthstamp
  global yearstamp
  global logdir
  global logfile
  global pid_file
  global defuser
  global defpwd

  config = ConfigParser.ConfigParser()
  config.read("./pi-uptodate.cnf")
  datestamp = time.strftime("%Y-%m-%d")
  timestamp = time.strftime("%H:%M:%S")
  monthstamp = time.strftime("%m")
  yearstamp = time.strftime("%Y")
  rhs=os.environ.
  logdir = config.get('System', 'logdir')
  pid_file = config.get('System', 'pid')
  logfile = config.get('System', 'logfile')
  defuser = config.get('Defaults', 'defuser')
  defpwd = config.get('Defaults', 'defpwd')

  if logdir == "": logdir = "/var/log/"
  if pid_file == "": pid_file = "/var/run/pi-uptodate.pid"
  if logfile == "": logfile = "pi-utd.log"


def ssh_command(ip, user, passwrd, command, *keyfile):
  client = paramiko.SSHClient()
  if keyfile:
    client.load_host_keys(keyfile)
  client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  client.connect(ip, username=user, password=passwrd)
  ssh_session = client.get_transport().open_session()
  if ssh_session.active:
    ssh_session.send(command)
    print ssh_session.recv(1024)  # Read banner
    while True:
      command = ssh_session.recv(1024)  # Get the command from the SSH server
      try:
        cmd_output = subprocess.check_output(command, shell=true)
        ssh_session.send(cmd_output)

        ssh_session.send(str(e))
    client.close()
  return


def main():
  # Initialise base and default parameters
  init()

  TESTIP = "192.168.0.12"

  # Check if parameters where parsed. I not, display usage.
  if not len(sys.argv[ 1: ]):
    usage()

  # Get input from command line.
  opts, args = getopt.getopt(sys.argv[ 1: ], "AaCcDd")
  if not args:
    usage()

  print "defuser: ", defuser
  print "defpwd: ", defpwd
  print "Datestamp: ", datestamp
  print "Logfile: ", logfile

  print "Connecting to: ", TESTIP
  ssh_command(ip=TESTIP, user=defuser, passwrd=defpwd, command="ls -la")


# ===========================================================================
# Main
# ===========================================================================
if __name__ == "__main__":
  main()
