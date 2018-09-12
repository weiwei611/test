# encoding=utf8
from selenium import webdriver
import datetime, time

dic = {}
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.maximize_window()
driver.get(
    'https://detail.tmall.com/item.htm?spm=a1z10.1-b-s.w19370147-18846483048.2.5ccf70bfVlqaMZ&id=568960237310&sku_properties=5919063:1173069333&scene=taobao_shop')
driver.implicitly_wait(30)
starttime = datetime.datetime.now()
driver.find_element_by_xpath("//*[@id='J_TabBar']/li[3]/a").click()
for i1 in range(2, 5):
    print(i1)
    for i in range(1, 16):
        try:
            l1 = driver.find_element_by_xpath(
                "//*[@id='J_Reviews']/div/div[6]/table/tbody/tr[%s]/td[1]/div[1]/div[1]" % i).text
            x = str(i1 - 1) + "--" + str(i)
            dic[x] = l1
        except:
            pass
    driver.implicitly_wait(30)
    driver.find_element_by_css_selector("a[data-page='%d'][href]" % i1).click()
    driver.implicitly_wait(30)

    # x = driver.find_element_by_class_name("rate-page-next").text
    # print(x)
endtime = datetime.datetime.now()
print(dic)
print((endtime - starttime).seconds)
driver.quit()








# driver.create_web_element(u"下一页").click()
#driver.create_web_element('下一页')

# while True:
#     k = 5
#     l = driver.find_element_by_xpath("//*[@id='J_Reviews']/div/div[7]/div/a[%s]" % k).text
#     k += 1

# f1 = open('texts.txt', 'w', encoding='utf-8')
# print(driver.title)
#driver.implicitly_wait(30)
#f1 = open('texts.txt', 'w +')
# f1 = open('texts.txt', 'a')
# f1.writelines(str(i) + ',' + l + '\n')