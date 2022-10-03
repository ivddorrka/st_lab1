import pandas as pd
import csv
import matplotlib.pyplot as plt
  

df_firstn = pd.read_csv("~/Downloads/deterministic02 - diff.csv").transpose()
# print(df_firstn.head())

df_firstn.to_csv("diffusion.csv")

with open('diffusion.csv', newline='') as f:
    reader = csv.reader(f)
    data = [list(row) for row in reader]


for i in range(2, len(data)):
    # print(data[i], i)
    if ',' in data[i][0]:
        data[i][0] = data[i][0].replace(',', '.')
    data[i][0] = float(data[i][0][:3])

    if ',' in data[i][3]:
        data[i][3] = data[i][3].replace(',', '.')
    data[i][3] = float(data[i][3][:3])

    if ',' in data[i][1]:
        data[i][1] = data[i][1].replace(',', '.')
    data[i][1] = float(data[i][1])
    
    if ',' in data[i][2]:
        data[i][2] = data[i][2].replace(',', '.')
    data[i][2] = float(data[i][2])


# print(data[3:6])

# last_i = ''

# 0.70 1.00 1.50 2.00
ss = 0.7
bd = 0.5
lst_chosen = [i for i in data if i[0]==ss]

lst_al_05 = [i for i in lst_chosen if i[1]==bd]


# print(lst_al_05)

last_i = 0
lst_keys = []
lst_values = []
for i in lst_al_05:
    if i[2]==last_i:
        lst_values[-1] += 0.2*i[3]
    else:
        lst_keys.append(i[2])
        lst_values.append(0.2*i[3])
        last_i = i[2]

print(lst_keys)
print(lst_values)


plt.plot(lst_keys, lst_values)
plt.xlabel("Num of agents")
plt.ylabel("time to reach boarder in ticks")
plt.title(f"stepsize = {ss}, lambda = {bd}")
plt.show()