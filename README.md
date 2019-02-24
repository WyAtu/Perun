# Perun
[![Python 2.7](https://img.shields.io/badge/python-2.7-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/aur/license/yaourt.svg)](https://github.com/WyAtu/Perun/blob/master/LICENSE) [![Vulns](https://img.shields.io/badge/Vulns/20190224-54-red.svg)](https://github.com/WyAtu/Perun/tree/master/vuln) 

**Perun**是一款主要适用于**乙方安服、渗透测试人员和甲方RedTeam红队人员的网络资产漏洞扫描器/扫描框架**，它主要适用于**内网环境**，加载漏洞检测Vuln模块后能够快速发现安全问题，并根据需要生成报表，以方便安全人员对授权项目完成测试工作。

**Perun**由Python2.7和Python标准库开发，所有功能(端口扫描，漏洞检测，控制台输出，生成Html报告)兼容Windows系统和\*nix系统，Html报告采用Vue+Element，**支持对扫描结果的排序、搜索、分页**。

**在内网环境中只需上传Perun的启动器文件**(未安装Python的主机环境下可以使用Pyinstaller[打包](https://github.com/WyAtu/Perun/tree/master/doc/package2exe#%E6%89%93%E5%8C%85perun%E4%BA%8C%E8%BF%9B%E5%88%B6%E6%96%87%E4%BB%B6)生成的单个控制台exe二进制启动器文件，大小在3-5M)，其余文件可以部署在云端，也可以部署在目标内网中，**既可用作普通的端口扫描器，又可用作漏洞扫描器**，方便安全人员在内网环境中进行工作。

## 快照预览

- 控制台快照

  ![all_list](https://github.com/WyAtu/Perun/blob/master/doc/snapshot/all_list.jpg)
  
  ---

  ![test](https://github.com/WyAtu/Perun/blob/master/doc/snapshot/test.jpg)

---

- 报告快照

  ![report_snapshot1](https://github.com/WyAtu/Perun/blob/master/doc/snapshot/report_snapshot1.jpg)
  
  ---

  ![report_snapshot1](https://github.com/WyAtu/Perun/blob/master/doc/snapshot/report_snapshot2.jpg)
  
  ---

  ![report_snapshot1](https://github.com/WyAtu/Perun/blob/master/doc/snapshot/report_snapshot3.jpg)

## 工作流程

- 加载-l参数指定路径下的项目代码

- 解析-t参数指定的目标

- 进行ping扫描活跃主机(使用--skip-ping参数将跳过ping扫描阶段)

- 根据默认扫描端口或-p参数对指定端口进行端口扫描，默认扫描178个端口，详见[Perun/conf/globallistconf.py](https://github.com/WyAtu/Perun/blob/master/conf/globallistconf.py)

- 解析--vuln和--search(包括--filter和--exclude)参数指定的漏洞检测Vuln模块

- 根据各Vuln模块默认扫描端口或--set-port指定各Vuln模块扫描端口，匹配目标主机开放端口，生成待扫描目标列表

- 加载各漏洞扫描Vuln模块Payload，进行漏洞扫描

- 生成报告(使用--skip-report参数将跳过生成报告)

## 启动和加载

Perun由Perun.py(或是由Perun.py打包生成的二进制文件)启动，有两种方式加载，远程加载和本地加载，通过-l/--load-file-path参数指定本地文件路径或者远程地址url后，Perun.py将会加载其他代码和漏洞检测Vuln模块并执行。

这样可以在保证项目开发目录结构清晰的同时，只需要一个启动器文件在内网环境中即可工作，其余文件可部署在公网云端或内网环境本地，单个启动器文件方便打包成更小的exe二进制文件，且更新插件不需要重新打包(如导入新的Python库则需要重新打包)，一劳永逸。

## 使用参数

[使用参数](https://github.com/WyAtu/Perun/blob/master/doc/how2start.md#%E4%BD%BF%E7%94%A8%E5%8F%82%E6%95%B0)

## 使用举例

[使用举例](https://github.com/WyAtu/Perun/blob/master/doc/how2start.md#%E4%BD%BF%E7%94%A8%E4%B8%BE%E4%BE%8B)

## 支持的Vuln模块

**Perun**目前支持54个Vuln模块

[支持的Vuln模块](https://github.com/WyAtu/Perun/blob/master/doc/aboutvuln.md#%E6%94%AF%E6%8C%81%E7%9A%84vuln%E6%A8%A1%E5%9D%97)

## 自定义Vuln模块

[编写新的自定义Vuln模块](https://github.com/WyAtu/Perun/blob/master/doc/aboutvuln.md#%E8%87%AA%E5%AE%9A%E4%B9%89vuln%E6%A8%A1%E5%9D%97)

**欢迎编写并提交更多自定义Vuln模块，直接pr或者发到邮箱wyatu[@]foxmail.com**

## 如何打包

[打包Perun二进制文件](https://github.com/WyAtu/Perun/tree/master/doc/package2exe#%E6%89%93%E5%8C%85perun%E4%BA%8C%E8%BF%9B%E5%88%B6%E6%96%87%E4%BB%B6)

## 更新日志

[CHANGELOG.md](https://github.com/WyAtu/Perun/blob/master/CHANGELOG.md)

## 致谢

- [liyuan](https://github.com/ly1102)大哥的报告前端代码支持

- [xunfeng](https://github.com/ysrc/xunfeng)、[Scanver](https://github.com/ydhcui/Scanver/)等开源项目和其他开源脚本/项目，很多Vuln模块参考或取自这些优秀的开源项目

在此表示感谢。

## 说明

Bug/更多自定义Vuln模块提交/意见建议，请直接pr或者发到邮箱wyatu[@]foxmail.com

本项目仅进行漏洞探测工作，无漏洞利用、攻击性行为，开发初衷仅为方便安全人员对授权项目完成测试工作和学习交流使用，**请使用者遵守当地相关法律，勿用于非授权测试，如作他用所承受的法律责任一概与作者无关，下载使用即代表使用者同意上述观点**。

附《[中华人民共和国网络安全法](http://www.npc.gov.cn/npc/xinwen/2016-11/07/content_2001605.htm)》。
