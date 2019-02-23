#!/usr/bin/env python
# -*- coding:utf-8 -*-
# https://devco.re/blog/2019/02/19/hacking-Jenkins-part2-abusing-meta-programming-for-unauthenticated-RCE/

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'unauth2rce'
        self.info = "Check if the Jenkins path exists for Jenkins pre-auth RCE chained by CVE-2018-1000861 and CVE-2019-10030000"
        self.keyword = ['all', 'jenkins', 'unauth', 'rce', 'web', 'danger', 'intranet']
        self.default_ports_list = WEB_PORTS_LIST
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        result = "maybe Jenkins pre-auth RCE chained by CVE-2018-1000861 and CVE-2019-10030000"
        poc_data = "/securityRealm/user/admin/descriptorByName/org.jenkinsci.plugins.workflow.cps.CpsFlowDefinition/checkScriptCompile"
        url_base1 = "http://%s:%d"%(ip, int(port)) if add_web_path == "" else "http://%s:%d/%s"%(ip, int(port), add_web_path)
        url_base2 = "https://%s:%d"%(ip, int(port)) if add_web_path == "" else "https://%s:%d/%s"%(ip, int(port), add_web_path)
        try:
            req = Requester(url_base1+poc_data)
            if "java.lang.NullPointerException" in req.html:
                self._output(ip, port, result)
        except RequesterOpenError:
            try:
                req = Requester(url_base2+poc_data)
                if "java.lang.NullPointerException" in req.html:
                    self._output(ip, port, result)
            except: pass
        except: pass

globals()['VulnChecker'] = VulnChecker