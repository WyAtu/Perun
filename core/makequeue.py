#!/usr/bin/env python
# -*- coding:utf-8 -*-

class MakeQueue():
    def __init__(self, ips_list, ports_list):
        self.q = Queue()
        if len(ips_list) * len(ports_list) == 0:
            PrintConsole('Target or port error', 'error')
        self._make_queue(ips_list, ports_list)

    def _make_queue(self, ips_list, ports_list):
        map(lambda x: self.q.put(x), ['%s:%d'%(ip, int(port)) for ip in ips_list for port in ports_list])

globals()['MakeQueue'] = MakeQueue