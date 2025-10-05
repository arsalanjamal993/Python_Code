# df["Column name"].mean()
# df["Column name"].sum()
# df["Column name"].min()
# df["Column name"].max()

import pandas as pd

data = {
    "Name":['mike', 'kite', 'skipe'],
    "Age":[28, 37, 23],
    "Salary":[30000,40000,50000],

}

df = pd.DataFrame(data)
avg_salary = df['Salary'].mean()
print(avg_salary)
