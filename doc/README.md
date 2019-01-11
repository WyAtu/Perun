# Perun
[![Python 2.7](https://img.shields.io/badge/python-2.7-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/aur/license/yaourt.svg)](https://github.com/WyAtu/Perun/blob/master/LICENSE) [![Vulns](https://img.shields.io/badge/Vulns/20190111-42-red.svg)](https://github.com/WyAtu/Perun/tree/master/vuln) 

**Perun**是一款主要适用于**乙方安服、渗透测试人员和甲方RedTeam红队人员的网络资产漏洞扫描器/扫描框架**，它主要适用于**内网环境**，加载漏洞检测Vuln模块后能够快速发现安全问题，并根据需要生成报表，以方便安全人员对授权项目完成测试工作。

**Perun**由Python2.7和Python标准库开发，所有功能(端口扫描，漏洞检测，控制台输出，生成Html报告)兼容Windows系统和\*nix系统，Html报告采用Vue+Element，**支持对扫描结果的排序、搜索、分页**。

**在内网环境中只需上传Perun的启动器文件**(未安装Python的主机环境下可以使用Pyinstaller[打包](https://github.com/WyAtu/Perun/tree/master/doc/package2exe#%E6%89%93%E5%8C%85perun%E4%BA%8C%E8%BF%9B%E5%88%B6%E6%96%87%E4%BB%B6)生成的单个控制台exe二进制启动器文件，大小在3-5M)，其余文件可以部署在云端，也可以部署在目标内网中，**既可用作普通的端口扫描器，又可用作漏洞扫描器**，方便安全人员在内网环境中进行工作。

## 如何开始使用

[开始使用](https://github.com/WyAtu/Perun/blob/master/doc/how2start.md)

## 支持的Vuln模块

[支持的Vuln模块](https://github.com/WyAtu/Perun/blob/master/doc/aboutvuln.md#%E6%94%AF%E6%8C%81%E7%9A%84vuln%E6%A8%A1%E5%9D%97)

## 自定义Vuln模块

[编写新的自定义Vuln模块](https://github.com/WyAtu/Perun/blob/master/doc/aboutvuln.md#%E8%87%AA%E5%AE%9A%E4%B9%89vuln%E6%A8%A1%E5%9D%97)

**欢迎编写并提交更多自定义模块，直接pr或者发到邮箱wyatu[@]foxmail.com**

## 如何打包

[打包Perun二进制文件](https://github.com/WyAtu/Perun/tree/master/doc/package2exe#%E6%89%93%E5%8C%85perun%E4%BA%8C%E8%BF%9B%E5%88%B6%E6%96%87%E4%BB%B6)