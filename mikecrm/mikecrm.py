# -*- coding: utf-8 -*-
import re
import json
import logging
from urllib import request, parse

class Mikecrm:
    def __init__(self, page, data):
        self.proxy_ip = 'localhost'
        submit_url = 'http://cn.mikecrm.com/handler/web/form_runtime/handleSubmit.php'
        referer_url = 'http://cn.mikecrm.com/%s' % page
        headers = {
            'Host': 'cn.mikecrm.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Origin': 'http://cn.mikecrm.com',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': referer_url,
            'Accept-Encoding': 'deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
        }
        data = parse.urlencode(data).encode('utf-8')
        self.req = request.Request(submit_url, headers=headers, data=data)

    def set_proxy(self, ip, port=None, proxy_type='http,https,sock4,sock5'):
        if not port:
            ipre = re.compile(r'^(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d]):\d{1,5}$')
            if ipre.match(ip):
                self.proxy_ip, port = ip.split(':')
        else:
            self.proxy_ip = ip
        proxy_address = {}
        for _type in proxy_type.split(','):
            proxy_address[_type] = '%s:%s' % (self.proxy_ip, port)
        proxy = request.ProxyHandler(proxy_address)
        opener = request.build_opener(proxy)
        opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64)")]
        self.opener = opener
        return self

    def submit(self, timeout=10):
        try:
            page = self.opener.open(self.req, timeout=timeout).read()
        except Exception as e:
            logging.error('%s ERROR OF [%s]' % (self.proxy_ip, e))
            return False
        resporse = page.decode('utf-8')
        try:
            result = json.loads(resporse)
            if result['r'] == 0:
                logging.info('%s  OK!' % self.proxy_ip)
                return True
            elif result['r'] == -827:
                logging.warning('%s has exist submited yet!' % self.proxy_ip)
                return False
        except:
            logging.error(resporse)
            return False
