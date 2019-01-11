#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Reference: https://github.com/ysrc/xunfeng/blob/master/vulscan/vuldb/phpmyadmin_crackpass.py

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'phpmyadmin_weakpwd'
        self.info = "Check the phpMyAdmin weak password"
        self.keyword = ['all', 'phpmyadmin', 'pma', 'weak_password', 'intranet', 'danger', 'web']
        self.default_ports_list = WEB_PORTS_LIST
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        flag_list = ['src="navigation.php', 'frameborder="0" id="frame_content"', 'id="li_server_type">',
                     'class="disableAjax" title=']
        user_list = ['root', 'mysql', 'admin', 'test']
        pass_list = ['root', 'root123', '123456', 'test', 'test123', '12345678', '{user}', '{user}123', '{user}1234', 'qwer1234', '',]
        user_list = user_list if len(USER_LIST) == 0 else USER_LIST
        pass_list = pass_list if len(PASS_LIST) == 0 else PASS_LIST
        error_i = 0
        try:
            res_html = urllib2.urlopen('http://' + ip + ":" + str(port), timeout=timeout).read()
            if 'input_password' in res_html and 'name="token"' in res_html:
                url = 'http://' + ip + ":" + str(port) + "/index.php"
            else:
                res_html = urllib2.urlopen('http://' + ip + ":" + str(port) + "/phpmyadmin", timeout=timeout).read()
                if 'input_password' in res_html and 'name="token"' in res_html:
                    url = 'http://' + ip + ":" + str(port) + "/phpmyadmin/index.php"
                else:
                    return
        except:
            pass
        for user in user_list:
            for password in pass_list:
                try:
                    password = str(password.replace('{user}', user))
                    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
                    res_html = opener.open(url, timeout=timeout).read()
                    token = re.search('name="token" value="(.*?)" />', res_html)
                    token_hash = urllib2.quote(token.group(1))
                    postdata = "pma_username=%s&pma_password=%s&server=1&target=index.php&lang=zh_CN&collation_connection=utf8_general_ci&token=%s" % (user, password, token_hash)
                    res = opener.open(url,postdata, timeout=timeout)
                    res_html = res.read()
                    for flag in flag_list:
                        if flag in res_html:
                            self._output(ip, port, 'exists phpMyAdmin weak password, user: %s pwd: %s'%(user, password))
                            return
                except urllib2.URLError:
                    error_i += 1
                    if error_i >= 3: return
                except:
                    return

globals()['VulnChecker'] = VulnChecker