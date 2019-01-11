#!/usr/bin/env python
# -*- coding:utf-8 -*-

class MakeWeakPWDList():
    def __init__(self, user_list, pass_list):
        if user_list == "": pass
        else:
            global USER_LIST
            USER_LIST = self._open_file(user_list)
        if pass_list == "": pass
        else:
            global PASS_LIST
            PASS_LIST = self._open_file(pass_list)

    def _open_file(self, file_path):
        list_tmp = []
        if not exists(file_path): PrintConsole('Not found file %s'%(file_path), 'error')
        try:
            fp = open(file_path, 'r+')
            map(lambda x: list_tmp.append(x), [_.strip() for _ in fp.readlines()])
            list_tmp = list(set(list_tmp))
            fp.close()
            return list_tmp
        except:
            try: fp.close()
            except: pass

globals()['MakeWeakPWDList'] = MakeWeakPWDList