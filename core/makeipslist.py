#!/usr/bin/env python
# -*- coding:utf-8 -*-

class MakeIPsList():
    def __init__(self, target):
        self.target = []
        map(self._get_ips_list_from_target, target)

    def _get_ips_list_from_target(self, target):
    	target = target.replace('http://', '').replace('https://', '').rstrip('/')
        if ':' in target:
            target = target.split(':')[0]
        if exists(target):
            try:
                fp = open(target, 'r+')
                map(self._get_ips_list_from_target, [_ for _ in [_.strip() for _ in fp.readlines()] if _ != ''])
                return
            except:
                try: fp.close()
                except: pass
        if '-' in target:
            self.target = list(set(self.target + get_ips_list_by_a2b(target)))
        elif '/' in target:
            self.target = list(set(self.target + get_ips_list_by_cidr(target)))
        else:
            try: socket.gethostbyname(target)
            except: PrintConsole('Failed to parse the target "%s"'%target, 'error')
            self.target = list(set(self.target + [target, ]))
            #self.target = list(set(self.target + get_ip_by_ip_or_url(target)))

globals()['MakeIPsList'] = MakeIPsList