#!/usr/bin/env python
# -*- coding:utf-8 -*-

def check_port_valid(port):
    try:
        if int(port) < 1 or int(port) > 65535:return False
        return True
    except:
        return False

def get_ports_list_by_a2b(ports):
    try:
        start_port, end_port = ports.split('-')
        if check_port_valid(start_port) and check_port_valid(end_port):
            return [port for port in range(int(start_port), int(end_port)+1)]
        return []
    except:
        return []

def get_ports_list_by_port(port):
    try:
        if check_port_valid(port):return [int(port), ]
        return []
    except:
        return []

def get_ports_list_from_input(input):
    ports_list = []
    for _ in input:
        ports_list = list(set(ports_list + _.split(',')))
    return ports_list

globals()['check_port_valid'] = check_port_valid
globals()['get_ports_list_by_a2b'] = get_ports_list_by_a2b
globals()['get_ports_list_by_port'] = get_ports_list_by_port
globals()['get_ports_list_from_input'] = get_ports_list_from_input