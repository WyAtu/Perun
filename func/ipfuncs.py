#!/usr/bin/env python
# -*- coding:utf-8 -*-

def ip2num(ip):
    ip = [int(x) for x in ip.split('.')]
    return ip[0] <<24 | ip[1]<<16 | ip[2]<<8 |ip[3]

def num2ip(num):
    return '%s.%s.%s.%s' %( (num & 0xff000000) >>24, (num & 0x00ff0000) >>16, (num & 0x0000ff00) >>8,num & 0x000000ff)

def check_ip_valid(ip):
    try:
        for _ in [int(x) for x in ip.split('.')]:
            if _ < 0 or _ > 255:return False
        return True
    except:
        return False

def get_ip_by_ip_or_url(url):
    try:
        ip = [socket.gethostbyname(url),]
        return ip
    except:
        PrintConsole('Failed to parse the target "%s"'%url, 'error')

def get_ips_list_by_a2b(ips):
    try:
        start_ip, end_ip = ips.split('-')
        if check_ip_valid(start_ip) and check_ip_valid(end_ip):
            return [num2ip(num) \
                    for num in range(ip2num(start_ip), ip2num(end_ip)+1) \
                    if num & 0xff]
    except:
        return []

def get_ips_list_by_cidr(ips):
    try:
        ip, mask = ips.split('/')
        ip_split = [int(i) for i in ip.split('.')]
        mask_type = int(mask) // 8
        mask_len = int(mask) - mask_type*8
        ip_start = ip_split[mask_type]
        if mask_len != 0:
            ip_num = eval('0b'+'1'*(8-mask_len))
            status = True
            total_num = 2**(8-mask_len)
            for i in range(1, 256):
                if i*total_num > ip_start:
                    ip_end = total_num * i - 1
                    ip_start = ip_end - ip_num
                    break
        else:
            ip_num = 256
            ip_start = 0
        all_ips = []
        new_ips = [str(i) for i in ip_split]
        for i in range(ip_start, 256):
            new_ips[mask_type] = str(i)
            if i > ip_start+ip_num:
                break
            if mask_type == 3:
                all_ips.append('.'.join(new_ips))
                continue
            for j in range(mask_type+1, 4):
                for k in range(256):
                    new_ips[j] = str(k)
                    if mask_type == 2:
                        all_ips.append('.'.join(new_ips))
                        continue
                    for l in range(mask_type+2, 4):
                        for m in range(256):
                            new_ips[l] = str(m)
                            if mask_type == 1:
                                all_ips.append('.'.join(new_ips))
                                continue
                            for n in range(mask_type+3, 4):
                                for o in range(256):
                                    new_ips[l] = str(o)
                                    if mask_type == 0:
                                        all_ips.append('.'.join(new_ips))
                                        continue
        return get_ips_list_by_a2b(all_ips[0]+"-"+all_ips[-1])
    except:
        return []

globals()['ip2num'] = ip2num
globals()['num2ip'] = num2ip
globals()['check_ip_valid'] = check_ip_valid
globals()['get_ip_by_ip_or_url'] = get_ip_by_ip_or_url
globals()['get_ips_list_by_a2b'] = get_ips_list_by_a2b
globals()['get_ips_list_by_cidr'] = get_ips_list_by_cidr