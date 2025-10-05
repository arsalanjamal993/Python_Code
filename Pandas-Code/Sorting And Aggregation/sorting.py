import pandas as pd

data = {
    "Name": ['jammy', 'noble', 'manjara'],
    "Age": [10, 20, 30],
    "Salary": [10000, 20000, 30000]
}

df = pd.DataFrame(data)
df.sort_values(by="Age", ascending=False, inplace=True)
print("Sorted Age by descending")
print(df)
