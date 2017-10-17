import analysis_fb.collection.crawler as crawler



pagename='jtbcnews'
since='2016-10-01'
until='2017-10-01'


items = [('jtbcnews','2017-10-01','2017-10-12'),('chosun','2017-10-01','2017-10-12')]


for pagename,since,until in items:
    crawler.crawling(pagename,since,until)
