# pd.merge(df1, df2 on="Column_Name", how="type of join")
import pandas as pd

df_customers = pd.DataFrame({
    'CustomerID':[1,2,3],
    'Name':["bill","steve","linus"]


})

# order dataframe
df_orders = pd.DataFrame({
    'CustomerID':[1,2,3],
    'OrderAmount':[250,654,387]
})

# merge
# df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="inner")
# df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="outer")
# df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="left")
df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="right")

print("outer join")
print(df_merged)

"""
1df = m rows
2df = n rows
m * n rows 
"""