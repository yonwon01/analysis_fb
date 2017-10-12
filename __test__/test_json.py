import sys
from urllib.request import Request, urlopen
from datetime import *
import json



try:
    url='http://localhost:8088/mysite3'
    request = Request(url)
    resp=urlopen(request)
    resp_body =resp.read().decode('utf-8')
    json_result=json.load(resp_body)

    print(json_result)

except Exception as e:
    print('%s : %s' % (e, datetime), file=sys.stderr)
