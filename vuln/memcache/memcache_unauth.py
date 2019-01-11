#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Reference: https://github.com/ysrc/xunfeng/blob/master/vulscan/vuldb/memcache_unauth.py

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'memcache_unauth'
        self.info = "Check the Memcache unauthorized access"
        self.keyword = ['all', 'memcache', 'unauth', 'intranet', '11211']
        self.default_ports_list = [11211,]
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        try:
            socket.setdefaulttimeout(timeout)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, int(port)))
            s.send("stats\r\n")
            recv = s.recv(1024)
            if "STAT version" in recv:
                result = "Memcache unauthorized access"
                self._output(ip, port, result)
                return
        except:
            pass

globals()['VulnChecker'] = VulnChecker