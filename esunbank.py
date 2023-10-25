from bs4 import BeautifulSoup
import requests

url = 'https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates'

header={
        'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
        }
#加入標頭，模擬瀏覽器
data = requests.get(url,headers=header).text
# print(data)
soup = BeautifulSoup(data,'html.parser')

allRate = soup.find(id='exchangeRate')
trs = allRate.find('tbody').find_all('tr')[1:]

    
for row in trs:
    tds = row.find_all('td',recursive=False)
    if len(tds) == 4:
        print(tds[0].text.strip().split()[0])
        print(tds[1].text.strip())
        print(tds[2].text.strip())
        print(tds[3].text.strip())
        print()


#不做內迴圈的方法:recursive=False (關閉遞迴搜尋,不抓子節點)  
#去除前後空白.strip()<--去除前後空白,中間空白無法
#.split()<--切割空白
