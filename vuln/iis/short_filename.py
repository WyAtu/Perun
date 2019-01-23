#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Reference: http://0cx.cc/iis_short_scaner.jspx

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'short_filename'
        self.info = "Check the IIS short filename vuln"
        self.keyword = ['all', 'iis', 'shortfile', 'shortfilename', 'filename', 'info', 'web']
        self.default_ports_list = WEB_PORTS_LIST
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        url1_400 = "http://%s:%d/san1e*~1****/a.aspx"%(ip, int(port)) if add_web_path == "" else "http://%s:%d/%s/san1e*~1****/a.aspx"%(ip, int(port), add_web_path)
        url1_404 = "http://%s:%d/*~1****/a.aspx"%(ip, int(port)) if add_web_path == "" else "http://%s:%d/%s/*~1****/a.aspx"%(ip, int(port), add_web_path)
        url2_400 = "https://%s:%d/san1e*~1****/a.aspx"%(ip, int(port)) if add_web_path == "" else "https://%s:%d/%s/san1e*~1****/a.aspx"%(ip, int(port), add_web_path)
        url2_404 = "https://%s:%d/*~1****/a.aspx"%(ip, int(port)) if add_web_path == "" else "https://%s:%d/%s/*~1****/a.aspx"%(ip, int(port), add_web_path)

        try:
            req_400 = Requester(url1_400)
            req_404 = Requester(url1_404)
            if req_400.code == 400 and req_404.code == 404:
                result = "exists IIS short filename vuln"
                self._output(ip, port, result)
        except RequesterOpenError:
            try:
                req_400 = Requester(url2_400)
                req_404 = Requester(url2_404)
                if req_400.code == 400 and req_404.code == 404:
                    result = "exists IIS short filename vuln"
                    self._output(ip, port, result)
            except: pass
        except: pass

globals()['VulnChecker'] = VulnChecker