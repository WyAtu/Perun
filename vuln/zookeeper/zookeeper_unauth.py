#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Reference: https://github.com/ysrc/xunfeng/blob/master/vulscan/vuldb/zookeeper_unauth_access.py

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'zookeeper_unauth'
        self.info = "Check the Zookeeper unauthorized access"
        self.keyword = ['all', 'zookeeper', 'unauth', 'intranet', '2181']
        self.default_ports_list = [2181,]
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        try:
            socket.setdefaulttimeout(timeout)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, int(port)))
            flag = "envi"
            # envi
            # dump
            # reqs
            # ruok
            # stat
            s.send(flag)
            data = s.recv(1024)
            s.close()
            if 'Environment' in data:
                result = "Zookeeper unauthorized access"
                self._output(ip, port, result)
                return
        except:
            pass

globals()['VulnChecker'] = VulnChecker