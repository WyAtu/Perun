#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Reference: https://github.com/ysrc/xunfeng/blob/master/vulscan/vuldb/crack_mysql.py

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'mysql_weakpwd'
        self.info = "Check the MySQL weak password"
        self.keyword = ['all', 'mysql', 'db', 'database', 'weak_password', 'danger', 'intranet', '3306']
        self.default_ports_list = [3306,]
        VulnCheck.__init__(self, ip_and_port_list)

    def get_hash(self, password, scramble):
        hash_stage1 = hashlib.sha1(password).digest()
        hash_stage2 = hashlib.sha1(hash_stage1).digest()
        to = hashlib.sha1(scramble + hash_stage2).digest()
        reply = [ord(h1) ^ ord(h3) for (h1, h3) in zip(hash_stage1, to)]
        hash = struct.pack('20B', *reply)
        return hash

    def get_scramble(self, packet):
        tmp = packet[15:]
        m = re.findall("\x00?([\x01-\x7F]{7,})\x00", tmp)
        if len(m) > 3: del m[0]
        scramble = m[0] + m[1]
        try:
            plugin = m[2]
        except:
            plugin = ''
        return plugin, scramble

    def get_auth_data(self, user, password, scramble, plugin):
        user_hex = binascii.b2a_hex(user)
        pass_hex = binascii.b2a_hex(self.get_hash(password, scramble))
        if not password:
            data = "85a23f0000000040080000000000000000000000000000000000000000000000" + user_hex + "0000"
        else:
            data = "85a23f0000000040080000000000000000000000000000000000000000000000" + user_hex + "0014" + pass_hex
        if plugin: data += binascii.b2a_hex(
            plugin) + "0055035f6f73076f737831302e380c5f636c69656e745f6e616d65086c69626d7973716c045f7069640539323330360f5f636c69656e745f76657273696f6e06352e362e3231095f706c6174666f726d067838365f3634"
        len_hex = hex(len(data) / 2).replace("0x", "")
        auth_data = len_hex + "000001" + data
        return binascii.a2b_hex(auth_data)

    def _check(self, ip, port):
        socket.setdefaulttimeout(timeout)
        pass_list = ['', 'root', '{user}', '{user}123', '{user}1234', '{user}123456', '{user}12345', '{user}@123', '{user}@123456', '{user}@12345', '{user}#123', '{user}#123456', '{user}#12345', '{user}_123', '{user}_123456', '{user}_12345', '{user}123!@#', '{user}!@#$', '{user}!@#', '{user}~!@', '{user}!@#123', 'qweasdzxc', '{user}2019', '{user}2018', '{user}2017', '{user}2016', '{user}2015', '{user}@2019', '{user}@2018', '{user}@2017', '{user}@2016', '{user}@2015', 'Passw0rd', 'admin123', 'admin888', 'administrator', 'administrator123', 'qwerty', 'test', '1q2w3e4r', '1qaz2wsx', 'qazwsx', '123qwe', '123qaz', '123456qwerty', 'password123', '1q2w3e', 'okmnji', 'test123', 'test12345', 'test123456', 'q1w2e3r4', 'mysql', 'web', 'null', '123', '1234', '12345', '123456', 'admin', 'pass', 'password', '!null!', '!user!', '1234567', '7654321', 'abc123', '111111', '123321', '123123', '12345678', '123456789', '000000', '888888', '654321', '987654321', '147258369', '123asd', 'qwer123', 'P@ssw0rd', '{user}3306']
        user_list = ['root'] if len(USER_LIST) == 0 else USER_LIST
        pass_list = pass_list if len(PASS_LIST) == 0 else PASS_LIST
        for user in user_list:
            for pass_ in pass_list:
                try:
                    pass_ = str(pass_.replace('{user}', user))
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.connect((ip, int(port)))
                    packet = sock.recv(254)
                    # print packet
                    plugin, scramble = self.get_scramble(packet)
                    auth_data = self.get_auth_data(user, pass_, scramble, plugin)
                    sock.send(auth_data)
                    result = sock.recv(1024)
                    if result == "\x07\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00":
                        self._output(ip, port, "exits weakpwd, user: %s pwd: %s"%(user, pass_))
                except Exception as e:
                    if "Errno 10061" in str(e) or "timed out" in str(e): return
                    if "list index out of range" in str(e): pass # the user has been blocked

globals()['VulnChecker'] = VulnChecker