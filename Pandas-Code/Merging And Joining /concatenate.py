"""
Vertically (row-wise)
Horizaontally (Column wise)

pd.cancate([df1, df2], axis=0, ignore_index=True

[df1, df2] =
axis = 1


"""

# Vertically

import pandas as pd

df_region1 = pd.DataFrame({
    'CustomerID':[1,2],
    'Name':['bill', 'jhill',]



})

df_region2 = pd.DataFrame({
    'CustomerID':[3,4],
    'Name':['sonam', 'iqra',]

})
# concatenate vertically
df_concat = pd.concat = pd.concat([df_region1, df_region2], axis=1,  ignore_index=True)
print(df_concat)