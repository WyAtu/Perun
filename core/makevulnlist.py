#!/usr/bin/env python
# -*- coding:utf-8 -*-

class MakeVulnList():
    def __init__(self, target):
        map(self._get_vuln_ports_list_from_target, target)
        check_vuln_valid()

    def _get_vuln_ports_list_from_target(self, target):
        _ = target.split('=')
        if len(_) == 1:
            vuln_name = _[0]
            vuln_ports_list = [0,]
            
        elif len(_) == 2:
            vuln_name = _[0]
            vuln_ports_list = MakePortsList(get_ports_list_from_input(_[1].split(' '))).target
        else: PrintConsole('The vuln selected error', 'error')
        VULN_INPUT_LIST.append({'vuln_name' : vuln_name, 'vuln_ports_list' : vuln_ports_list})

globals()['MakeVulnList'] = MakeVulnList