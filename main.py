# -*- coding: utf-8 -*-
import logsetting
from conffor import conffor
from mikecrm.mikecrm import Mikecrm

conf_file = './mikecrm.json'
config = conffor.load(conf_file)
target = config['mikecrm']



if __name__ == "__main__":
    brush = Mikecrm(**target)
    brush.set_proxy('http', '117.143.109.155', '80')
    brush.submit()

