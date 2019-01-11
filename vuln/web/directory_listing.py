#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Reference: https://github.com/ydhcui/Scanver/blob/master/payloads/httpinfo.py

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'directory_listing'
        self.info = "Scan the Directory Listing"
        self.keyword = ['all', 'web', 'directory', 'dir', 'listing', 'scan']
        self.default_ports_list = WEB_PORTS_LIST
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        PAYLOADS = (
            re.compile(r'<title>Index of /',re.I),
            re.compile(r'<a href="?C=N;O=D">Name</a>',re.I),
            re.compile(r'<A HREF="?M=A">Last modified</A>',re.I),
            re.compile(r'Last modified</a>',re.I),
            re.compile(r'Parent Directory</a>',re.I),
            re.compile(r'<TITLE>Folder Listing.',re.I),
            re.compile(r'<table summary="Directory Listing',re.I),
            re.compile(r'">[To Parent Directory]</a><br><br>',re.I),
            re.compile(r'&lt;dir&gt; <A HREF="/',re.I),
            re.compile(r'''<pre><A HREF="/">\[''',re.I),
        )
        url1 = 'http://%s:%s'%(ip, port) if add_web_path == "" else 'http://%s:%s/%s'%(ip, port, add_web_path)
        url2 = 'https://%s:%s'%(ip, port) if add_web_path == "" else 'https://%s:%s/%s'%(ip, port, add_web_path)
        try:
            req = Requester(url1)
            for payload in PAYLOADS:
                r = payload.findall(req.html)
                if r:
                    self._output(ip, port, 'Directory Listing: %s'%(url1))
                    return
        except RequesterOpenError:
            try:
                req = Requester(url2)
                for payload in PAYLOADS:
                    r = payload.findall(req.html)
                    if r:
                        self._output(ip, port, 'Directory Listing: %s'%(url2))
                        return
            except:
                pass
        except:
            pass

globals()['VulnChecker'] = VulnChecker