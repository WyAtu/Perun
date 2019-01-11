#!/usr/bin/env python
# -*- coding:utf-8 -*-

import ctypes
# import traceback, and then use traceback.print_exc() for easier debugging
# import traceback
from sys import exit, argv
from urllib import urlopen

def load_file(load_filename):
    try:
        load_file_path = '%s/%s.py'%(load_file_base_path, load_filename.replace('.', '/'))
        try:
            load_source = open(load_file_path).read()
        except IOError:
            try:
                load_source = urlopen(load_file_path).read()
            except IOError:
                exit('[-] Load file url/path error')
    except:
        exit('[-] Load file url/path error')
    try:
        load_code = compile(load_source, load_file_path, 'exec')
        exec(load_code)
    except:
        # traceback.print_exc()
        exit('[-] Load code error')

def main():
    flags = ['-l', '-load-file-path']
    for flag in flags:
        if flag in argv:
            load_flag = 1
            try:
                load_file_base_path = argv[argv.index(flag)+1]
                globals()['load_file_base_path'] = load_file_base_path
                load_file('start')
                break
            except:
                try:
                    exit('[-] Load file url/path error')
                except:
                    exit(0)
        else:
            load_flag = 0
    if not load_flag:exit("[-] %s need a url to load start.py, use '-l' or '--load-file-path' to set the load_file_path"%(argv[0].replace('.py', '')))

if __name__ == "__main__":
    main()