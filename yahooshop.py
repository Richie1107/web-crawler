import requests
import json
from bs4 import BeautifulSoup



url =  'https://tw.buy.yahoo.com/search/product'


header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    
    
param = {}

p = input('請輸入查詢的商品：')

param['p'] = p


data = requests.get(url,params=param,headers=header).text

soup = BeautifulSoup(data,'html.parser')

ul = soup.find(id='isoredux-data').get('data-state')
with open ('yahoo.txt','w') as fObj:
    fObj.write(ul)
yahoo = json.loads(ul)
comm = yahoo['search']['ecsearch']['hits']

for item in comm:
    link = item['pres_data']['producturl']
    title = item['ec_title']
    photo = item['ec_image']
    price = item['ec_price']
    info = item['ec_description']
    price = price.replace('.0','')
    print('商品名稱:',title)
    print('價格:$'+price)
    print('照片連結:',photo)
    print('商品簡介:',info)
    print('商品連結:',link)
    print()