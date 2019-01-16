# 如何开始

### 使用参数

```
usage: Perun     [-h] [-t TARGET [TARGET ...]] [-p PORT [PORT ...]]
                 [--timeout TIMEOUT] [--thread THREAD] [-l LOAD_FILE_PATH]
                 [--vuln VULN [VULN ...]] [--all-list] [--selected-vuln]
                 [--search SEARCH [SEARCH ...]] [--filter FILTER [FILTER ...]]
                 [--exclude EXCLUDE [EXCLUDE ...]]
                 [--set-port SET_PORT [SET_PORT ...]] [--search-list]
                 [--user-path USER_PATH] [--pass-path PASS_PATH]
                 [--add-web-path ADD_WEB_PATH] [--skip-ping] [--report REPORT]
                 [--skip-report]

Perun

optional arguments:
  -h, --help            显示帮助
  -t TARGET [TARGET ...], --target TARGET [TARGET ...]
                        设置目标或目标文件，支持URL/IP/IPa-IPb段/CIDR，以及前述类型的混杂输入，多个目标使用空格分隔
  -p PORT [PORT ...], --port PORT [PORT ...]
                        设置端口，支持单个端口和端口段(PortA-PortB)，以及前述类型的混杂输入，多个端口使用空格分隔
  --timeout TIMEOUT     设置超时时间
  --thread THREAD       设置线程数量
  -l LOAD_FILE_PATH, --load-file-path LOAD_FILE_PATH
                        设置加载路径，本地文件路径或者远程URL地址
  --vuln VULN [VULN ...]
                        选择Vuln模块，多个Vuln模块名使用空格分隔，默认会针对各模块内默认端口进行扫描，扫描指定端口
                        可以使用activemq.activemq_weakpwd=8161这样的形式输入，'='后指定的端口也支持单个端口和
                        端口段的形式，多个端口使用','分隔
  --all-list            显示所有支持的Vuln模块
  --selected-vuln       显示已选择的Vuln模块(包括vuln指定/search搜索/filter筛选/exclude排除操作后的结果)和Vuln模
                        块信息，设置此参数是为了方便使用者确定需要运行的模块是否符合预期
  --search SEARCH [SEARCH ...]
                        设置关键词，用于搜索匹配的Vuln模块(或关系)，多个关键词使用空格分隔
  --filter FILTER [FILTER ...]
                        设置关键词，用于搜索匹配的Vuln模块(和关系)，多个关键词使用空格分隔
  --exclude EXCLUDE [EXCLUDE ...]
                        排除运行指定的Vuln模块，多个Vuln模块名使用空格分隔
  --set-port SET_PORT [SET_PORT ...]
                        设置搜索匹配的Vuln模块的端口，支持单个端口和端口段的形式，多个端口使用','分隔
  --search-list         显示搜索后的Vuln模块结果(仅包含search搜索/filter筛选操作的结果)，设置此参数是为了便于使用
                        者查看搜索结果是否符合预期
  --user-path USER_PATH
                        设置用于爆破一些弱口令的username字典文件路径(各模块已内置精简字典)
  --pass-path PASS_PATH
                        设置用于爆破一些弱口令的password字典文件路径(各模块已内置精简字典)
  --add-web-path ADD_WEB_PATH
                        追加web扫描时的web路径，此参数用于解决如phpMyAdmin未处于web根目录等情况
  --skip-ping           忽略ping扫描
  --report REPORT       设置生成报告名，默认以时间戳命名
  --skip-report         忽略报告生成操作
```

### 使用举例

- 本地加载同目录下项目文件, 扫描`192.168.0.1/24、192.168.1.10-192.168.1.30、https://www.google.com、192.168.2.100`的默认端口

  `Perun -l . -t 192.168.0.1/24 192.168.1.10-192.168.1.30 https://www.google.com 192.168.2.100`

- 远程加载`http://Perun.com`Web上的项目文件，扫描`192.168.0.0/24`的`80、443、8000-9000、81-90`端口

  `Perun -l http://Perun.com -t 192.168.0.0/24 -p 80 443 8000-9000 81-90`

