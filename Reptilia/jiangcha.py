import requests

eg=requests.get('url','https://detail.tmall.com/item.htm?spm=a1z10.1-b-s.w19370147-18846483048.2.5ccf70bfVlqaMZ&id=568960237310&sku_properties=5919063:1173069333&scene=taobao_shop')
# driver.implicitly_wait(30)
# driver.find_element_by_xpath("//*[@id='J_TabBar']/li[3]/a").click()
print(eg.content)