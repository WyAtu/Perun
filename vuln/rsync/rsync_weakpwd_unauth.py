#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Reference: https://github.com/ysrc/xunfeng/blob/master/vulscan/vuldb/rsync_weak_auth.py


class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'rsync_weakpwd_unauth'
        self.info = "Check the Rsync weak password and unauthorized access"
        self.keyword = ['all', 'rsync', 'unauth', 'weak_password', 'intranet', '873', '1873',]
        self.default_ports_list = [873, 1873,]
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        info = ''
        not_unauth_list = []
        weak_auth_list = []
        userlist = ['test', 'root', 'www', 'web', 'rsync', 'admin']
        passwdlist = ['test', 'root', 'password', 'p@aaw0rd', 'abc123!', '123456', 'admin', 'admin123', '',]
        userlist = userlist if len(USER_LIST) == 0 else USER_LIST
        passwdlist = passwdlist if len(PASS_LIST) == 0 else PASS_LIST
        try:
            rwc = RsyncWeakCheck(ip, port)
            for path_name in rwc.get_all_pathname():
                ret = rwc.is_path_not_auth(path_name)
                if ret == 0:
                    not_unauth_list.append(path_name)
                elif ret == 1:
                    for username, passwd in product(userlist, passwdlist):
                        try:
                            res = rwc.weak_passwd_check(path_name, username, passwd)
                            if res:
                                weak_auth_list.append((path_name, username, passwd))
                        except VersionNotSuppError as e:
                            # TODO fengxun error support
                            pass
        except:
            pass

        if not_unauth_list:
            info += u'unauth directory: [%s]'%(",".join(not_unauth_list))
        if weak_auth_list:
            for weak_auth in weak_auth_list:
                info += u'directory %s weak password: %s:%s;'%(weak_auth)
        if info:
            self._output(ip, port, info)

class ReqNoUnderstandError(Exception):
    def __init__(self):
        super(Exception, self).__init__(self)


class VersionNotSuppError(Exception):
    '''\
    版本不支持错误,当前Rsync协议常见有三个版本，
    目前来看还不能支持小于版本30的用户登录逻辑
    如果你对该版本29的登录过程有兴趣，可以参考：
    https://git.samba.org/rsync.git/?p=rsync.git;a=blob;f=authenticate.c;h=5370cb781fd8c73f09f1e9a25fd91095f86dd1c6;hb=0c6d79528ac651ef064173327d769ba7a2b338ab#l224
    欢迎讨论
    '''
    def __init__(self):
        super(Exception, self).__init__(self)


class RsyncWeakCheck(object):
    """用于检测Rsync弱口令和弱验证 beta0.1 @Nearg1e"""

    # '.'
    _list_request = ('''
    0a
    ''').replace(' ', '').replace('\n', '').decode('hex')

    # '@RSYNCD: 29\n'
    _hello_request = '@RSYNCD: 31\n'

    def __init__(self, host='', port=0, timeout=5):
        super(RsyncWeakCheck, self).__init__()
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = None


    def _rsync_init(self):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(self.timeout)
        sock.connect((self.host,self.port))
        sock.send(self._hello_request)
        res = sock.recv(1024)
        self.sock = sock
        return res


    def is_path_not_auth(self, path_name = ''):
        '''\
        验证某一目录是否可以被未授权访问
        >>> result = is_path_not_auth('nearg1e')
        0 # 无需登录可未授权访问
        1 # 需要密码信息进行登录
        -1 # 出现了rsync的error信息无法读取
        raisee ReqNoUnderstandError # 出现了本喵=0v0=无法预料的错误
        '''
        self._rsync_init()
        payload = path_name + '\n'
        self.sock.send(payload)
        result = self.sock.recv(1024)
        if result == '\n':
            result = self.sock.recv(1024)
        if result.startswith('@RSYNCD: OK'):
            return 0
        if result.startswith('@RSYNCD: AUTHREQD'):
            return 1
        if '@ERROR: chdir failed' in result:
            return -1
        else:
            raise ReqNoUnderstandError()


    def get_all_pathname(self):
        self._rsync_init()
        self.sock.send(self._list_request)
        sleep(0.5)
        result = self.sock.recv(1024)
        if result:
            for path_name in re.split('\n', result):
                if path_name and not path_name.startswith('@RSYNCD: '):
                    yield path_name.split('\t')[0].strip()

    def weak_passwd_check(self, path_name='', username='', passwd=''):
        ver_string = self._rsync_init()
        if self._get_ver_num(ver_string=ver_string) < 30:
            # print('Error info:', ver_string)
            raise VersionNotSuppError()
        payload = path_name + '\n'
        self.sock.send(payload)
        result = self.sock.recv(1024)
        if result == '\n':
            result = self.sock.recv(1024)
        if result:
            hash_o = hashlib.md5()
            hash_o.update(passwd)
            hash_o.update(result[18:].rstrip('\n'))
            auth_string = base64.b64encode(hash_o.digest())
            send_data = username + ' ' + auth_string.rstrip('==') + '\n'
            self.sock.send(send_data)
            res = self.sock.recv(1024)
            if res.startswith('@RSYNCD: OK'):
                return (True, username, passwd)
            else:
                return False


    def _get_ver_num(self, ver_string=''):
        if ver_string:
            ver_num_com = re.compile('@RSYNCD: (\d+)')
            ver_num = ver_num_com.match(ver_string).group(1)
            if ver_num.isdigit():
                return int(ver_num)
            else: return 0
        else:
            return 0

#globals()['hex2str'] = hex2str
globals()['VulnChecker'] = VulnChecker
globals()['RsyncWeakCheck'] = RsyncWeakCheck
globals()['VersionNotSuppError'] = VersionNotSuppError
globals()['ReqNoUnderstandError'] = ReqNoUnderstandError