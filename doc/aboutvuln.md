# 关于Vuln模块

## 支持的Vuln模块

**Perun**目前支持54个Vuln模块

| Vuln模块名 | Vuln模块说明信息 |
| ------ | ------ |
| activemq.activemq_weakpwd | 检测ActiveMQ弱口令 |
| activemq.activemq_upload | 检测ActiveMQ任意文件上传漏洞(CVE-2016-3088) |
| axis2.axis2_file_read | 检测Axis2任意文件读取漏洞 |
| cerio.cerio_auth_rce | 检测CERIO路由器认证后的RCE漏洞(CVE-2018-18852) |
| docker.docker_unauth | 检测Docker未授权访问漏洞 |
| elasticsearch.rce_cve20143120 | 检测Elasticsearch远程代码执行漏洞(CVE-2014-3120) |
| elasticsearch.rce_cve20151427 | 检测Elasticsearch远程代码执行漏洞(CVE-2015-1427) |
| elasticsearch.read_cve20153337 | 检测Elasticsearch任意文件读取漏洞(CVE-2015-3337) |
| elasticsearch.read_cve20155531 | 检测Elasticsearch任意文件读取漏洞(CVE-2015-5531) |
| ftp.ftp_weakpwd | 检测FTP弱口令 |
| glassfish.glassfish_file_read | 检测Glassfish任意文件读取漏洞 |
| glassfish.glassfish_weakpwd | 检测Glassfis弱口令 |
| grafana.grafana_weakpwd | 检测Grafana弱口令 |
| iis.iis_webdav_put | 检测IIS WebDav PUT任意文件上传漏洞 |
| iis.iis_webdav_rce | 检测IIS WebDav远程命令执行漏洞(CVE-2017-7269) |
| iis.short_filename | 检测IIS短文件名漏洞 |
| javarmi.javarmi_rce | 检测Java RMI远程命令执行漏洞 |
| jboss.jboss_readonly | 检测是否存在JBoss路径/invoker/readonly，路径存在即可能存在漏洞CVE-2017-12149 |
| jboss.jboss_jmxconsole | 检测是否存在JBoss路径/jmx-console/HtmlAdaptor，路径存在即可能存在漏洞CVE-2006-5750/CVE-2007-1036/CVE-2010-0738 |
| jboss.jboss_webconsole | 检测是否存在JBoss路径/web-console/Invoker，路径存在即可能存在漏洞CVE-2013-4810 |
| jboss.jboss_adminconsole | 检测是否存在JBoss路径/admin-console/，路径存在即可能存在漏洞CVE-2010-1871 |
| jboss.jboss_jbossmq_httpil | 检测是否存在JBoss路径/jbossmq-httpil/HTTPServerILServlet，路径存在即可能存在漏洞CVE-2017-7504 |
| jboss.jboss_EJBInvokerServlet | 检测是否存在JBoss路径/invoker/EJBInvokerServlet，路径存在即可能存在漏洞CVE-2012-0874/CVE-2013-4810 |
| jboss.jboss_JMXInvokerServlet | 检测是否存在JBoss路径/invoker/JMXInvokerServlet，路径存在即可能存在漏洞CVE-2007-1036/CVE-2012-0874/CVE-2013-4810/CVE-2017-7501 |
| jenkins.unauth2rce | 检测Jenkins pre-auth 远程命令执行漏洞 |
| jenkins.user_enumeration | 检测Jenkins用户名枚举漏洞 |
| memcache.memcache_unauth | 检测Memcache未授权访问漏洞 |
| mikrotik.winbox_cve_2018_14847 | 检测MikroTik RouterOS Winbox未经身份验证的任意文件读/写漏洞(CVE-2018-14847) |
| mongodb.mongodb_unauth | 检测MongoDB未授权访问漏洞 |
| mysql.mysql_weakpwd | 检测MySQL弱口令 |
| mssql.mssql_weakpwd | 检测MSSQL弱口令 |
| nexus_repository.nexus_weakpwd | 检测Sonatype Nexus Repository Manager弱口令 |
| nginx.nginx_httproxy | 检测Nginx配置不当导致正向代理 |
| tomcat.tomcat_put | 检测Tomcat PUT远程命令执行漏洞(CVE-2017-12615) |
| phpmyadmin.phpmyadmin_weakpwd | 检测phpMyAdmin漏洞 |
| phpmyadmin.phpmyadmin_setup_rce | 检测phpMyAdmin Scripts/setup.php远程命令执行漏洞 |
| postgresql.postgresql_weakpwd | 检测PostgresSQL弱口令 |
| redis.redis_weakpwd_unauth | 检测Redis弱口令和未授权访问漏洞 |
| rsync.rsync_weakpwd_unauth | 检测Rsync弱口令和未授权访问漏洞 |
| smb_netbios.computer_info | 获取主机信息，如主机名/域名/操作系统信息，类似于nbtscan |
| smb_netbios.ms17_010 | 检测MS17-010远程命令执行漏洞 |
| smb_netbios.new_ms17_010 | 检测MS17-010远程命令执行漏洞新版本 |
| thinkphp.thinkphp5_rce | 检测ThinkPHP 5.* 远程代码执行漏洞 |
| thinkphp.thinkphp5010_rce | 检测ThinkPHP 5.0.*(低于5.0.10) 远程代码执行漏洞 |
| thinkphp.thinkphp5023_rce | 检测ThinkPHP 5.0.*(低于5.0.23) 远程代码执行漏洞 |
| thinkphp.thinkphp5152_rce | 检测ThinkPHP 5.1.\*/5.2.\*(5.1.x - 5.1.31, 5.2.0beta1) 远程代码执行漏洞 |
| web.directory_listing | 扫描列目录漏洞 |
| web.git_or_svn_disclosure | 扫描Git和SVN源码泄露漏洞 |
| web.web_sensitive | 扫描敏感文件和目录 |
| weblogic.rce_cve201710271 | 检测WebLogic WLS远程命令执行漏洞(CVE-2017-10271) |
| weblogic.rce_cve20182628 | 检测WebLogic WLS远程命令执行漏洞(CVE-2018-2628) |
| weblogic.ssrf_cve20144210 | 检测WebLogic SSRF漏洞(CVE-2014-4210) |
| zabbix.zabbix_weakpwd | 检测Zabbix弱口令 |
| zookeeper.zookeeper_unauth | 检测Zookeeper未授权访问 |

