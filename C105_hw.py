import csv
from numpy import tile
import plotly.express as px
import pandas as pd
import math


with open('data.csv',newline='') as f:
    file = csv.reader(f)

    data= list(file)

file_data=[]

for q in data:
    for n in q:
        file_data.append(n)


print('Data:',file_data)

num_of_values=len(file_data)

sum_of_values=0


for i in file_data:
    sum_of_values += float(i)

print('sum:',sum_of_values)
print('num:',num_of_values)


mean = sum_of_values / num_of_values


squared_list = []

for x in file_data:
    a  = int(x) - mean

    a = a ** 2

    squared_list.append(a)


sum = 0

for i in squared_list:
    sum = sum+i

result = sum / num_of_values

standard_dev=math.sqrt(result)

print(standard_dev)





