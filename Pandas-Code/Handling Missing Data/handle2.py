# fillna()
# fillna(value, inplace=True)
import pandas as pd

data = {
    "Name": ["Alice", None, "Charlie", "David", "Eva", "Frank"],
    "Age": [25, None, 35, 40, 28, 32],
    "Salary": [50000, None, 70000, 80000, 55000, 65000],
    "performance score": [87, None, 78, 88, 92, 85],

}

df = pd.DataFrame(data)
print(df)

# df.fillna(0, inplace=True)
df['Age'].fillna(df['Age'].mean(), inplace=True)
print(df)



