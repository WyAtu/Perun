#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Reference: https://github.com/ysrc/xunfeng/blob/master/vulscan/vuldb/crack_postgres.py

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'postgresql_weakpwd'
        self.info = "Check the PostgresSQL weak password"
        self.keyword = ['all', 'postgresql', 'postsql', 'weak_password', 'db', 'database', 'danger', 'intranet', '5432']
        self.default_ports_list = [5432,]
        VulnCheck.__init__(self, ip_and_port_list)

    def make_response(self, username, password, salt):
        pu = hashlib.md5(password + username).hexdigest()
        buf = hashlib.md5(pu + salt).hexdigest()
        return 'md5' + buf

    def auth(self, host, port, username, password):
        try:
            socket.setdefaulttimeout(timeout)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            packet_length = len(username) + 7 + len(
                "\x03user  database postgres application_name psql client_encoding UTF8  ")
            p = "%c%c%c%c%c\x03%c%cuser%c%s%cdatabase%cpostgres%capplication_name%cpsql%cclient_encoding%cUTF8%c%c" % (
            0, 0, 0, packet_length, 0, 0, 0, 0, username, 0, 0, 0, 0, 0, 0, 0, 0)
            sock.send(p)
            packet = sock.recv(1024)
            if packet[0] == 'R':
                authentication_type = str([packet[8]])
                c = int(authentication_type[4:6], 16)
                if c == 5: salt = packet[9:]
            else:
                return 3
            lmd5 = self.make_response(username, password, salt)
            packet_length1 = len(lmd5) + 5 + len('p')
            pp = 'p%c%c%c%c%s%c' % (0, 0, 0, packet_length1 - 1, lmd5, 0)
            sock.send(pp)
            packet1 = sock.recv(1024)
            if packet1[0] == "R":
                return True
        except Exception, e:
            if "Errno 10061" in str(e) or "timed out" in str(e): return 3

    def _check(self, ip, port):
        pass_list = ['admin', 'Passw0rd', 'postgres', '{user}', '{user}123', '{user}1234', '{user}123456', '{user}12345', '{user}@123', '{user}@123456', '{user}@12345', '{user}#123', '{user}#123456', '{user}#12345', '{user}_123', '{user}_123456', '{user}_12345', '{user}123!@#', '{user}!@#$', '{user}!@#', '{user}~!@', '{user}!@#123', 'qweasdzxc', '{user}2019', '{user}2018', '{user}2017', '{user}2016', '{user}2015', '{user}@2019', '{user}@2018', '{user}@2017', '{user}@2016', '{user}@2015', 'admin123', 'admin888', 'administrator', 'administrator123', 'root123', 'ftp', 'ftppass', '123456', 'password', '12345', '1234', 'root', '123', 'qwerty', 'test', '1q2w3e4r', '1qaz2wsx', 'qazwsx', '123qwe', '123qaz', '0000', 'oracle', '1234567', '123456qwerty', 'password123', '12345678', '1q2w3e', 'abc123', 'okmnji', 'test123', '123456789', 'q1w2e3r4', 'user', 'web']
        user_list = ['postgres', 'admin'] if len(USER_LIST) == 0 else USER_LIST
        pass_list = pass_list if len(PASS_LIST) == 0 else PASS_LIST
        for user in user_list:
            for pass_ in pass_list:
                try:
                    pass_ = str(pass_.replace('{user}', user))
                    result = self.auth(ip, port, user, pass_)
                    if result == 3: break
                    if result == True:
                        self._output(ip, port, "exits weakpwd, user: %s pwd: %s"%(user, pass_))
                        return
                except:
                    pass

globals()['VulnChecker'] = VulnChecker