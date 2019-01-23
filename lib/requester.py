#!/usr/bin/env python
# -*- coding:utf-8 -*-

class RequesterOpenError(Exception):
    def __init__(self):
        super(Exception, self).__init__(self)

    def __str__(self):
        return "<Requester error [url open failed]>"

class RequesterBuildError(Exception):
    def __init__(self, method):
        super(Exception, self).__init__(self)
        self._method = method

    def __str__(self):
        return "<Requester error [No such method: '%s']>"%(self._method)

class Requester():
    def __init__(self, url, method="GET", data="", jsons="", header="", timeout=3, noencode=False, proxy={}):
        self._url = url
        self._timeout = timeout
        self._header = header
        if jsons != "":
            self._data = json.dumps(jsons)
        elif noencode:
            self._data = data
        else:
            self._data = urllib.urlencode(data)
        if self._header == "":
            uas = [ 
                'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36',
                'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
                'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
                'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:27.0) Gecko/20121011 Firefox/27.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0',
                'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; de-at) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
                'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 3.0)',
                'Mozilla/5.0 (X11; Linux i686; rv:21.0) Gecko/20100101 Firefox/21.0',
                'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
                'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
                'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20100101 Firefox/21.0',
                'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F',
                'Opera/9.80 (Windows NT 5.1; U; zh-tw) Presto/2.8.131 Version/11.10',
                'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; zh-cn) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5',
                'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.1; SV1; .NET CLR 2.8.52393; WOW64; en-US)',
                ]
            random_ua = uas[random.randint(0,len(uas))]
            self._header = {
                "Accept-Language": "en-US,en;q=0.5",
                "User-Agent": random_ua,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Referer": "http://thewebsite.com",
                "Connection": "keep-alive"
                }

        if proxy == {}:
            proxy_server = {}
        else:
            proxy_server = proxy
        ## Global proxy for debug
        #proxy_server = {'http': '127.0.0.1:8080'}
        proxy = urllib2.ProxyHandler(proxy_server)
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)

        if method.lower() == "get":
            self._get()
        elif method.lower() == "post":
            self._post()
        elif method.lower() in ["head", "put", "delete", "options"]:
            self._other_method(method)
        else:
            raise RequesterBuildError(method.upper())

    def _get(self):
        try:
            request = urllib2.Request(self._url, headers=self._header)
            response = urllib2.urlopen(request, timeout=self._timeout)
            self.html = response.read()
            self.code = response.code
            self.headers_dict = response.headers
            self.headers = str(response.headers)
            if response.geturl() != self._url:
                self.code = 301 # 301 or 302
        except urllib2.HTTPError as e: # 400-599
            if e.code == 400 and 'https' in e.read().lower():
                raise RequesterOpenError()
            self.headers = str(e.headers)
            self.headers_dict = e.headers
            self.code = e.code
            self.html = e.read()
        except urllib2.URLError as e:
            raise RequesterOpenError()
        except:
            self.headers_dict = {}
            self.headers = ""
            self.code = 0
            self.html = ""

    def _post(self):
        try:
            request = urllib2.Request(self._url, headers=self._header)
            response = urllib2.urlopen(request, data=self._data, timeout=self._timeout)
            self.html = response.read()
            self.code = response.code
            self.headers = str(response.headers)
            self.headers_dict = response.headers
            if response.geturl() != self._url:
                self.code = 301 # 301 or 302
        except urllib2.HTTPError as e:
            if e.code == 400 and 'https' in e.read().lower():
                raise RequesterOpenError()
            self.headers = str(e.headers)
            self.headers_dict = e.headers
            self.code = e.code
            self.html = e.read()
        except urllib2.URLError as e:
            raise RequesterOpenError()
        except:
            self.headers_dict = {}
            self.headers = ""
            self.code = 0
            self.html = ""

    def _other_method(self, method):
        try:
            request = urllib2.Request(self._url, headers=self._header)
            request.get_method = lambda : method.upper()
            response = urllib2.urlopen(request, data=self._data, timeout=self._timeout)
            self.html = response.read()
            self.code = response.code
            self.headers = str(response.headers)
            self.headers_dict = response.headers
            if response.geturl() != self._url:
                self.code = 301 # 301 or 302
        except urllib2.HTTPError as e:
            if e.code == 400 and 'https' in e.read().lower():
                raise RequesterOpenError()
            self.headers_dict = e.headers
            self.headers = str(e.headers)
            self.code = e.code
            self.html = e.read()
        except urllib2.URLError as e:
            raise RequesterOpenError()
        except:
            self.headers_dict = {}
            self.headers = ""
            self.code = 0
            self.html = ""

globals()['Requester'] = Requester
globals()['RequesterOpenError'] = RequesterOpenError
globals()['RequesterBuildError'] = RequesterBuildError