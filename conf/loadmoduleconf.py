#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import io
import sys
import ssl
import json
import base64
import ctypes
import ftplib
import random
import urllib
import socket
import string
import struct
import difflib
import hashlib
import urllib2
import binascii
import threading
from sys import stdout
from Queue import Queue
from os.path import exists
from os import _exit as exit
from itertools import product
from os import name as osname
from urlparse import urlparse
from subprocess import PIPE, Popen
from argparse import ArgumentParser
from time import time, asctime, localtime, sleep

ssl._create_default_https_context = ssl._create_unverified_context
reload(sys)
sys.setdefaultencoding('UTF-8') 

globals()['io'] = io
globals()['re'] = re
globals()['sys'] = sys
globals()['ssl'] = ssl
globals()['exit'] = exit
globals()['json'] = json
globals()['time'] = time
globals()['PIPE'] = PIPE
globals()['Popen'] = Popen
globals()['Queue'] = Queue
globals()['sleep'] = sleep
globals()['base64'] = base64
globals()['ctypes'] = ctypes
globals()['exists'] = exists
globals()['ftplib'] = ftplib
globals()['osname'] = osname
globals()['random'] = random
globals()['urllib'] = urllib
globals()['socket'] = socket
globals()['string'] = string
globals()['struct'] = struct
globals()['stdout'] = stdout
globals()['asctime'] = asctime
globals()['difflib'] = difflib
globals()['hashlib'] = hashlib
globals()['product'] = product
globals()['urllib2'] = urllib2
globals()['binascii'] = binascii
globals()['urlparse'] = urlparse
globals()['localtime'] = localtime
globals()['threading'] = threading
globals()['ArgumentParser'] = ArgumentParser