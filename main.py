# -*- coding: utf-8 -*-
import logging
import logsetting
from conffor import conffor
from mikecrm.mikecrm import Mikecrm

conf_file = './mikecrm.json'
config = conffor.load(conf_file)
target = config['mikecrm']

proxy_file = './proxy.json'
proxys = conffor.load(proxy_file)['data']


if __name__ == "__main__":
    brush = Mikecrm(**target)
    count = 0
    for index, item in enumerate(proxys):
        proxy = (item['type'], item['ip'], item['port'])
        if brush.set_proxy(*proxy).submit():
            count += 1
            logging.info('Current successes count is %d/%d' % (count, index))
