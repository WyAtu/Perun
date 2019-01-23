#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Reference: https://github.com/ysrc/xunfeng/blob/master/vulscan/vuldb/crack_grafana.py

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'grafana_weakpwd'
        self.info = "Check the Grafana weak password"
        self.keyword = ['all', 'grafana', 'weak_password', 'danger', 'intranet', 'web', '3000']
        self.default_ports_list = [3000,]
        VulnCheck.__init__(self, ip_and_port_list)

    def check_url(self, url):
        try:
            req = Requester(url)
            if "Grafana" in req.html:
                return url
        except:
            pass
        return False

    def _check(self, ip, port):
        valid_url = ""
        pass_list = ['admin', 'admin123', '123456', 'admin888']
        user_list = ['admin'] if len(USER_LIST) == 0 else USER_LIST
        pass_list = pass_list if len(PASS_LIST) == 0 else PASS_LIST

        url1 = "http://%s:%d/grafana/login"%(ip, int(port)) if add_web_path == "" else "http://%s:%d/%s/grafana/login"%(ip, int(port), add_web_path)
        url2 = "https://%s:%d/grafana/login"%(ip, int(port)) if add_web_path == "" else "https://%s:%d/%s/grafana/login"%(ip, int(port), add_web_path)
        url3 = "http://%s:%d/login"%(ip, int(port)) if add_web_path == "" else "http://%s:%d/%s/login"%(ip, int(port), add_web_path)
        url4 = "https://%s:%d/login"%(ip, int(port)) if add_web_path == "" else "https://%s:%d/%s/login"%(ip, int(port), add_web_path)

        for url in (url1, url2, url3, url4):
            if self.check_url(url):
                valid_url = url
                break

        if valid_url == "":
            return

        header = {                 
                    "Accept-Language": "en-US,en;q=0.5",
                    "User-Agent": 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36',
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Referer": "http://thewebsite.com",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json;charset=UTF-8",
                }

        for user in user_list:
            for pass_ in pass_list:
                try:
                    post_data = r'{"user":"%s","email":"","password":"%s"}'%(user, pass_)
                    req = Requester(valid_url, method='post', data=post_data, noencode=True, header=header)
                    if "Logged in" in req.html:
                        self._output(ip, port, "exits Grafana weakpwd, user: %s pwd: %s"%(user, pass_))
                        return
                except:
                    pass

globals()['VulnChecker'] = VulnChecker