import requests
import json

header = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
    
url = 'https://ecapi-cdn.pchome.com.tw/fsapi/cms/onsale'

data = requests.get(url,headers=header).text

goods = json.loads(data)
goods = goods['data']

for row in goods:
    time = row['time']
    print('-'*30)
    print('限時搶購時間:',time)
    print('-'*30)
    for r in row['products']:
        name = r['name']
        image = r['image']
        origin = r['price']['origin']
        onsale = r['price']['onsale']
        print('商品名稱:',name)
        print('商品圖片:',image)
        print('商品原價:',origin)
        print('商品特價:',onsale)
        print()
