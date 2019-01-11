#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Reference: https://github.com/ysrc/xunfeng/blob/master/vulscan/vuldb/crack_mongo.py

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'mongodb_unauth'
        self.info = "Check the MongoDB unauthorized access"
        self.keyword = ['all', 'mongodb', 'mongo', 'db', 'database', 'unauth', 'weak_password', 'intranet', '27017']
        self.default_ports_list = [27017,]
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        try:
            socket.setdefaulttimeout(timeout)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, int(port)))
            data = binascii.a2b_hex(
                "3a000000a741000000000000d40700000000000061646d696e2e24636d640000000000ffffffff130000001069736d6173746572000100000000")
            s.send(data)
            result = s.recv(1024)
            if "ismaster" in result:
                getlog_data = binascii.a2b_hex(
                    "480000000200000000000000d40700000000000061646d696e2e24636d6400000000000100000021000000026765744c6f670010000000737461727475705761726e696e67730000")
                s.send(getlog_data)
                result = s.recv(1024)
                if "totalLinesWritten" in result:
                    self._output(ip, port, "exits MongoDB unauthorized access")
        except Exception, e:
            pass

globals()['VulnChecker'] = VulnChecker
