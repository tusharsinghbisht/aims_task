''' 
Create a python script to do ordinal encoding and one hot encoding 
using basic python functions and just pandas and numpy libraries
'''

import pandas as pd


data = pd.read_csv("../melb_data.csv")

categorical_cols = [col for col in data.columns if data[col].dtype == "object" and data[col].nunique() < 10]
print("\n\n\nBefore -\n")
print(data[categorical_cols])

for col in categorical_cols:
    c = 1
    d = {}
    for v in set(data[col]):
        d[v] = c
        c+=1
    # print(d)
    data[col] = [d[x] for x in data[col]]

print("\n\n\nAfter -\n")
print(data[categorical_cols])