from urllib.parse import urlencode
from .json_request import json_request


BASE_URL_DB_API = 'https://graph.facebook.com/v2.8'
LIMIT_REQUEST = 20
ACCESS_TOKEN = '%s|%s' % ('1946274482294048','ff576cb289bd807c03c040e1d6e7e9ee')

def fb_gen_url(base=BASE_URL_DB_API,node='', **params):   #기본페이지,페이지이름,....
    return '%s/%s/?%s' % (base,node,urlencode(params)) #urlendcode라이브러리는 알아서 인코딩 다해줌

def fb_name_to_id(pagename):
    url = fb_gen_url(node=pagename,access_token=ACCESS_TOKEN)

    json_result=json_request(url=url)
    #print(json_result)

    return json_result.get('id')

def fb_fetch_posts(pagename,since,until): #페이지관련이름, 언제부터, 언제까지
    url = fb_gen_url(node=pagename+ "/posts",
    fields = 'id,message,link,name,type,shares,created_time,reactions.limit(0).summary(true),comments.limit(0).summary(true)',
                     since=since, until=until,limit=LIMIT_REQUEST, access_token=ACCESS_TOKEN)

    while True:
        json_result=json_request(url=url)
        posts = json_result.get('data')
        paging= json_result.get('paging') #next라는게 없으면 다음페이지 안가게.

        yield posts


        url = paging.get('next')
        if url is None:
            break


