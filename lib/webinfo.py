#!/usr/bin/env python
# -*- coding:utf-8 -*-

def get_code(header,html):
    try:
        m = re.search(r'<meta.*?charset\=(.*?)"(>| |\/)',html, flags=re.I)
        if m:
            return m.group(1).replace('"','')
    except:
        pass
    try:
        if header.has_key('Content-Type'):
            Content_Type = header['Content-Type']
            m = re.search(r'.*?charset\=(.*?)(;|$)',Content_Type,flags=re.I)
            if m:return m.group(1)
    except:
        pass

def get_web_info(host,port):
    title_str,html = '',''
    try:
        info = urllib2.urlopen("https://%s:%d"%(host,int(port)),timeout=timeout)
        html = info.read()
        header = info.headers
    except urllib2.HTTPError,e:
        header = e.headers
    except:
        try:
            info = urllib2.urlopen("http://%s:%d"%(host,int(port)),timeout=timeout)
            html = info.read()
            header = info.headers
        except urllib2.HTTPError,e:
            header = e.headers
        except:
            return False,False
    if not header:return False,False
    try:
        html_code = get_code(header,html).strip()
        if html_code and len(html_code) < 12:
            html = html.decode(html_code).encode('utf-8')
    except:
        pass
    try:
        title = re.search(r'<title>(.*?)</title>', html, flags=re.I|re.M)
        if title:title_str=title.group(1)
    except:
        pass
    return str(header).replace('\n', ' ').replace('\r', ' '), title_str

globals()['get_code'] = get_code
globals()['get_web_info'] = get_web_info