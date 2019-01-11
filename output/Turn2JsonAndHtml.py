#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Turn2JsonAndHtml():
    def __init__(self, start_time_str, end_time_str):
        try:
            port_scan_table_data = ""
            for _ in PORT_SCAN_RESULT_LIST:
                try:
                    port_scan_table_data = port_scan_table_data + """{"ip" : "%s", "port" : "%s", "status" : "open", "default_service" : "%s"},\n\t\t\t\t"""%(_['ip'], _['port'], _['default_service'])
                except UnicodeDecodeError:
                    pass
            columns = """\n\t\t\t\t{"field" : "ip", "title" : "IP", "width" : 100, "tilteAlign" : "center", "columnAlign" : "center"},\n\t\t\t\t{"field" : "port", "title" : "PORT", "width" : 100, "tilteAlign" : "center", "columnAlign" : "center"},\n\t\t\t\t{"field" : "status", "title" : "STATUS", "width" : 100, "tilteAlign" : "center", "columnAlign" : "center"},\n\t\t\t\t{"field" : "default_service", "title" : "DEFAULT SERVICE", "width" : 100, "tilteAlign" : "center", "columnAlign" : "center"},\n\t\t\t\t"""
            json_source_table = """\n\t\t\t{\n\t\t\t"name" : "port scan",\n\t\t\t"tableData" : [\n\t\t\t\t%s],\n\t\t\t"columns" : [%s],\n\t\t\t},"""%(port_scan_table_data, columns)

            web_scan_table_data = ""
            for _ in WEB_INFO_RESULT_LIST:
                try:
                    web_scan_table_data = web_scan_table_data +  """{"ip" : "%s", "port" : "%s", "header" : "%s", "title" : "%s"},\n\t\t\t\t"""%(_['ip'], _['port'], _['header'].replace('"', '\\"'), _['title'].replace('"', '\\"'))
                except UnicodeDecodeError:
                    pass
            columns = """\n\t\t\t\t{"field" : "ip", "title" : "IP", "width" : 100, "tilteAlign" : "center", "columnAlign" : "center"},\n\t\t\t\t{"field" : "port", "title" : "PORT", "width" : 100, "tilteAlign" : "center", "columnAlign" : "center"},\n\t\t\t\t{"field" : "header", "title" : "HEADER", "width" : 100, "tilteAlign" : "center", "columnAlign" : "center"},\n\t\t\t\t{"field" : "title", "title" : "TITLE", "width" : 100, "tilteAlign" : "center", "columnAlign" : "center"},\n\t\t\t\t"""
            json_source_table = json_source_table + """\n\t\t\t{\n\t\t\t"name" : "web scan",\n\t\t\t"tableData" : [\n\t\t\t\t%s],\n\t\t\t"columns" : [%s],\n\t\t\t},"""%(web_scan_table_data, columns)

            for vuln_name, vuln_info in self.adjustment_vulnlist().items():
                vuln_scan_table_data = ""
                for _ in vuln_info:
                    try:
                        vuln_scan_table_data = vuln_scan_table_data + """{"ip" : "%s", "port" : "%s", "vuln_name" : "%s", "more_info" : "%s"},\n\t\t\t\t"""%(_['ip'], _['port'], vuln_name, _['more_info'].replace('"', '\\"'))
                    except UnicodeDecodeError:
                        pass
                columns = """\n\t\t\t\t{"field" : "ip", "title" : "IP", "width" : 100, "tilteAlign" : "center", "columnAlign" : "center"},\n\t\t\t\t{"field" : "port", "title" : "PORT", "width" : 100, "tilteAlign" : "center", "columnAlign" : "center"},\n\t\t\t\t{"field" : "vuln_name", "title" : "VULN NAME", "width" : 100, "tilteAlign" : "center", "columnAlign" : "center"},\n\t\t\t\t{"field" : "more_info", "title" : "MORE INFO", "width" : 100, "tilteAlign" : "center", "columnAlign" : "center"},\n\t\t\t\t"""
                json_source_table = json_source_table + """\n\t\t\t{\n\t\t\t"name" : "%s",\n\t\t\t"tableData" : [\n\t\t\t\t%s],\n\t\t\t"columns" : [%s],\n\t\t\t},"""%(vuln_name.replace('_', ' '), vuln_scan_table_data, columns)

            self.json_source_summary = """\n\t"summary" : {\n\t\t"command" : "%s",\n\t\t"start" : "%s",\n\t\t"end" : "%s",\n\t\t},\n\t"table" : [%s\n\t\t]\n"""%(" ".join(argv), start_time_str, end_time_str, json_source_table)
        except:
            PrintConsole('Generated report unsuccessfully', 'error')

    def adjustment_vulnlist(self):
        vuln_scan_result_dict = {}
        exists_vuln_name = []
        for _ in VULN_SCAN_RESULT_LIST:
            if len(vuln_scan_result_dict) == 0:
                vuln_scan_result_dict[_['vuln_name']] = [{"ip" : _['ip'], "port" : _['port'], "more_info" : _['more_info']}]
                exists_vuln_name.append(_['vuln_name'])
            else:
                if _['vuln_name'] not in exists_vuln_name:
                    vuln_scan_result_dict[_['vuln_name']] = [{"ip" : _['ip'], "port" : _['port'], "more_info" : _['more_info']}]
                    exists_vuln_name.append(_['vuln_name'])
                else:
                    vuln_scan_result_dict[_['vuln_name']].append({"ip" : _['ip'], "port" : _['port'], "more_info" : _['more_info']})
        return vuln_scan_result_dict

    def export2html(self):
        try:
            fp1 = open('%s/output/report.html'%(load_file_base_path), 'r')
            read = fp1.read()
            fp1.close()
        except:
            try:
                try: fp1.close()
                except: pass
                read = urllib.urlopen('%s/output/report.html'%(load_file_base_path)).read()
            except:
                PrintConsole('Found no template report html file', 'error')
        try:
            fp2 = open(report_name, 'w')
            fp2.write(read.replace("'summary': {}", self.json_source_summary.decode('utf-8').encode('utf-8')))
        except:
            PrintConsole('Generated report unsuccessfully', 'error')
            try: fp2.close()
            except: pass

globals()['Turn2JsonAndHtml'] = Turn2JsonAndHtml