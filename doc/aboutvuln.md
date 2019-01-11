# Perun
[![Python 2.7](https://img.shields.io/badge/python-2.7-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/aur/license/yaourt.svg)](https://github.com/WyAtu/Perun/blob/master/LICENSE) [![Vulns](https://img.shields.io/badge/Vulns/20190111-42-red.svg)](https://github.com/WyAtu/Perun/tree/master/vuln) 

**Perun**是一款主要适用于**乙方安服、渗透测试人员和甲方RedTeam红队人员的网络资产漏洞扫描器/扫描框架**，它主要适用于**内网环境**，加载漏洞检测Vuln模块后能够快速发现安全问题，并根据需要生成报表，以方便安全人员对授权项目完成测试工作。

**Perun**由Python2.7和Python标准库开发，所有功能(端口扫描，漏洞检测，控制台输出，生成Html报告)兼容Windows系统和\*nix系统，Html报告采用Vue+Element，**支持对扫描结果的排序、搜索、分页**。

**在内网环境中只需上传Perun的启动器文件**(未安装Python的主机环境下可以使用Pyinstaller[打包](https://github.com/WyAtu/Perun/tree/master/doc/package2exe#%E6%89%93%E5%8C%85perun%E4%BA%8C%E8%BF%9B%E5%88%B6%E6%96%87%E4%BB%B6)生成的单个控制台exe二进制启动器文件，大小在3-5M)，其余文件可以部署在云端，也可以部署在目标内网中，**既可用作普通的端口扫描器，又可用作漏洞扫描器**，方便安全人员在内网环境中进行工作。

## 支持的Vuln模块

**Perun**目前支持42个Vuln模块

| Vuln模块名 | Vuln模块说明信息 |
| ------ | ------ |
| activemq.activemq_weakpwd | 检测ActiveMQ弱口令 |
| activemq.activemq_upload | 检测ActiveMQ任意文件上传漏洞(CVE-2016-3088) |
| axis2.axis2_file_read | 检测Axis2任意文件读取漏洞 |
| docker.docker_unauth | 检测Docker未授权访问漏洞 |
| elasticsearch.rce_cve20143120 | 检测Elasticsearch远程代码执行漏洞(CVE-2014-3120) |
| elasticsearch.rce_cve20151427 | 检测Elasticsearch远程代码执行漏洞(CVE-2015-1427) |
| elasticsearch.read_cve20153337 | 检测Elasticsearch任意文件读取漏洞(CVE-2015-3337) |
| elasticsearch.read_cve20155531 | 检测Elasticsearch任意文件读取漏洞(CVE-2015-5531) |
| ftp.ftp_weakpwd | 检测FTP弱口令 |
| glassfish.glassfish_file_read | 检测Glassfish任意文件读取漏洞 |
| iis.iis_webdav_put | 检测IIS WebDav PUT任意文件上传漏洞 |
| iis.iis_webdav_rce | 检测IIS WebDav远程命令执行漏洞(CVE-2017-7269) |
| javarmi.javarmi_rce | 检测Java RMI远程命令执行漏洞 |
| jboss.jboss_readonly | 检测是否存在JBoss路径/invoker/readonly，路径存在即可能存在漏洞CVE-2017-12149 |
| jboss.jboss_jmxconsole | 检测是否存在JBoss路径/jmx-console/HtmlAdaptor，路径存在即可能存在漏洞CVE-2006-5750/CVE-2007-1036/CVE-2010-0738 |
| jboss.jboss_webconsole | 检测是否存在JBoss路径/web-console/Invoker，路径存在即可能存在漏洞CVE-2013-4810 |
| jboss.jboss_adminconsole | 检测是否存在JBoss路径/admin-console/，路径存在即可能存在漏洞CVE-2010-1871 |
| jboss.jboss_jbossmq_httpil | 检测是否存在JBoss路径/jbossmq-httpil/HTTPServerILServlet，路径存在即可能存在漏洞CVE-2017-7504 |
| jboss.jboss_EJBInvokerServlet | 检测是否存在JBoss路径/invoker/EJBInvokerServlet，路径存在即可能存在漏洞CVE-2012-0874/CVE-2013-4810 |
| jboss.jboss_JMXInvokerServlet | 检测是否存在JBoss路径/invoker/JMXInvokerServlet，路径存在即可能存在漏洞CVE-2007-1036/CVE-2012-0874/CVE-2013-4810/CVE-2017-7501 |
| memcache.memcache_unauth | 检测Memcache未授权访问漏洞 |
| mongodb.mongodb_unauth | 检测MongoDB未授权访问漏洞 |
| mysql.mysql_weakpwd | 检测MySQL弱口令 |
| nexus_repository.nexus_weakpwd | 检测Sonatype Nexus Repository Manager弱口令 |
| tomcat.tomcat_put | 检测Tomcat PUT远程命令执行漏洞(CVE-2017-12615) |
| phpmyadmin.phpmyadmin_weakpwd | 检测phpMyAdmin漏洞 |
| phpmyadmin.phpmyadmin_setup_rce | 检测phpMyAdmin Scripts/setup.php远程命令执行漏洞 |
| postgresql.postgresql_weakpwd | 检测PostgresSQL弱口令 |
| redis.redis_weakpwd_unauth | 检测Redis弱口令和未授权访问漏洞 |
| rsync.rsync_weakpwd_unauth | 检测Rsync弱口令和未授权访问漏洞 |
| smb_netbios.computer_info | 获取主机信息，如主机名/域名/操作系统信息，类似于nbtscan |
| smb_netbios.ms17_010 | 检测MS17-010远程命令执行漏洞 |
| thinkphp.thinkphp5_rce | 检测ThinkPHP5.*远程代码执行漏洞 |
| thinkphp.thinkphp5023_rce | 检测ThinkPHP5.0.*(在5.0.23上测试)远程代码执行漏洞 |
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
