#!/usr/bin/env python
# -*- coding:utf-8 -*-

class MakePortsList():
    def __init__(self, target):
        self.target = []
        map(self._get_ports_list_from_target, target)

    def _get_ports_list_from_target(self, target):
        if '-' in target:
            self.target = list(set(self.target + get_ports_list_by_a2b(target)))
        else:
            self.target = list(set(self.target + get_ports_list_by_port(target)))

globals()['MakePortsList'] = MakePortsList