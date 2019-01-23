#!/usr/bin/env python
# -*- coding:utf-8 -*-

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'glassfish_weakpwd'
        self.info = "Check the Glassfish weak password"
        self.keyword = ['all', 'glassfish', 'weak_password', 'danger', 'web', 'internet', '4848']
        self.default_ports_list = [4848,]
        VulnCheck.__init__(self, ip_and_port_list)

    def check_url(self, url):
        try:
            req = Requester(url)
            if "GlassFish" in req.html and req.code == 200:
                return url
        except:
            pass
        return False

    def _check(self, ip, port):
        valid_url = ""
        pass_list = ['', 'admin', 'admin123', '123456', 'admin888', 'glassfish', 'vulhub_default_password']
        user_list = ['admin'] if len(USER_LIST) == 0 else USER_LIST
        pass_list = pass_list if len(PASS_LIST) == 0 else PASS_LIST

        url1 = "http://%s:%d/common/j_security_check"%(ip, int(port)) if add_web_path == "" else "http://%s:%d/%s/common/j_security_check"%(ip, int(port), add_web_path)
        url2 = "https://%s:%d/common/j_security_check"%(ip, int(port)) if add_web_path == "" else "https://%s:%d/%s/common/j_security_check"%(ip, int(port), add_web_path)
        url3 = "http://%s:%d/j_security_check"%(ip, int(port)) if add_web_path == "" else "http://%s:%d/%s/j_security_check"%(ip, int(port), add_web_path)        
        url4 = "https://%s:%d/j_security_check"%(ip, int(port)) if add_web_path == "" else "https://%s:%d/%s/j_security_check"%(ip, int(port), add_web_path)

        for url in (url1, url2, url3, url4):
            if self.check_url(url):
                valid_url = url
                break

        if valid_url == "":
            return

        for user in user_list:
            for pass_ in pass_list:
                post_data = {"j_username":user, "j_password":pass_, "loginButton":"Login", "loginButton.DisabledHiddenField":"true"}
                try:
                    req = Requester(valid_url, method='post', data=post_data)
                    if req.code == 301:
                        self._output(ip, port, "exits Glassfish weak password, user: %s pwd: %s"%(user, pass_))
                        return
                except:
                    pass

globals()['VulnChecker'] = VulnChecker