#!/usr/bin/env python
# -*- coding:utf-8 -*-

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'git_or_svn_disclosure'
        self.info = "Scan the Git or SVN Disclosure"
        self.keyword = ['all', 'web', 'disclosure', 'leak', 'leakage', 'info', 'git', 'svn', 'scan']
        self.default_ports_list = WEB_PORTS_LIST
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        PAYLOADS = ['/.svn/entries', '/.svn/all-wcprops', '/.git/config']
        url1 = 'http://%s:%s'%(ip, port) if add_web_path == "" else 'http://%s:%s/%s'%(ip, port, add_web_path)
        url2 = 'https://%s:%s'%(ip, port) if add_web_path == "" else 'https://%s:%s/%s'%(ip, port, add_web_path)
        for payload in PAYLOADS:
            try:
                req = Requester(url1+payload)
                if req.code == 200 and check_200_or_404(url1):
                    self._output(ip, port, 'Git or SVN Disclosure: %s'%(url1+payload))
                    return
            except RequesterOpenError:
                try:
                    req = Requester(url2+payload)
                    if req.code == 200 and check_200_or_404(url2):
                        self._output(ip, port, 'Git or SVN Disclosure: %s'%(url1+payload))
                        return
                except:
                    pass
            except:
                pass

globals()['VulnChecker'] = VulnChecker