#!/usr/bin/env python
# -*- coding:utf-8 -*-

try:
    load_file('conf.loadfileconf')
    args = make_argparse()

    if args['all_list']: get_support_vulns_4_list()

    start_time = time()
    start_time_str = asctime(localtime(time()))

    globals()['args'] = args
    globals()['timeout'] = args['timeout']
    globals()['thread'] = args['thread']
    globals()['report_name'] = str(args['report'])
    globals()['vuln'] = [_.lower() for _ in args['vuln']]
    globals()['search_input'] = [_.lower() for _ in args['search']]
    globals()['search_list'] = args['search_list']
    globals()['_filter_input'] = [_.lower() for _ in args['filter']]
    globals()['exclude'] = [_.lower() for _ in args['exclude']]
    globals()['set_port'] = [_.lower() for _ in args['set_port']]
    globals()['add_web_path'] = args['add_web_path']

    if search_input or _filter_input: MakeSearchByfilter()

    if exclude: do_exclude(exclude)
    
    if args['selected_vuln']: show_vulns_info_4_info(vuln)
    
    if args['target'] == None: PrintConsole('Argument -t/--target is required, use \'-h\' to show the help info', 'error')
    
    PrintConsole('Perun start at %s'%(start_time_str), 'info')

    MakeVulnList(vuln)

    MakeWeakPWDList(args['user_path'], args['pass_path'])

    args_port = get_ports_list_from_input(args['port'])

    ips_list = MakeIPsList(args['target']).target

    ports_list = MakePortsList(args_port).target
    if not args['skip_ping']:
        PrintConsole('Start to pingscan', 'info')
        PingScan(ips_list)
        ips_list = PING_SCAN_RESULT_LIST
    else:
        PrintConsole('Skip the pingscan', 'info')

    if len(ips_list) == 0:
        PrintConsole('Found no up host by ping, if u are sure the target is up, please use --skip-ping to skip ping', 'error')

    PrintConsole('Start to portscan for %d hosts and %d ports'%(len(ips_list), len(ports_list)), 'info')
    queue = MakeQueue(ips_list, ports_list).q
    MakeStartThread(queue)
    queue.join()

    match_openport_2_vulnport()

    # if len(IP_OPENPORT_VULN_MATCH_DICT): DnsChecker().dns_start()   # this module is abandoned
    for _vuln_name, _ip_port_list in IP_OPENPORT_VULN_MATCH_DICT.items():
        load_file('vuln.%s'%(str(_vuln_name)))
        vulnchecker = VulnChecker(_ip_port_list).start()

    end_time_str = asctime(localtime(time()))

    if not args['skip_report']:
        PrintConsole('Start to generate the report %s'%(report_name), 'info')
        Turn2JsonAndHtml(start_time_str, end_time_str).export2html()
        PrintConsole('Generated report successfully', 'info')
    PrintConsole('Perun stop at %s'%(end_time_str), 'info')
    PrintConsole('All scan overed in %.2fs'%(time()-start_time), 'info')
except KeyboardInterrupt:
    PrintConsole('Ctrl+C by user aborted', 'error')