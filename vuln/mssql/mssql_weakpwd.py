#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Reference: https://github.com/ysrc/xunfeng/blob/master/vulscan/vuldb/crack_mssql.py

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'mssql_weakpwd'
        self.info = "Check the MSSQL weak password"
        self.keyword = ['all', 'mssql', 'db', 'database', 'weak_password', 'danger', 'intranet', '1433']
        self.default_ports_list = [1433,]
        VulnCheck.__init__(self, ip_and_port_list)

    def auth(self, host, port, username, password):
        try:
            socket.setdefaulttimeout(timeout)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            hh = binascii.b2a_hex(host)
            husername = binascii.b2a_hex(username)
            lusername = len(username)
            lpassword = len(password)
            ladd = len(host) + len(str(port)) + 1
            hladd = hex(ladd).replace('0x', '')
            hpwd = binascii.b2a_hex(password)
            pp = binascii.b2a_hex(str(port))
            address = hh + '3a' + pp
            hhost = binascii.b2a_hex(host)
            data = "0200020000000000123456789000000000000000000000000000000000000000000000000000ZZ5440000000000000000000000000000000000000000000000000000000000X3360000000000000000000000000000000000000000000000000000000000Y373933340000000000000000000000000000000000000000000000000000040301060a09010000000002000000000070796d7373716c000000000000000000000000000000000000000000000007123456789000000000000000000000000000000000000000000000000000ZZ3360000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000Y0402000044422d4c6962726172790a00000000000d1175735f656e676c69736800000000000000000000000000000201004c000000000000000000000a000000000000000000000000000069736f5f31000000000000000000000000000000000000000000000000000501353132000000030000000000000000"
            data1 = data.replace(data[16:16 + len(address)], address)
            data2 = data1.replace(data1[78:78 + len(husername)], husername)
            data3 = data2.replace(data2[140:140 + len(hpwd)], hpwd)
            if lusername >= 16:
                data4 = data3.replace('0X', str(hex(lusername)).replace('0x', ''))
            else:
                data4 = data3.replace('X', str(hex(lusername)).replace('0x', ''))
            if lpassword >= 16:
                data5 = data4.replace('0Y', str(hex(lpassword)).replace('0x', ''))
            else:
                data5 = data4.replace('Y', str(hex(lpassword)).replace('0x', ''))
            hladd = hex(ladd).replace('0x', '')
            data6 = data5.replace('ZZ', str(hladd))
            data7 = binascii.a2b_hex(data6)
            sock.send(data7)
            packet = sock.recv(1024)
            if 'master' in packet:
                return True
        except Exception, e:
            pass

    def _check(self, ip, port):
        pass_list = ['', 'admin', '{user}', '{user}123', '{user}1234', '{user}123456', '{user}12345', '{user}@123', '{user}@123456', '{user}@12345', '{user}#123', '{user}#123456', '{user}#12345', '{user}_123', '{user}_123456', '{user}_12345', '{user}123!@#', '{user}!@#$', '{user}!@#', '{user}~!@', '{user}!@#123', 'qweasdzxc', '{user}2017', '{user}2016', '{user}2015', '{user}@2017', '{user}@2016', '{user}@2015', 'Passw0rd', 'qweasdzxc', 'admin123', 'admin888', 'administrator', 'administrator123', 'sa123', 'ftp', 'ftppass', '123456', 'password', '12345', '1234', 'sa', '123', 'qwerty', 'test', '1q2w3e4r', '1qaz2wsx', 'qazwsx', '123qwe', '123qaz', '0000', 'oracle', '1234567', '123456qwerty', 'password123', '12345678', '1q2w3e', 'abc123', 'okmnji', 'test123', '123456789', 'q1w2e3r4', 'sqlpass', 'sql123', 'sqlserver', 'web']
        user_list = ['sa', 'test', 'admin', 'web', 'guest'] if len(USER_LIST) == 0 else USER_LIST
        pass_list = pass_list if len(PASS_LIST) == 0 else PASS_LIST
        for user in user_list:
            for pass_ in pass_list:
                try:
                    print user, pass_
                    pass_ = str(pass_.replace('{user}', user))
                    result = self.auth(ip, port, user, pass_)
                    if result == True:
                        self._output(ip, port, "exits MSSQL weakpwd, user: %s pwd: %s"%(user, pass_))
                        return
                except Exception,e:
                    if "Errno 10061" in str(e) or "timed out" in str(e): return

globals()['VulnChecker'] = VulnChecker