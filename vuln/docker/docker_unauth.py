#!/usr/bin/env python
# -*- coding:utf-8 -*-

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'docker_unauth'
        self.info = "Check the Docker unauthorized access"
        self.keyword = ['all', 'docker', 'unauth', 'intranet', 'dangers', '2375']
        self.default_ports_list = [2375,]
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        try:
            socket.setdefaulttimeout(timeout)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, int(port)))
            s.send("GET /containers/json HTTP/1.1\r\nHost: %s:%s\r\n\r\n"%(ip, port))
            recv = s.recv(1024)
            if "HTTP/1.1 200 OK" in recv and 'Docker' in recv and 'Api-Version' in recv:
                result = "Docker unauthorized access"
                self._output(ip, port, result)
                return
        except:
            pass

globals()['VulnChecker'] = VulnChecker