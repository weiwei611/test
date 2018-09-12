# coding = UTF-8
import urllib.request
import re, pdfkit

count = 0
page = urllib.request.urlopen("http://www.zhoujingen.cn/blog/")
html = page.read()
page.close()
#print(html.decode("gbk"))
#print(html.decode("utf-8"))
reg = r'(?:href|HREF)=("?(?:http://)?.+?\头手心练习)'
url_re = re.compile(reg)
url_lst = url_re.findall(html.decode("utf-8"))
print(url_lst)
for i in url_lst:
    count += 1
    i1 = i.split(">")[0]
    w = urllib.request.urlopen(eval(i1)).read()
    with open(str(count) + "file_name".replace('/', '_') + ".html", "wb") as f:
        f.write(w)
pdfkit.from_file('1file_name.html', 'test.pdf')

