#파이썬에서 날짜와 시간을 다루는 방법
import datetime

now=datetime.datetime.now()
print(now)

#문자열 포맷팅
nowdate=now.strftime('%Y-%m-%d')
print(nowdate)