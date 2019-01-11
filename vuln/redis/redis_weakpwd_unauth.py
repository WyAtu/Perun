#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Reference: https://github.com/ysrc/xunfeng/blob/master/vulscan/vuldb/crack_redis.py

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'redis_weakpwd_unauth'
        self.info = "Check the Redis weak password and unauthorized access"
        self.keyword = ['all', 'redis', 'unauth', 'weak_password', 'intranet', 'danger', '6379']
        self.default_ports_list = [6379,]
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        pass_list = ['redis', 'root', 'oracle', 'password', 'p@aaw0rd', 'abc123!', '123456', 'admin', 'admin123', '',]
        pass_list = pass_list if len(PASS_LIST) == 0 else PASS_LIST
        try:
            socket.setdefaulttimeout(timeout)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, int(port)))
            s.send("INFO\r\n")
            recv = s.recv(1024)
            if "redis_version" in recv:
                result = "exists Redis unauthorized access"
                self._output(ip, port, result)
                return
            elif "Authentication" in recv:
                for _pass in pass_list:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((ip, int(port)))
                    s.send("AUTH %s\r\n" %(_pass))
                    recv = s.recv(1024)
                    if '+OK' in recv:
                        resul = "pwd: %s"(_pass)
                        self._output(ip, port, result)
                        return
        except:
            pass

globals()['VulnChecker'] = VulnChecker