import pandas as pd
import matplotlib.pyplot as plt


lsts, gender, height = [], [], []
name = 'name'
try:
    with open(f'./files/{name}.csv', 'r') as file:
        lst = file.readlines()
        for i, f in enumerate(lst):
            lsts.append(f.split(','))
            gender.append(lsts[i][1])
            height.append(int(lsts[i][3]))
except:
    print('файл не открывается')

'''x = ['male', 'female']
y = [gender.count('Male'), gender.count('Female')]
plt.bar(x, y, label='gender')
plt.legend()
plt.show()'''

x = sorted(height)

plt.figure(figsize=(12, 7))
plt.plot(x)
plt.show()