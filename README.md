# Mikecrm Brush

Its a samll tool for brush tickets at mikecrm.com voting page.

## Usage

**Its need python 3.5 and above.**

### Install

First install require packages of python,

```bash
# recommend to use venv
$ python -m venv venv
$ source venv/bin/activate
# or in win
# > venv\Scripts\activate.bat
$ pip install -r requirements.txt
```

### config

Then change the config file for **your own info**, and institute rules of how to focus.

```bash
$ cp mikecrm.json.example mikecrm.json
$ vim mikecrm.json
```

This tool need proxys, so u must get some proxy address and save into `proxy.csv` or `proxys.json`.

The format stated in `proxy.csv/json.example` , and recommended use **CSV**.

### run

```python
python main.py
```

### some free proxy

[XiciDaili](http://api.xicidaili.com/free2016.txt)

[安小墨5000高匿代理](http://www.66ip.cn/nmtq.php?getnum=5000&isp=0&anonymoustype=3&start=&ports=&export=&ipaddress=&area=1&proxytype=2&api=66ip)

[快代理](http://www.kuaidaili.com/fetch/)

## License

MIT LICENSE