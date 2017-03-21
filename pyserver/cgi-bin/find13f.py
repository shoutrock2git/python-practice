#!/usr/bin/env python
# coding: utf-8

#2.xでは .encode("utf-8")、.encode("shift-jis")などとすることで、出力するHTMLのエンコーディングを変更出来たのですが、
#3.xではこのテクニックは使えず、出力のエンコーディングはsys.stdout.encodingに固定です。
#では、3.xではどうすれば良いかというと、sys.stdoutの値自体を変えてしまえば良いのです。
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
#自動でutf-8にエンコードされて出力される


import cgi
from datetime import datetime

html_body="""
<html><meta charset="utf-8"><body>
%s
</body></html>"""

content=''

form=cgi.FieldStorage()
year_str=form.getvalue('year','')
if not year_str.isdigit():
	content="西暦を入力してください"
else:
	year=int(year_str)
	friday13=0
	for month in range(1,13):
		date=datetime(year, month, 13)
		if date.weekday()==4:
			friday13+=1
			content+="%d年%d月13日は金曜日です" % (year, date.month)
			content+="<br>"

	if friday13:
		content+="%d年には合計%d個の13日の金曜日があります" % (year, friday13)
	else:
		content+="%d年には13日の金曜日がありません"

print ("Content-type: text/html; charset=utf-8\n")
print (html_body % content)
