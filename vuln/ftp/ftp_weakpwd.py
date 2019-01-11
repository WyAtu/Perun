#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Reference: https://github.com/ysrc/xunfeng/blob/master/vulscan/vuldb/crack_ftp.py

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'ftp_weakpwd'
        self.info = "Check the FTP weak password"
        self.keyword = ['all', 'ftp','weak_password', '21']
        self.default_ports_list = [21,]
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        user_list = ['ftp', 'www', 'admin', 'root', 'db', 'wwwroot', 'data', 'web']
        pass_list = ['', 'admin', 'Passw0rd', 'postgres', '{user}', '{user}123', '{user}1234', '{user}123456', '{user}12345', '{user}@123', '{user}@123456', '{user}@12345', '{user}#123', '{user}#123456', '{user}#12345', '{user}_123', '{user}_123456', '{user}_12345', '{user}123!@#', '{user}!@#$', '{user}!@#', '{user}~!@', '{user}!@#123', 'qweasdzxc', '{user}2019', '{user}2018', '{user}2017', '{user}2016', '{user}2015', '{user}@2019', '{user}@2018', '{user}@2017', '{user}@2016', '{user}@2015', 'admin123', 'admin888', 'administrator', 'administrator123', 'root123', 'ftp', 'ftppass', '123456', 'password', '12345', '1234', 'root', '123', 'qwerty', 'test', '1q2w3e4r', '1qaz2wsx', 'qazwsx', '123qwe', '123qaz', '0000', 'oracle', '1234567', '123456qwerty', 'password123', '12345678', '1q2w3e', 'abc123', 'okmnji', 'test123', '123456789', 'q1w2e3r4', 'user', 'web']
        user_list = user_list if len(USER_LIST) == 0 else USER_LIST
        pass_list = pass_list if len(PASS_LIST) == 0 else PASS_LIST
        for user in user_list:
            for pass_ in pass_list:
                pass_ = str(pass_.replace('{user}', user))
                try:
                    ftp = ftplib.FTP()
                    ftp.timeout = timeout
                    ftp.connect(ip, port)
                    ftp.login(user, pass_)
                    if pass_ == '': pass_ = "null"
                    self._output(ip, port, 'exits FTP weak password, user: %s pwd: %s'%(user, pass_))
                    return
                except Exception as e:
                    if "Errno 10061" in str(e) or "timed out" in str(e): return

globals()['VulnChecker'] = VulnChecker