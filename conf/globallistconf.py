#!/usr/bin/env python
# -*- coding:utf-8 -*-

VULN_CHECK_LIST = [
    # The length is best not to exceed 30 characters
    'activemq.activemq_weakpwd',
    'activemq.activemq_upload',
    'axis2.axis2_file_read',
    'cerio.cerio_auth_rce',
    'docker.docker_unauth',
    'elasticsearch.rce_cve20143120',
    'elasticsearch.rce_cve20151427',
    'elasticsearch.read_cve20153337',
    'elasticsearch.read_cve20155531',
    'ftp.ftp_weakpwd',
    'glassfish.glassfish_file_read',
    'glassfish.glassfish_weakpwd',
    'grafana.grafana_weakpwd',
    'iis.iis_webdav_put',
    'iis.iis_webdav_rce',
    'iis.short_filename',
    'javarmi.javarmi_rce',
    'jboss.jboss_readonly',
    'jboss.jboss_jmxconsole',
    'jboss.jboss_webconsole',
    'jboss.jboss_adminconsole',
    'jboss.jboss_jbossmq_httpil',
    'jboss.jboss_EJBInvokerServlet',
    'jboss.jboss_JMXInvokerServlet',
    'jenkins.user_enumeration',
    'jenkins.unauth2rce',
    'memcache.memcache_unauth',
    'mikrotik.winbox_cve_2018_14847',
    'mongodb.mongodb_unauth',
    'mysql.mysql_weakpwd',
    'mssql.mssql_weakpwd',
    'nexus_repository.nexus_weakpwd',
    'nginx.nginx_httproxy',
    'phpmyadmin.phpmyadmin_weakpwd',
    'phpmyadmin.phpmyadmin_setup_rce',
    'postgresql.postgresql_weakpwd',
    'redis.redis_weakpwd_unauth',
    'rsync.rsync_weakpwd_unauth',
    'smb_netbios.computer_info',
    'smb_netbios.ms17_010',
    'smb_netbios.new_ms17_010',
    'thinkphp.thinkphp5_rce',
    'thinkphp.thinkphp5010_rce',
    'thinkphp.thinkphp5023_rce',
    'thinkphp.thinkphp5152_rce',
    'tomcat.tomcat_put',
    'web.directory_listing',
    'web.git_or_svn_disclosure',
    'web.web_sensitive',
    'weblogic.rce_cve201710271',
    'weblogic.rce_cve20182628',
    'weblogic.ssrf_cve20144210',
    'zabbix.zabbix_weakpwd',
    'zookeeper.zookeeper_unauth',
]

WEB_PORTS_LIST = [    80,    81,    82,    83,    84,    85,    86,    87,    88,    89,\
                      90,   443,  4848,  7001,  7002,  7778,  8000,  8001,  8002,  8003,\
                    8004,  8005,  8006,  8007,  8008,  8009,  8010,  8020,  8030,  8040,\
                    8043,  8050,  8060,  8066,  8069,  8070,  8080,  8081,  8082,  8083,\
                    8084,  8085,  8086,  8087,  8088,  8089,  8090,  8096,  8099,  8100,\
                    8200,  8443,  8480,  8488,  8588,  8688,  8788,  8800,  8888,  8900,\
                    9000,  9001,  9002,  9003,  9004,  9005,  9006,  9007,  9008,  9909,\
                    9010,  9020,  9030,  9040,  9043,  9050,  9060,  9070,  9080,  9081,\
                    9082,  9083,  9084,  9085,  9086,  9087,  9088,  9089,  9090,  9100,\
                    9200,  9300,  9400,  9500,  9600,  9700,  9800,  9900,  9999,
                    ]

DEFAULT_PORTS_LIST = [   21,    22,    23,    25,    53,    67,    68,    80,    81,    82,\
                         83,    84,    85,    86,    87,    88,    89,    90,   109,   110,\
                        137,   139,   143,   161,   389,   443,   445,   465,   489,   512,\
                        513,   514,   873,   993,   995,  1080,  1090,  1098,  1099,  1158,\
                       1352,  1433,  1434,  1521,  1723,  1873,  2082,  2083,  2181,  2222,\
                       2375,  2601,  2604,  3000,  3128,  3306,  3311,  3312,  3389,  3690,\
                       4440,  4444,  4445,  4848,  5000,  5432,  5632,  5800,  5900,  5984,\
                       6082,  6379,  6800,  7001,  7002,  7778,  8000,  8001,  8002,  8003,\
                       8004,  8005,  8006,  8007,  8008,  8009,  8010,  8020,  8030,  8040,\
                       8043,  8050,  8060,  8066,  8069,  8070,  8080,  8081,  8082,  8083,\
                       8084,  8085,  8086,  8087,  8088,  8089,  8090,  8096,  8099,  8100,\
                       8161,  8200,  8291,  8443,  8480,  8488,  8588,  8688,  8788,  8800,\
                       8888,  8900,  8999,  9000,  9001,  9002,  9003,  9004,  9005,  9006,\
                       9007,  9008,  9909,  9010,  9020,  9030,  9040,  9043,  9050,  9060,\
                       9066,  9070,  9080,  9081,  9082,  9083,  9084,  9085,  9086,  9087,\
                       9088,  9089,  9090,  9100,  9200,  9300,  9400,  9500,  9600,  9700,\
                       9800,  9900,  9999, 10000, 10001, 10050, 10051, 10990, 11211, 14147,\
                      27017, 28017, 50000, 50030, 50070, 61616, 62078, 65535,
                       ]

