#!/usr/bin/env python
# -*- coding:utf-8 -*-
# this module is abandoned

class DnsChecker():
    # check_str = DnsChecker().make_record(ip)
    # local_ip = DnsChecker().get_local_ip()
    # ... nslookup check_str local_ip ...
    # ... dig @local_ip check_str ...
    def dns_start(self):
        t = threading.Thread(target=self.dns_work)
        t.setDaemon(True)
        t.start()

    def dns_work(self):
        try:
            dns_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            dns_server.bind(('0.0.0.0',53))
            dns_server.settimeout(5.0)
            PrintConsole('Start to listen on port 53 to receive DNS request')
        except:
            PrintConsole('Failed to listen on port 53 to receive DNS request')
            pass

        while 1:
            try:
                recv, addr = dns_server.recvfrom(1024)
                print DNS_HISTORY_RECORD
                if recv not in DNS_HISTORY_RECORD:
                    DNS_HISTORY_RECORD.append(recv)
                    PrintConsole('Received a dns request from %s'%(str(addr[0])), 'right')
            except:
                pass

    def make_record(self, ip):
        return ("%s.%s.%s"%(str(ip), str(time()), random8string())).replace('.', '_')

    def get_local_ip(self, ip):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((ip, 80))
            local_ip, _ = s.getsockname()
            s.close()
            return str(local_ip)
        except:
            PrintConsole('Failed to get local ip', 'error')

    def check_record(self, record):
        global DNS_HISTORY_RECORD
        record_flag = 0
        tmp_DNS_HISTORY_RECORD = DNS_HISTORY_RECORD[:]
        for _ in DNS_HISTORY_RECORD:
            if record in _:
                record_flag = 1
                tmp_DNS_HISTORY_RECORD.remove(_)
        DNS_HISTORY_RECORD = tmp_DNS_HISTORY_RECORD
        return record_flag

globals()['DnsChecker'] = DnsChecker