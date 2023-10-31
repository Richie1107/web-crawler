import requests
import json
from datetime import datetime
import csv

url = 'https://www.thsrc.com.tw/TimeTable/Search'

header = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
    
stationName={'南港':"NanGang",'台北':"TaiPei",'板橋':"BanQiao",'桃園':"TaoYuan"\
             ,'新竹':"XinZhu",'苗栗':"MiaoLi",'台中':"TaiZhong",\
             '彰化':"ZhangHua",'雲林':"YunLin",'嘉義':"JiaYi",'台南':"TaiNan"\
             ,'左營':"ZuoYing"}
print(stationName.keys())

depName = input('輸入起始站名:')
if depName in stationName:
    depName = depName
else:
    print('無法找到站名請重新輸入')
    depName = input('輸入起始站名:')

destName = input('輸入到站名:')
if destName in stationName:
    destName = destName
else:
    print('無法找到站名請重新輸入')
    destName = input('輸入到站名:')
#讀取時間韓式
datetime = datetime.now()
strdate = datetime.strftime('%Y/%m/%d')

inputTime = input('輸入想查詢的時間(H:M):')
if len(inputTime) == 0: 
    time = datetime.strftime('%H:%M')
else:
    time = inputTime
param = {'SearchType': 'S',
'Lang': 'TW',
'StartStation': stationName[depName],
'EndStation': stationName[destName],
'OutWardSearchDate': strdate,
'OutWardSearchTime': '21:30',
'ReturnSearchDate': '2023/10/29',
'ReturnSearchTime': '22:30'}

data = requests.post(url,data=param,headers=header).text

thsrc = json.loads(data)
items = thsrc['data']['DepartureTable']['TrainItem']

fileName = 'thrsc.csv'
fobj = open(fileName,'w',newline='')
csvWrite = csv.writer(fobj)
csvWrite.writerow(['列車號','起始站->終點站','出發時間','抵達時間','旅行時間','區間各站'])

    
for row in items:
    if row['DepartureTime']>time:
        station = ['區間各站:',depName,'->']
        
        for st in row['StationInfo']:
            if st['Show']and row['DepartureTime'] < st['DepartureTime'] and row['DestinationTime']>st['DepartureTime']:
                station.append(st['StationName'])
                station.append('->')
        station.append(destName)
        #st['show]本身等於bool不用給Ture也行
        print('列車號:',row['TrainNumber'])
        print(depName,'->',destName)
        print('出發時間:',row['DepartureTime'])
        print('抵達時間:',row['DestinationTime'])
        print('旅行時間:',row['Duration'])
        for sts in station:
            print(sts,end='')
        print()
        print('-'*30)
        csvWrite.writerow([row['TrainNumber'],[depName,'->',destName],row['DepartureTime'],row['DestinationTime'],row['Duration'],station])
        
        
fobj.close()        
        