from datetime import *
import sys


#json_request모듈 테스트 해보는곳
from analysis_fb.collection.api import json_request as jr


url='http://localhost:8088/mysite3/api/guestbook/list'

def success_fetch_guestbook_list(response):
    print(response)



def error_fetch_guestbook_list(e):
    print('%s : %s' % (e, datetime.now()), file=sys.stderr)


#jr.json_request(url=url,success=success_fetch_guestbook_list, error=error_fetch_guestbook_list)


json_result=jr.json_request(url=url)
print(json_result)