## 自定义Vuln模块

Vuln模块目录在[Perun/vuln](https://github.com/WyAtu/Perun/tree/master/vuln)下

自定义Vuln模块非常简单，只需要按以下格式编写即可

``` Python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'vuln_name'                                          # Vuln模块名，应当和文件名相同(不包括文件后缀)
        self.info = "Vuln info"                                           # Vuln说明信息
        self.keyword = ['all', 'morekeyword', ...]                        # Vuln的关键词，用于搜索使用
        self.default_ports_list = ['default_portA', 'default_portB', ...] # Vuln的默认端口，指定为Web端口使用WEB_PORTS_LIST
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        ...                                                               # 检测代码         
        if True:                                                          # 设置判断条件
            self._output(ip, port)                                        # 满足判断条件，输出结果，并保存到结果列表中

globals()['VulnChecker'] = VulnChecker
```

编写测试完成后，在[Perun/conf/globallistconf.py](https://github.com/WyAtu/Perun/tree/master/conf/globallistconf.py)文件VULN_CHECK_LIST列表中添加该模块，如需要新导入Python库，在[Perun/conf/loadmoduleconf.py](https://github.com/WyAtu/Perun/tree/master/conf/loadmoduleconf.py)文件中导入并注册为全局变量即可

自定义Vuln模块举例:

``` Python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'git_or_svn_disclosure'
        self.info = "Scan the Git or SVN Disclosure"
        self.keyword = ['all', 'web', 'disclosure', 'leak', 'leakage', 'info', 'git', 'svn', 'scan']
        self.default_ports_list = WEB_PORTS_LIST
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        PAYLOADS = ['/.svn/entries', '/.svn/all-wcprops', '/.git/config']
        url1 = 'http://%s:%s'%(ip, port) if add_web_path == "" else 'http://%s:%s/%s'%(ip, port, add_web_path)
        url2 = 'https://%s:%s'%(ip, port) if add_web_path == "" else 'https://%s:%s/%s'%(ip, port, add_web_path)
        for payload in PAYLOADS:
            try:
                req = Requester(url1+payload)
                if req.code == 200 and check_200_or_404(url1):
                    self._output(ip, port, 'Git or SVN Disclosure: %s'%(url1+payload))
                    return
            except RequesterOpenError:
                try:
                    req = Requester(url2+payload)
                    if req.code == 200 and check_200_or_404(url2):
                        self._output(ip, port, 'Git or SVN Disclosure: %s'%(url1+payload))
                        return
                except:
                    pass
            except:
                pass

globals()['VulnChecker'] = VulnChecker
```

**欢迎编写并提交更多自定义模块，直接pr或者发到邮箱wyatu[@]foxmail.com**
