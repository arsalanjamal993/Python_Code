import pandas as pd


data = {
    "Name": ["John", "Jane", "Doe"],
    "Age": [28, 34, 29],
    "City": ["New York", "Los Angeles", "Chicago"]


}

df = pd.DataFrame(data)
print(df)

# df.to_csv("output.csv", index=False)
# df.to_excel("output.xlsx", index=False)
df.to_json("output.json", index=False)