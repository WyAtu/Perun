#!/usr/bin/env python
# -*- coding:utf-8 -*-
#

class MakeStartThread():
    def __init__(self, queue):
        self.thread_list = []
        self._start_thread(queue)

    def _lambda(self, queue):
        t = PerunThread(queue)
        t.setDaemon(True)
        t.start()
        self.thread_list.append(t)

    def _start_thread(self, queue):
        map(self._lambda, [queue for i in range(thread)])
        while 1:
            alive = False
            for t in self.thread_list:
                alive = alive or t.isAlive()
            if not alive: break

globals()['MakeStartThread'] = MakeStartThread