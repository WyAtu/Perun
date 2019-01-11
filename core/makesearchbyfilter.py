#!/usr/bin/env python
# -*- coding:utf-8 -*-

class MakeSearchByfilter():
    def __init__(self):
        self._vuln_name_and_keyword = []
        search = self._replace_synonym(search_input)
        _filter = self._replace_synonym(_filter_input)
        if len(search) != 0 or len(_filter) != 0:
            self._load_file_2_get_keyword()
        if len(search) != 0:
            self._search_result_list = []
            map(self._get_search_result_list, search)
            self._search_result_list = list(set(self._search_result_list))

        if len(_filter) != 0:
            self._filter_result_list = []
            map(self._get_filter_result_list, _filter)

        if len(search) != 0 and len(_filter) == 0:
            self._match_list = self._search_result_list
        elif len(search) == 0 and len(_filter) != 0:
            self._match_list = self._filter_result_list
        elif len(search) != 0 and len(_filter) != 0:
            self._match_list = list((set(self._search_result_list).union(set(self._filter_result_list)))^(set(self._search_result_list)^set(self._filter_result_list)))
        else:
            self._match_list = []

        if self._match_list == []:
            PrintConsole('No matching vuln checker found by search', 'error')

        if search_list:
            show_vulns_info_4_info(self._match_list, 0)
        #   exit(0)
        for _ in self._match_list:
            for __ in set_port:
                vuln.append('%s=%s'%(_, __))
            if len(set_port) == 0:
                vuln.append('%s'%(_))

    def _load_file_2_get_keyword(self):
        for vuln_name in VULN_CHECK_LIST:
            load_file('vuln.%s'%(str(vuln_name)))
            vulnchecker = VulnChecker([])
            self._vuln_name_and_keyword.append({'vuln_name' : vuln_name, 'keyword' : vulnchecker.keyword})

    def _get_search_result_list(self, search_input):
        for _ in self._vuln_name_and_keyword:
            _vuln_name, _keyword = _.values()
            if search_input in _keyword:
                self._search_result_list.append(_vuln_name)

    def _get_filter_result_list(self, filter_input):
            tmp_filter_list = []
            for _ in self._vuln_name_and_keyword:
                _vuln_name, _keyword = _.values()
                if filter_input in _keyword:
                    tmp_filter_list.append(_vuln_name)
            if len(self._filter_result_list) == 0:
                self._filter_result_list = tmp_filter_list
            else:
                self._filter_result_list = list((set(tmp_filter_list).union(set(self._filter_result_list)))^(set(tmp_filter_list)^set(self._filter_result_list)))

    def _replace_synonym(self, input_list):
        result_list = []
        for i in input_list:
            if i.lower() in ['weakpass', 'weakpassword', 'weakpwd', 'weakpass', 'pwd', 'pass', 'password']:
                result_list.append('weak_password')
            elif i.lower() in ['intranet', 'innet']:
                result_list.append('intranet')
            elif i.lower() in ['rce', 'remote', 'remotecodeexecute', 'remotecommandexecute', 'remote_code_execute', 'remote_command_execute']:
                result_list.append('rce')
            elif i.lower() in ['file_upload', 'file-upload', 'fileupload', 'upload-file', 'upload_file', 'uploadfile']:
                result_list.append('file_upload')
            elif i.lower() in ['file_read', 'file-read', 'fileread', 'read-file', 'read_file', 'readfile']:
                result_list.append('file_read')
            elif '-' in i:
                result_list.append(i.replace('-', '_').lower())
            else:
                result_list.append(i.lower())
        return list(set(result_list))

globals()['MakeSearchByfilter'] = MakeSearchByfilter