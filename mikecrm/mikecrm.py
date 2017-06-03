# -*- coding: utf-8 -*-
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

    def set_proxy(self, proxy_type, ip, port):
        self.proxy_ip = ip
        proxy_address = {proxy_type: '%s:%s' % (ip, port)}
        proxy = request.ProxyHandler(proxy_address)
        opener = request.build_opener(proxy)
        request.install_opener(opener)

    def submit(self):
        page = request.urlopen(self.req).read()
        resporse = page.decode('utf-8')
        try:
            result = json.loads(resporse)
            if result['r'] == 0:
                logging.info('%s  OK!' % self.proxy_ip)
            elif result['r'] == -827:
                logging.warning('%s has exist submited yet!' % self.proxy_ip)
        except:
            logging.error(resporse)
