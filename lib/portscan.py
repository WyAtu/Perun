#!/usr/bin/env python
# -*- coding:utf-8 -*-

def port_scan(ip, port):
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, int(port)))
    except:
        return False, (False, False)

    try:
        s.send('hello')
        r = s.recv(512)
        s.close()
    except:
        pass
    try:
        return True, get_web_info(ip, port)
    except:
        return False, False,False

globals()['port_scan'] = port_scan