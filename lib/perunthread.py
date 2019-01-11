#!/usr/bin/env python
# -*- coding:utf-8 -*-

class PerunThread(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q

    def run(self):
        while not self.q.empty():
            try:
                ip, port = self.q.get(block = True, timeout = 1).split(':')
                process_port_scan(ip, int(port))
                self.q.task_done()
            except:
                pass

globals()['PerunThread'] = PerunThread