import os
import requests
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
from config import NASA_API_KEY

url = 'https://api.nasa.gov/DONKI/CMEAnalysis'
parameters = {
    'startDate': '',
    'endDate': '',
    'mostAccurateOnly': 'true',
    'speed': '500',
    'halfAngle': '30',
    'catalog': 'ALL',
    'api_key': NASA_API_KEY   
}

def request_data():
    response = requests.get(url, params=parameters)
    try:    
        data = response.json()
        df = pd.DataFrame(data)
        df.to_excel('dataframe.xlsx', index=False)
        print('всё ок')
    except:
        print('чёт не то ')


#request_data()
x = []
table = pd.read_excel('dataframe.xlsx')
for i in table['time21_5']:
    x.append(i[5:10])
y = table['speed']

plt.plot(x, y)
plt.show()
