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
    def __init__(self, url, method="GET", data="", jsons="", header="", timeout=3, noencode=False):
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
            self._header = {
                "Accept-Language": "en-US,en;q=0.5",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Referer": "http://thewebsite.com",
                "Connection": "keep-alive"
                }

        ## Global proxy for debug
        # proxy_server = {'http': '127.0.0.1:8080'}
        # proxy = urllib2.ProxyHandler(proxy_server)
        # opener = urllib2.build_opener(proxy)
        # urllib2.install_opener(opener)

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
            self.headers = str(e.headers)
            self.headers_dict = e.headers
            self.code = e.code
            self.html = ""
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