''' 
Create a python script to do ordinal encoding and one hot encoding 
using basic python functions and just pandas and numpy libraries
'''

import pandas as pd


data = pd.read_csv("../melb_data.csv")

categorical_cols = [col for col in data.columns if data[col].dtype == "object" and data[col].nunique() < 10]
print("\n\n\nBefore -\n")
print(data[categorical_cols])

all_new_col_added = []
for col in categorical_cols:
    new_cols_to_add = list(set(data[col]))

    for c in new_cols_to_add:
        new_col_val = []
        for p in data[col]:
            new_col_val.append(1 if p == c else 0)
        data[c] = new_col_val

    data.drop(col, axis=1)
    all_new_col_added.extend(new_cols_to_add)


print("\n\n\nAfter -\n")
print(data[all_new_col_added])
# data[all_new_col_added].to_csv("output_onehot.csv", sep='\t', encoding='utf-8')