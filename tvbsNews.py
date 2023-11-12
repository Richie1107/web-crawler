import requests
from bs4 import BeautifulSoup
import db
from datetime import datetime

url = 'https://news.tvbs.com.tw/realtime'


header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }

data = requests.get(url,headers=header).text
soup = BeautifulSoup(data,'html.parser')

news = soup.find('div',{'class':'news_list'})

news = news.find('div',{'class':'list'})




allli = news.find_all('li')

for row in allli:
    a = row.find('a')
    if a != None:

        link ='https://news.tvbs.com.tw' + a.get('href')
        title = a.find('h2').text.strip()
        photo = a.find('img').get('data-original')
        post_date = datetime.today()
        
        sql = "select * from news where title='{}' and platform='Tvbs'  ".format(title)
        
        db.cursor.execute(sql)
        
        
        if db.cursor.rowcount == 0:  # 表示在資料表中沒有此筆資料
        
            sql = "insert into news(title,link_url,post_date,platform,photo_url) values('{}','{}','{}','Tvbs','{}')".format(title,link,post_date,photo)
            
            db.cursor.execute(sql)
            db.conn.commit()
        
        
db.conn.close()         
        
        