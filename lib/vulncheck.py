#!/usr/bin/env python
# -*- coding:utf-8 -*-

class VulnCheck():
    def __init__(self, ip_and_port_list):
        #self._name = 'vuln_name'
        #self.info = 'vuln_info'
        #self.default_ports_list = [80, 443]
        #self.keyword = ['a', 'b', 'danger'] # danger means it may be remote code/command execution, file upload(deploy webshell), deserialization, etc.
        self.target_ip_and_port_list = ip_and_port_list

    def start(self):
        if self.target_ip_and_port_list is not []:

            self.thread_list = []
            self._make_ip_port_list(self.target_ip_and_port_list)
            if len(self.ip_and_port_list):
                PrintConsole('Start to check vuln %s'%(self._name), 'info') 
                self._make_queue()
                for i in range(thread):
                    self._start_thread()
                self._check_exit()

    def _make_ip_port_list(self, ip_and_port_list):
        self.ip_and_port_list = []
        tmp_ip_and_port_list = []
        for _ in ip_and_port_list:
            if int(_.split(':')[1]) == 0:
                ip = str(_.split(':')[0])
                for port in self.default_ports_list:
                    tmp_ip_and_port_list.append("%s:%d"%(ip, int(port)))
                self.ip_and_port_list = tmp_ip_and_port_list
            else:
                self.ip_and_port_list = ip_and_port_list

        self.ip_and_port_list = list((set(self.ip_and_port_list).union(set(IP_OPEN_PORT)))^(set(self.ip_and_port_list)^set(IP_OPEN_PORT)))

    def _make_queue(self):
        self.q = Queue()
        map(lambda x: self.q.put(x), self.ip_and_port_list)

    def _start_thread(self):
        while not self.q.empty():
            try:
                ip, port = self.q.get(block = True, timeout = 1).split(':')
                self._make_thread(ip, port)
                self.q.task_done()
            except Exception as e:
                pass

    def _make_thread(self, ip, port):
        t = threading.Thread(target=self._check, args=(ip, int(port)))
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

    def _output(self, ip, port, more_info=""):
        PrintConsole('Vuln %s found: %s:%d %s'%(self._name, ip, int(port), more_info), 'right')
        VULN_SCAN_RESULT_LIST.append({'vuln_name' : self._name, 'ip' : ip, 'port' : int(port), 'more_info' : more_info})

    def _check(self, ip, port):
        # if True:
        #     self._output(ip, port)
        pass

globals()['VulnCheck'] = VulnCheck