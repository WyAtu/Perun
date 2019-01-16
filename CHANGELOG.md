# Changelog

## 2019.01.16

### 修改

- [Perun/lib/requester.py](https://github.com/WyAtu/Perun/blob/master/lib/requester.py)中的Requester类，使其支持Proxy代理设置，和随机User-Agent头功能

- [Perun/vuln/thinkphp/thinkphp5_rce.py](https://github.com/WyAtu/Perun/blob/master/vuln/thinkphp/thinkphp5_rce.py)Vuln模块的检测方法，避免phpinfo首页错报等情况

- [Perun/vuln/thinkphp/thinkphp5023_rce.py](https://github.com/WyAtu/Perun/blob/master/vuln/thinkphp/thinkphp5023_rce.py)Vuln模块的检测方法，使其兼容不同系统

### 新增

- [Perun/vuln/thinkphp/thinkphp5010_rce.py](https://github.com/WyAtu/Perun/blob/master/vuln/thinkphp/thinkphp5010_rce.py)Vuln模块，用于检测ThinkPHP 5.0.\*(低于5.0.10)远程代码执行漏洞

- [Perun/vuln/thinkphp/thinkphp5152_rce.py](https://github.com/WyAtu/Perun/blob/master/vuln/thinkphp/thinkphp5010_rce.py)Vuln模块，用于检测ThinkPHP 5.1.*/5.2.*(5.1.x - 5.1.31, 5.2.0beta1)远程代码执行漏洞

- [Perun/vuln/nginx/nginx_httproxy.py](https://github.com/WyAtu/Perun/blob/master/vuln/nginx/nginx_httproxy.py)Vuln模块，用于检测Nginx配置不当导致正向代理

## 2019.01.10

### 新增

- [Perun/vuln/thinkphp/thinkphp5_rce.py](https://github.com/WyAtu/Perun/blob/master/vuln/thinkphp/thinkphp5_rce.py)Vuln模块，用于检测ThinkPHP 5.0.\*/5.1.\*远程代码执行漏洞

- [Perun/vuln/thinkphp/thinkphp5023_rce.py](https://github.com/WyAtu/Perun/blob/master/vuln/thinkphp/thinkphp5023_rce.py)Vuln模块，用于检测ThinkPHP5.0.\*(低于5.0.23)远程代码执行漏洞

## 更早

### 无记录