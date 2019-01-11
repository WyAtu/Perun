#!/usr/bin/env python
# -*- coding:utf-8 -*-

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'jboss_jmxconsole'
        self.info = "Check if the JBoss path /jmx-console/HtmlAdaptor exists for CVE-2006-5750/CVE-2007-1036/CVE-2010-0738"
        self.keyword = ['all', 'jboss', 'rce', 'cve_2005_5750', 'cve_2007_1036', 'cve_2010_0738', 'web', 'intranet', 'danger', '8080']
        self.default_ports_list = WEB_PORTS_LIST
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        result = "Maybe jBoss vuln CVE-2006-5750/CVE-2007-1036/CVE-2010-0738"
        url1 = "http://%s:%d/jmx-console/HtmlAdaptor"%(ip, int(port)) if add_web_path == "" else "http://%s:%d/%s/jmx-console/HtmlAdaptor"%(ip, int(port), add_web_path)
        url2 = "https://%s:%d/jmx-console/HtmlAdaptor"%(ip, int(port)) if add_web_path == "" else "https://%s:%d/%s/jmx-console/HtmlAdaptor"%(ip, int(port), add_web_path)
        try:
            req = Requester(url1, method='HEAD')
            if (req.code == 500 or (req.code == 200 and check_200_or_404(url1))) and ('JBoss'.lower() in req.headers.lower() or 'Apache-Coyote/1.1'.lower() in req.headers.lower()):
                self._output(ip, port, result)
        except RequesterOpenError:
            try:
                req = Requester(url2, method='HEAD')
                if (req.code == 500 or (req.code == 200 and check_200_or_404(url2))) and ('JBoss'.lower() in req.headers.lower() or 'Apache-Coyote/1.1'.lower() in req.headers.lower()):
                    self._output(ip, port, result)
            except:
                pass
        except:
            pass

globals()['VulnChecker'] = VulnChecker