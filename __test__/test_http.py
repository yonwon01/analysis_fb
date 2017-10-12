from urllib.request import Request, urlopen
from datetime import datetime
import sys

try:
    url='http://192.168.1.38:8088/mysite3/guestbook/ajax'
    request = Request(url)
    resp=urlopen(request)
    resp_body =resp.read().decode('utf-8')
    print(resp_body)
except Exception as e:
    print('%s : %s' % (e,datetime),file=sys.stderr)