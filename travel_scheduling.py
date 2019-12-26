import pandas as pd
import numpy as np

df_city_site = pd.read_csv("site_city.csv", encoding="big5")
site_city_dict = {}
city_site_dict = {}

# 創建 dict 是縣市對應裡面的所有景點
for i in range(len(df_city_site)):
    site_name = df_city_site.iloc[i][1]
    city_name = df_city_site.iloc[i][0]
    site_city_dict[site_name] = city_name
    try:
        city_site_dict[city_name[:2]].append(site_name)
    except:
        city_site_dict[city_name[:2]] = [site_name]

        
city_order = [ '基隆', '臺北', '新北', '桃園', '新竹', '苗栗', '臺中', '南投', '彰化',
               '雲林', '嘉義', '臺南', '高雄', '屏東', '臺東', '花蓮', '宜蘭']
# read file
df_site_distance = pd.read_csv("travel_sites.csv", encoding="big5")

# 把第一行當作 index
df_site_distance.set_index("Unnamed: 0", inplace=True)

# 去掉 nan 值(有些列是空的的狀況)
df_site_distance = df_site_distance.dropna(axis=0, how="any")
df_site_distance = df_site_distance.dropna(axis=1, how="all")

'''
# 取值方法
print(df_site_distance.loc['101大樓', '木柵動物園'])
print(df_site_distance.iloc[0, 1])
'''

# 所有景點的 list
site_list = list(df_site_distance.keys())

# - - - - #

import random
from pulp import *

satisfaction = list(np.zeros(len(df_site_distance.keys())))
# create 隨機滿意度變數 list
for i in range(len(satisfaction)):
    satisfaction[i] = round(random.uniform(0, 10), 1)  # 取小數兩位

# create 2-D variables list
length = len(df_site_distance.keys())

# create a new model
prob = pulp.LpProblem("travel routines scheduling", pulp.LpMaximize)

# decision variable
variable_list = []
for num_source in range(length):
    tmp_list = []  # 因為是二維的，所以先建好一維再依序加入
    for num_destination in range(length):
        variable_name = site_list[num_source] + "-" + site_list[num_destination]
        tmp = pulp.LpVariable(variable_name, lowBound=0, cat="Binary")
        tmp_list.append(tmp)
        # infinite distance (A -> A)
        if(num_source == num_destination):
            df_site_distance.iloc[num_source, num_destination] = float("inf")
            
    variable_list.append(tmp_list)

'''    
# 變數名稱查看    
print(variable_list[0][:10])     
print(len(satisfaction))
print("finish")
'''

# objective(滿意度最大化)
tmp_obj = 0
for i in range(length):
        tmp_obj += lpSum([satisfaction[j] * variable_list[i][j] for j in range(length)])
prob += tmp_obj


# constraint

for num in range(length):
    # 景點行列各別總和等於 0 或 1  variables_list
    prob += lpSum([variable_list[num][j] for j in range(length)]) <= 1  # column
    prob += lpSum([variable_list[j][num] for j in range(length)]) <= 1  # row
    
    # 景點有進有出 (### 但是還沒處理完三個以上景點的 loop ###)
    tmp1, tmp2 = 0, 0
    for j in range(length):
        tmp1 += variable_list[num][j]
        tmp2 += variable_list[j][num]
        prob += (variable_list[num][j] + variable_list[j][num] <= 1)  # 避免兩個景點之間互相抵達
    prob += (tmp1 == tmp2)

# 每個縣市都要逛到(有進有出):從外縣市、離開此縣市，縣市之間有順序性
for city in city_site_dict:
    flag = True
    for next_city in city_site_dict:
        city_tmp_sum_in, city_tmp_sum_out = 0, 0
        if(next_city == city):
            continue
        # 某個縣市的所有景點針對另一個縣市所有的景點進出計算(跨縣市)    
        for site in city_site_dict[city]:
            index_site = site_list.index(site)
            city_tmp_sum_out += lpSum(variable_list[index_site][site_list.index(next_site)] 
                                     for next_site in city_site_dict[next_city])
            city_tmp_sum_in += lpSum(variable_list[site_list.index(next_site)][index_site] 
                                     for next_site in city_site_dict[next_city])
        
        num_in, num_out = 0, 0
        if(next_city == city_order[(city_order.index(city)+1)%len(city_order)]):
            num_out = 1
        if(city == city_order[(city_order.index(next_city)+1)%len(city_order)]):
            num_in = 1
            
        prob += (city_tmp_sum_in == num_in)
        prob += (city_tmp_sum_out == num_out)
    
# 距離成本
distance = 0
for i in range(length):
    for j in range(length):
        if(i == j):
            distance += 1000 * variable_list[i][j]
            continue
        distance += df_site_distance.iloc[i, j] * variable_list[i][j]
    
prob += (distance <= float(1000))

prob.solve()

print("Status:", LpStatus[prob.status])
total = 0
distance_total = 0
bool_list = [0] * len(site_list)  # 判斷走幾次
global final_dict
final_dict = {}

for site in site_list:
    final_dict[site] = ["", ""]
    
# 計算總距離的 function + 存入景點進出狀況到 final_dict
def add(routine, distance_total, bool_list):
    routine = routine.split("_")
    bool_list[site_list.index(routine[0])] += 1
    bool_list[site_list.index(routine[1])] += 1
    #print(df_site_distance.loc[routine[0], routine[1]])
    distance_total += df_site_distance.loc[routine[0], routine[1]]
    
    final_dict[routine[0]][1] = routine[1]  # 抵達
    final_dict[routine[1]][0] = routine[0]  # 出發

    return distance_total

final_site_list = []    
for v in prob.variables():
    if(int(v.varValue) == 1):
        #print(v.name, "=", int(v.varValue))
        total += 1
        distance_total = add(str(v.name), distance_total, bool_list)
        final_site_list.append(str(v.name).split("_")[0])
        
# 把景點順序印出來
first =  "嘉義火車站"  # 有在路線當中隨便一個景點丟進來
this_site = first
next_site = final_dict[first][1]
final_site_list.remove(first)
print(first + " -> " + next_site)
this_site = next_site
next_site = final_dict[this_site][1]
counting = 0

while(this_site != first and counting <= 50):
    print(this_site + " -> " + next_site)
    final_site_list.remove(this_site)
    this_site = next_site
    next_site = final_dict[this_site][1]
    counting += 1
    
print("count:", counting)
print(final_site_list)  # 剩下有問題沒接起來的景點(自己有小 loop 的)

'''
比如範例裡面臺南的 '赤崁樓', '林百貨', '國華街' 三個自己在小圈圈
'''
print('obj=',round(value(prob.objective), 2))  # 滿意度
print("total sites:", total)                   # 經過總景點數
print("distance:", distance_total)             # 總里程
print(bool_list)
final_site_list = set(final_site_list)
print(final_site_list, len(final_site_list))