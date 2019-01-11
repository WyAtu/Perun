#!/usr/bin/env python
# -*- coding:utf-8 -*-

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'nexus_weakpwd'
        self.info = "Check the Sonatype Nexus Repository Manager weak password"
        self.keyword = ['all', 'nexus', 'weak_password', 'web', '8081']
        self.default_ports_list = [8081,]
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        url1 = "http://%s:%d/service/rapture/session"%(ip, int(port)) if add_web_path == "" else "http://%s:%d/%s/service/rapture/session"%(ip, int(port), add_web_path)
        url2 = "https://%s:%d/service/rapture/session"%(ip, int(port)) if add_web_path == "" else "https://%s:%d/%s/service/rapture/session"%(ip, int(port), add_web_path)
        user_list = ['admin', 'anonymous', 'deployment',]
        pass_list = ['admin', 'admin123', '123456', 'root', 'password','p@ssw0rd','1qaz2wsx', 'qwer!@#$', 'qwer1234', '|$|N|E|X|U|S|$|', '',]

        user_list = user_list if len(USER_LIST) == 0 else USER_LIST
        pass_list = pass_list if len(PASS_LIST) == 0 else PASS_LIST

        for user in user_list:
            for pwd in pass_list:
                data = {'username':base64.b64encode(user.encode()).decode(), 'password':base64.b64encode(pwd.encode()).decode()}
                try:
                    req = Requester(url1, data=data, method='post')
                    if req.code == 204 or req.code == 405:
                        result = "user: %s pwd: %s"%(user, pwd)
                        self._output(ip, port, result)
                        return
                except RequesterOpenError:
                    try:
                        req = Requester(url2, header=data, method='post')
                        if req.code == 204 or req.code == 405:
                            result = "user: %s pwd: %s"%(user, pwd)
                            self._output(ip, port, result)
                            return
                    except:
                        pass
                except:
                    pass

globals()['VulnChecker'] = VulnChecker