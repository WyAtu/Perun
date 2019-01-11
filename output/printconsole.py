#!/usr/bin/env python
# -*- coding:utf-8 -*-

class PrintConsole():
    def __init__(self, message, style='info'):
        self._style = style.lower()
        self._message = str(message.decode('utf-8').encode('gbk'))
        self._message = ''.join(self._message.splitlines())

        self._style2color_list = {'error' : 'red', 'right' : 'green', 'info' : 'blue', 'common' : 'white'}
        self._style2symbol_list = {'error' : '[-]', 'right' : '[+]', 'info' : '[*]', 'common' : ''}
        
        self._color = self._style2color_list[self._style] if self._style2color_list.has_key(self._style) else 'white'
        self._symbol = self._style2symbol_list[self._style] if self._style2symbol_list.has_key(self._style) else '[*]'
       
        self._select_color_by_platform()
        self._print()

    def _print(self):
        try:
            if osname == 'nt':
                MUTEX.acquire()
                self.set_cmd_text_color(self._color_list[self._color])
                stdout.write(self._symbol)
                self.set_cmd_text_color(0x0f)
                stdout.write(' ' + self._message + '\n')
                MUTEX.release()
                self._exit()
            else:
                MUTEX.acquire()
                stdout.write(self._color_list[self._color]+self._symbol+'\033[0m ' + self._message + '\n')
                MUTEX.release()
                self._exit()
        except:
            pass

    def set_cmd_text_color(self, color):
        STD_OUTPUT_HANDLE = -11
        std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, color)
        return Bool

    def _select_color_by_platform(self):
        _unix_color_list = {'red' : '\033[0;91m', 'green' : '\033[0;92m', 'white' : '\033[0;97m', 'blue' : '\033[0;94m',}
        _windows_color_list = {'red' : 0x04, 'green' : 0x0a, 'white' : 0x0f, 'blue' : 0x03, }
        self._color_list = _windows_color_list if osname == "nt" else _unix_color_list

    def _exit(self):
        if self._style == 'error':
            exit(0)

globals()['PrintConsole'] = PrintConsole