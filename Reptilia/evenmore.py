from selenium import webdriver
from Reptilia.Projects1 import *

def frist():
    driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    #driver.maximize_window()
    driver.get(
        'https://detail.tmall.com/item.htm?spm=a1z10.1-b-s.w19370147-18846483048.2.5ccf70bfVlqaMZ&id=568960237310&sku_properties=5919063:1173069333&scene=taobao_shop')

    driver.implicitly_wait(30)
    L = []
    driver.find_element_by_xpath("//*[@id='J_TabBar']/li[3]/a").click()
    for i in range(1, 21):
        try:
            l = driver.find_element_by_xpath(
                "//*[@id='J_Reviews']/div/div[6]/table/tbody/tr[%s]/td[1]/div[1]/div[1]" % i).text
            L.append(l)
        except:
            pass
    driver.quit()
    return L


def many_img(data,beg = 0):
    #用于匹配多图中的url
    try:
        many_img_str = ''
        while True:
            src1 = data.index('http',beg)
            src2 = data.index(' /><br /> <img src=',src1)
            many_img_str += data[src1:src2]+'|' # 多个图片的url用"|"隔开
            beg = src2
    except ValueError:
        return many_img_str