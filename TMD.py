print("Running : requests")
import requests

url = "http://data.tmd.go.th/api/WeatherToday/V1/"

payload = ""
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "63cad96b-461e-4396-b9b5-d678080c2d03"
    }

response = requests.request("GET", url, data=payload, headers=headers)
print("Running : response.json")
#print(response.text)
data = response.json()
#print(type(data))
print("Running : dict")
dict_1=data

#import csv
import csv
#i = 'D:/TMD_water.csv'
#with open(i, 'w',encoding="utf-8") as file:
#    file.write('NO,NAME ,Latitude ,Longitude ,Date \n')
#    file.write('1,Anon bianglae ,18.222 ,100.2 ,10/29/2019 \n')
#file.close()


#output path
output = 'C:/Users/sattawat.a/Desktop/Python/TMD/tmd_today.csv'


#writ csv file
with open(output, 'w',encoding="utf-8") as file:
    file.write('Province,StationNameTh ,Latitude ,Longitude ,Date  ,Rainfall\n')
    for line in data['Stations']:
        print(line)
        try:
            file.write(str(line["StationNameEng"])+','+str(line["StationNameTh"])+','+str(line["Latitude"]["Value"])+','+str(line["Longitude"]["Value"])+','+str(line["Observe"]["Time"])+','+str(line["Observe"]["Rainfall"]["Value"])+','+str('\n'))
        except:
            pass
    
file.close()