from lxml import etree
import requests
import pymysql
def getdel():
        url = 'https://book.douban.com/top250'
        data = requests.get(url).text
        s=etree.HTML(data)


        file=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div[1]/a/@title')
        print(file)
        return file
l1=getdel()
db = pymysql.connect("localhost", "root", "admin", "test", charset="utf8")
cs = db.cursor()
for i in range(len(l1)):


    sql = "insert into py(jing) values('{0}')".format(l1[i])

    cs.execute(sql)
    db.commit()
print('数据插入完成')
db.close()