DEFAULT_PORTS_LIST = [str(i) for i in DEFAULT_PORTS_LIST]

DEFAULT_PORT_SERVICES_DICT = {
    '21':'FTP',
    '22':'SSH',
    '23':'Telnet',
    '25':'SMTP',
    '53':'DNS',
    '67':'DHCP',
    '68':'DHCP',
    '69':'TFTP',
    '80':'Web',
    '109':'POP3',
    '110':'POP3',
    '137':'NetBIOS',
    '139':'NetBIOS',
    '143':'IMAP',
    '161':'SNMP',
    '389':'LDAP',
    '443':'Web',
    '445':'SMB',
    '465':'SMTPS',
    '489':'LDAP',
    '512':'Linux R RPE',
    '513':'Linux R RLT',
    '514':'Linux R cmd',
    '873':'Rsync',
    '993':'IMAPS',
    '995':'POP3',
    '1080':'Proxy',
    '1090':'JavaRMI',
    '1098':'JavaRMI',
    '1099':'JavaRMI',
    '1158':'Oracle EMCTL', 
    '1352':'Lotus',
    '1433':'MSSQL',
    '1434':'MSSQL Monitor',
    '1521':'Oracle',
    '1723':'PPTP', 
    '1873':'Rsync',
    '2082':'cPanel admin panel/CentOS web panel',
    '2083':'CPanel admin panel/CentOS web panel',
    '2100':'Oracle XDB FTP',
    '2181':'Zookeeper',
    '2222':'DA admin panel',
    '2375':'Docker',
    '2601':'Zebra',
    '2604':'Zebra',
    '3000':'Gitea Web',
    '3128':'Squid Proxy',
    '3306':'MySQL/MariaDB',
    '3311':'Kangle admin panel',
    '3312':'Kangle admin panel',
    '3389':'RDP',
    '3690':'SVN',
    '4440':'Rundeck',
    '4848':'GlassFish',
    '5000':'SysBase/DB2',
    '5432':'PostgreSql',
    '5632':'PcAnywhere',
    '5800':'VNC',
    '5900':'VNC',
    '5938':'TeamViewer',
    '5984':'CouchDB',
    '6082':'varnish',
    '6379':'Redis',
    '6380':'Redis',
    '6800':'Aria2',
    '7001':'Weblogic',
    '7002':'Weblogic',
    '7778':'Kloxo admin panel',
    '8069':'Zabbix',
    '8161':'ActiveMQ',
    '8291':'RouterOS/Winbox',
    '8080':'Web',
    '9001':'Weblogic',
    '9043':'WebSphere',
    '9060':'WebSphere',
    '9080':'WebSphere',
    '9090':'WebSphere',
    '9200':'Elasticsearch',
    '9300':'Elasticsearch',
    '10000':'Virtualmin/Webmin',
    '10050':'Zabbix agent',
    '10051':'Zabbix server',
    '10990':'JavaRMI',
    '11211':'Memcached',
    '14147':'FileZilla Manager',
    '27017':'MongoDB',
    '27018':'MongoDB',
    '50000':'SAP NetWeaver',
    '50030':'Hadoop',
    '50070':'Hadoop',
    '61616':'ActiveMQ',
    '62078':'iPhone-sync',
}

MUTEX = threading.Lock()

USER_LIST = []
PASS_LIST = []
IP_OPEN_PORT = []
VULN_INPUT_LIST = []
DNS_HISTORY_RECORD = []
WEB_INFO_RESULT_LIST = []
PING_SCAN_RESULT_LIST = []
PORT_SCAN_RESULT_LIST = []
VULN_SCAN_RESULT_LIST = []
IP_OPENPORT_VULN_MATCH_DICT = {}

globals()['MUTEX'] = MUTEX
globals()['USER_LIST'] = USER_LIST
globals()['PASS_LIST'] = PASS_LIST
globals()['IP_OPEN_PORT'] = IP_OPEN_PORT
globals()['WEB_PORTS_LIST'] = WEB_PORTS_LIST
globals()['VULN_CHECK_LIST'] = VULN_CHECK_LIST
globals()['VULN_INPUT_LIST'] = VULN_INPUT_LIST
globals()['DEFAULT_PORTS_LIST'] = DEFAULT_PORTS_LIST
globals()['DNS_HISTORY_RECORD'] = DNS_HISTORY_RECORD
globals()['WEB_INFO_RESULT_LIST'] = WEB_INFO_RESULT_LIST
globals()['PING_SCAN_RESULT_LIST'] = PING_SCAN_RESULT_LIST
globals()['PORT_SCAN_RESULT_LIST'] = PORT_SCAN_RESULT_LIST
globals()['VULN_SCAN_RESULT_LIST'] = VULN_SCAN_RESULT_LIST
globals()['DEFAULT_PORT_SERVICES_DICT'] = DEFAULT_PORT_SERVICES_DICT
globals()['IP_OPENPORT_VULN_MATCH_DICT'] = IP_OPENPORT_VULN_MATCH_DICT