from selenium import webdriver
from bs4 import BeautifulSoup
import pymysql
driver = webdriver.Chrome()
#访问网站
driver.get('http://huaban.com')
#获得网页信息
soup = BeautifulSoup(driver.page_source, "lxml")
#利用开发者工具找到我们需要的图片地址
results = soup.select('img[data-baiduimageplus-ignore="1"]')
#for r in results时发现有最后两个列表元素不是我们需要的网址，用[0:-2]去除
db = pymysql.connect("localhost", "root", "admin", "test", charset="utf8")
cs = db.cursor()
for r in results[0:-2]:
    sql = "insert into shu(shu) values('{0}')".format('http:'+r['src'])
    cs.execute(sql)
    db.commit()
print('数据插入完成')
db.close()
#关闭浏览器
driver.quit()