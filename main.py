# -*- coding: utf-8 -*-
import queue
import logsetting
from conffor import conffor, csvtor as csv
from mikecrm.mikebrush import MikeBrush

conf_file = './mikecrm.json'
config = conffor.load(conf_file)
target = config['mikecrm']
thead_count = config['thead_count']

# proxy_file = './proxy.json'
# proxys_list = conffor.load(proxy_file)['data']

proxy_file = './proxy.csv'
proxys_list = csv.read_list_csv(None, proxy_file)

if __name__ == "__main__":
    proxys = queue.Queue()
    for item in proxys_list:
        # proxy = (item['ip'], item['port'], item['type'])
        proxys.put(item)
    brush = MikeBrush(target, proxys, thead_count)
    brush.run()
