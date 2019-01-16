#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Reference: https://mp.weixin.qq.com/s/EtUmfMxxJjYNl7nIOKkRmA

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'nginx_httproxy'
        self.info = "Check the improper configuration of Nginx leads to proxy"
        self.keyword = ['all', 'nginx', 'proxy', 'web',]
        self.default_ports_list = WEB_PORTS_LIST
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        url = "http://ip.360.cn/IPShare/info"
        try:
            req = Requester(url)
            req_json = json.loads(req.html)
            local_ip = req_json['ip']

            req = Requester(url, proxy={'http': '%s:%d'%(ip, port)})
            req_json = json.loads(req.html)
            proxy_ip = req_json['ip']

            if local_ip != proxy_ip:
                result = "exists the improper configuration of Nginx leads to proxy"
                self._output(ip, port, result)                
        except:
            pass

globals()['VulnChecker'] = VulnChecker