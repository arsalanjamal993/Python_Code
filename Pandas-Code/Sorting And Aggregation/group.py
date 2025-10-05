import pandas as pd

data = {
    "Name": ['jammy', 'noble', 'manjara', 'gnome', 'kde', 'cinnamon'],
    "Age": [34, 22, 28, 27, 24, 44],
    "Salary": [40000, 20000, 30000, 1200000, 70000, 440000]
}

df = pd.DataFrame(data)
grouped = df.groupby("Age")["Salary"].sum()
print(grouped)
"""
df.groupedby("Age")
age = 22 > [45000]
age = 28 [50,0000]




"""