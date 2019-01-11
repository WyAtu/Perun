#!/usr/bin/env python
# -*- coding:utf-8 -*-

def match_openport_2_vulnport():
    for _ in PORT_SCAN_RESULT_LIST:
        for __ in VULN_INPUT_LIST:
            if (_['port'] in __['vuln_ports_list']  or __['vuln_ports_list'] == [0]) and __['vuln_name'] in VULN_CHECK_LIST:
                port = _['port']
                if __['vuln_ports_list'] == [0]:
                    port = 0
                if IP_OPENPORT_VULN_MATCH_DICT.has_key(__['vuln_name']):
                    IP_OPENPORT_VULN_MATCH_DICT[__['vuln_name']].append("%s:%d"%(_['ip'], int(port)))
                else:
                    IP_OPENPORT_VULN_MATCH_DICT[__['vuln_name']] = ["%s:%d"%(_['ip'], int(port))]
    for _key, _value in IP_OPENPORT_VULN_MATCH_DICT.items():
        IP_OPENPORT_VULN_MATCH_DICT[_key] = list(set(_value))

def check_vuln_valid():
    for _ in VULN_INPUT_LIST:
        if _['vuln_name'] not in VULN_CHECK_LIST:
            PrintConsole("Wrong Vuln checker selected, use '--all-list' to list all support Vulns", 'error')

def process_port_scan(ip, port):
    port_status, (header, title) = port_scan(ip, port)
    if port_status is True:
        default_service = match_port_2_service(port)
        PrintConsole('Port open: %s:%d, Default service: %s'%(ip, int(port), default_service), 'right')
        PORT_SCAN_RESULT_LIST.append({'ip' : ip, 'port' : port, 'default_service' : default_service})
        IP_OPEN_PORT.append('%s:%d'%(ip, port))
        if header is not False:
            PrintConsole('Web service: %s:%d, Title: %s'%(ip, int(port), str(title)), 'right')
            WEB_INFO_RESULT_LIST.append({'ip' : ip, 'port' : port, 'header' : str(header), 'title' : str(title)})

def match_port_2_service(port):
    if DEFAULT_PORT_SERVICES_DICT.has_key(str(port)):
        return DEFAULT_PORT_SERVICES_DICT[str(port)]
    return ""

def get_vuln_name_and_info():
    vuln_name_and_info = []
    for vuln_name in VULN_CHECK_LIST:
        load_file('vuln.%s'%(str(vuln_name)))
        vulnchecker = VulnChecker([])
        vuln_name_and_info.append({'vuln_name' : vuln_name, 'info' : vulnchecker.info})
    return vuln_name_and_info

def get_support_vulns_4_list():
    PrintConsole('Perun supports check the following Vulns:')
    vuln_name_and_info = get_vuln_name_and_info()
    stdout.write("{:^25}\t{:^20}\n".format("Vuln","Info"))
    for _ in vuln_name_and_info:
        stdout.write("%-25s\t%s\n"%(_['vuln_name'], _['info']))
    PrintConsole('There are %d Vulns in total'%(len(vuln_name_and_info)))
    exit(0)

def show_vulns_info_4_info(info, flag=1):
    if flag: PrintConsole('Perun shows the info of selected Vuln/Vulns:')
    else:  PrintConsole('Perun shows the info of matching Vuln/Vulns by seach:')
    vuln_name_and_info = get_vuln_name_and_info()
    show_info = "{:^25}\t{:^20}\n".format("Vuln","Info")
    for _ in vuln_name_and_info:
        if _['vuln_name'] in info:
            show_info = show_info + "%-25s\t%s\n"%(_['vuln_name'], _['info'])
    if show_info == "{:^25}\t{:^20}\n".format("Vuln","Info"):
        PrintConsole("Not found the selected Vuln/Vulns, use '--all-list' to list all support Vulns")
        exit(0)
    stdout.write(show_info)
    exit(0)

def random8string():
    return ''.join(random.sample(string.ascii_letters + string.digits, 8))

def do_exclude(exclude):
    for _ in exclude:
        try:
            vuln.remove(_)
        except:
            PrintConsole('No such Vuln %s'%(_))

globals()['do_exclude'] = do_exclude
globals()['random8string'] = random8string
globals()['check_vuln_valid'] = check_vuln_valid
globals()['process_port_scan'] = process_port_scan
globals()['match_port_2_service'] = match_port_2_service
globals()['get_vuln_name_and_info'] = get_vuln_name_and_info
globals()['show_vulns_info_4_info'] = show_vulns_info_4_info
globals()['get_support_vulns_4_list'] = get_support_vulns_4_list
globals()['match_openport_2_vulnport'] = match_openport_2_vulnport