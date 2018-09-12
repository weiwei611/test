# coding = UTF-8
import urllib.request
import re,os



page = urllib.request.urlopen("http://www.zhoujingen.cn/blog/6164.html/comment-page-1#comment-104678")
html = page.read()
page.close()

#url = ("http://www.math.pku.edu.cn/teachers/lidf/docs/textrick/index.htm")
#print(html.decode("gbk"))
print(html.decode("utf-8"))

# a = re.compile(r'_',re.I)
# b = a.match('_happy')
# print(b.group())