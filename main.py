# -*- coding: utf-8 -*-
from urllib import request, parse
submit_url = 'http://cn.mikecrm.com/handler/web/form_runtime/handleSubmit.php'
referer_url = 'http://cn.mikecrm.com/uf12V0J'
headers = {
    'Host': 'cn.mikecrm.com',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'http://cn.mikecrm.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': referer_url,
    'Accept-Encoding': 'deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
}
data = {
    'd': '{"cvs":{"i":200053046,"t":"uf12V0J","s":200146967,"acc":"p5Z0CY6lFfrzCacbCATBH76a22U89piw","r":"","c":{"cp":{"200547965":[200396017]}}}}'
}

if __name__ == "__main__":
    data = parse.urlencode(data).encode('utf-8')
    req = request.Request(submit_url, headers=headers, data=data)
    page = request.urlopen(req).read()
    page = page.decode('utf-8')
    print(page)
