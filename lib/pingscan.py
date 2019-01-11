#!/usr/bin/env python
# -*- coding:utf-8 -*-

class PingScan():
    def __init__(self, ips_list):
        self.thread_list = []
        self._make_queue(ips_list)
        for i in range(thread):
            self._start_thread()
        self._check_exit()

    def _ping_scan(self, ip):
        if osname == "nt":
            try:
                p=Popen('ping -n 1 ' + ip, stdout=PIPE)
            except:
                PrintConsole('Ping failed, please check the privilege or use --skip-ping to skip ping', 'error')
            if p.stdout.read().find("TTL") != -1: PING_SCAN_RESULT_LIST.append(ip)
        else:
            try:
                p=Popen(['ping','-c 1',ip], stdout=PIPE, stderr=PIPE)

            except: 
                PrintConsole('Ping failed, please check the privilege or use --skip-ping to skip ping', 'error')
            if p.stdout.read().find("1 received") != -1: PING_SCAN_RESULT_LIST.append(ip)

    def _make_queue(self, ips_list):
        self.q = Queue()
        map(lambda x: self.q.put(x), ips_list)

    def _start_thread(self):
        while not self.q.empty():
            try:
                ip = self.q.get(block = True, timeout = 1)
                self._make_thread(ip)
                self.q.task_done()
            except:
                pass

    def _make_thread(self, ip):
        t = threading.Thread(target=self._ping_scan, args=(ip,))
        t.setDaemon(True)
        t.start()
        self.thread_list.append(t)

    def _check_exit(self):
        while 1:
            alive = False
            for t in self.thread_list:
                alive = alive or t.isAlive()
            if not alive:
                break

globals()['PingScan'] = PingScan