- 本地加载扫描`192.168.0.0/24`的默认端口，并检测是否存在`javarmi.javarmi_rce`和`weblogic.rce_cve201710271`漏洞，其中`javarmi.javarmi_rce`模块扫描该Vuln模块默认端口，`weblogic.rce_cve201710271`扫描`80、90、8000-9000`端口

  `Perun -l . -t 192.168.0.0/24 --vuln javarmi.javarmi_rce weblogic.rce_cve201710271=80,90,8000-9000`

- 本地加载并列出所有支持Vuln模块

  `Perun -l . --all-list`

- 本地加载并指定关键词为smb/rce进行搜索，并列出搜索结果，不进行扫描，Perun将列出所有关键词为smb和rce的Vuln模块和Vuln模块信息
  
  `Perun -l . --search smb rce --search-list`

  `Perun -l . -t 192.168.0.0/24 --search smb rce --search-list`

- 本地加载并指定关键词为innet/rce进行搜索，从搜索结果中筛选出所有dangers关键词Vuln模块，不进行扫描，Perun将列出所有同时具有`innet&dangers`、`rce&dangers`的Vuln模块和Vuln模块信息

  `Perun -l . --search innet rce --filter rce --search-list`

- 本地加载并针对target.txt文件内的目标，忽略ping扫描和Html报告生成操作，进行默认端口扫描，然后加载所有内网Vuln模块(关键词为innet)进行扫描，所有Vuln模块仅扫描各模块默认端口

  `Perun -l . -t target.txt --search innet --skip-ping --skip-report`

- 本地加载，指定选择Vuln模块`nexus_repository.nexus_weakpwd`，搜索所有innet关键词Vuln模块，从选择和搜索的结果中排除Vuln模块`tomcat.tomcat_put`和`zabbix.zabbix_weakpwd`，列出已选择的Vuln模块(包括vuln指定/search搜索/filter筛选/exclude排除操作后的结果)和Vuln模块信息，不进行扫描

  `Perun -l . -t 192.168.0.0/24 --vuln nexus_repository.nexus_weakpwd --search innet --exclude tomcat.tomcat_put zabbix.zabbix_weakpwd --selected-vuln`

- 本地加载扫描`192.168.0.0/24`的默认端口，加载所有关键词有rce的Vuln模块，各Vuln模块不扫描其默认端口，改为扫描`80、1000-8000`端口，其中需要访问Web服务的Vuln模块设置Web路径为`http://target.com/wwwtest/`

  `Perun -l . -t 192.168.0.0/24 --search rce --set-port 80,1000-8000 --add-web-path wwwtest`

- 本地加载扫描192.168.0.0/24的默认端口，加载MySQL的弱口令扫描Vuln模块，针对该模块默认端口(3306)进行弱口令扫描，弃用该模块内置精简密码字典，改为使用password.txt密码字典进行爆破，不生成报告

  `Perun -l . -t 192.168.0.0/24 --search mysql --filter weakpassword --pass-path password.txt --skip-report`

**注意:**

- 关于-l/--load-file-path参数
  
  -l/--load-file-path参数用于指定Perun启动器加载其余文件的路径，可以为远程路径，也可以是本地指定路径，上述示例中分别以指定当前同目录路径和指定`http://Perun.com`远程路径为示例

- 关于三个显示参数
  
  --all-list是显示所有支持的Vuln模块，--search-list是显示搜索后结果的Vuln模块(仅包含search搜索/filter筛选操作的结果)，--selected-vuln是显示所有已选择的Vuln模块(包括vuln指定/search搜索/filter筛选/exclude排除操作后的结果)，这三个参数都是为了使用者方便选择Vuln模块而设置，使用这三个参数中任一参数，Perun都将只列出符合要求的Vuln模块，不进行扫描

- 关键词同义词

  关键词不区分大小写，且部分关键词支持同义词，具体参见MakeSearchByfilter类_replace_synonym()方法，如`weakpass`、`weakpassword`、`weakpwd`、`weakpass`、`pwd`、`pass`、`password`将指向`weak_password`关键词，`CVE-2017-7504`、`Cve_2017-7504`等都将指向`cve_2017_7504`关键词
