#!/usr/bin/env python
# -*- coding:utf-8 -*-

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'activemq_weakpwd'
        self.info = "Check the ActiveMQ weak password"
        self.keyword = ['all', 'activemq', 'weak_password', 'web', 'intranet', '8161']
        self.default_ports_list = [8161,]
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        url1 = "http://%s:%d/admin"%(ip, int(port)) if add_web_path == "" else "http://%s:%d/%s/admin"%(ip, int(port), add_web_path)
        url2 = "https://%s:%d/admin"%(ip, int(port)) if add_web_path == "" else "https://%s:%d/%s/admin"%(ip, int(port), add_web_path)
        user_list = ['admin', 'root', 'activemq', 'ActiveMQ',]
        pass_list = ['admin', 'admin123', '123456', 'root', 'activemq', 'ActiveMQ', 's3cret', 'password','p@ssw0rd','1qaz2wsx', 'qwer!@#$', 'qwer1234', '',]

        user_list = user_list if len(USER_LIST) == 0 else USER_LIST
        pass_list = pass_list if len(PASS_LIST) == 0 else PASS_LIST

        for user in user_list:
            for pwd in pass_list:
                data = {'Authorization':'Basic '+base64.b64encode((user+':'+pwd).encode()).decode()}
                try:
                    req = Requester(url1, header=data)
                    if 'Welcome'.lower() in str(req.html).lower() and "ActiveMQ Console".lower() in str(req.html).lower():
                        result = "user: %s pwd: %s"%(user, pwd)
                        self._output(ip, port, result)
                        return
                except RequesterOpenError:
                    try:
                        req = Requester(url2, header=data)
                        if'Welcome'.lower() in str(req.html).lower() and "ActiveMQ Console".lower() in str(req.html).lower():
                            result = "user: %s pwd: %s"%(user, pwd)
                            self._output(ip, port, result)
                            return
                    except:
                        pass
                except:
                    pass

globals()['VulnChecker'] = VulnChecker