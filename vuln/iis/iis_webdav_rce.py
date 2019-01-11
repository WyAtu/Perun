#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Reference: https://github.com/ysrc/xunfeng/blob/master/vulscan/vuldb/iis_webdav_rce.py

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'iis_webdav_rce'
        self.info = "Check the IIS WebDav RCE CVE-2017-7269"
        self.keyword = ['all', 'iis', 'webdav', 'RCE', 'web', 'intranet', 'danger', 'cve_2017_7269']
        self.default_ports_list = WEB_PORTS_LIST
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        try:
            socket.setdefaulttimeout(timeout)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            pay = "OPTIONS / HTTP/1.0\r\n\r\n"
            s.send(pay) 
            data = s.recv(2048)
            s.close()
            if "PROPFIND" in data and "Microsoft-IIS/6.0" in data :
                result = "Maybe exists IIS WebDav RCE CVE-2017-7269"
                self._output(ip, port, result)
        except:
            pass

globals()['VulnChecker'] = VulnChecker