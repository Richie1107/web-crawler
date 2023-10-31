import requests
import json

header = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
url = 'https://ecshweb.pchome.com.tw/search/v4.3/all/results'

serchName = input('輸入想查詢的商品:')


for i in range(1,5):
    param = {
        'q': serchName,
    'page': i,
    'sort': 'rnk/dc'
        }
    
    data = requests.get(url,headers=header,params=param).text
    pchome = json.loads(data)
    
    goods = pchome['Prods']
    
    for items in goods:
        title = items['Name']
        photo = 'https://cs-a.ecimg.tw'+items['PicB']
        price = items['Price']
        info = items['Describe']
        
        print(title)
        print(photo)
        print(price)
        print(info)
        print()
        print()
        