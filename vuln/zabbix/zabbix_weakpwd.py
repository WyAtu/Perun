#!/usr/bin/env python
# -*- coding:utf-8 -*-

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'zabbix_weakpwd'
        self.info = "Check the Zabbix weak password"
        self.keyword = ['all', 'zabbix', 'weak_password', 'intranet', 'danger', '8069']
        self.default_ports_list = [8069,]
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        user_list = ['admin', 'Admin', 'guest']
        pass_list = ['', 'zabbix',]
        user_list = user_list if len(USER_LIST) == 0 else USER_LIST
        pass_list = pass_list if len(PASS_LIST) == 0 else PASS_LIST
        urls = []
        urls.append('http://%s:%d/index.php'%(ip, port) if add_web_path == "" else 'http://%s:%d/%s/index.php'%(ip, port, add_web_path))
        urls.append('http://%s:%d/zabbix/index.php'%(ip, port) if add_web_path == "" else 'http://%s:%d/%s/zabbix/index.php'%(ip, port, add_web_path))
        urls.append('https://%s:%d/index.php'%(ip, port) if add_web_path == "" else 'https://%s:%d/%s/index.php'%(ip, port, add_web_path))
        urls.append('https://%s:%d/zabbix/index.php'%(ip, port) if add_web_path == "" else 'https://%s:%d/%s/zabbix/index.php'%(ip, port, add_web_path))
        for user in user_list:
            for pass_ in pass_list:
                for url in urls:
                    try:
                        data = "&name=" + user + "&password=" + pass_ + "&autologin=1&enter=Sign+in"
                        req = Requester(url, method='post', data=data, noencode=True)
                        if 'zbx_sessionid' in req.headers and req.code == 301:
                            result = "exists Zabbix weak password, user: %s, pwd: %s"%(user, pass_)
                            self._output(ip, port, result)
                    except:
                        break

globals()['VulnChecker'] = VulnChecker