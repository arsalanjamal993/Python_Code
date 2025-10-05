# adding column
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Age": [25, 30, 35, 40, 28, 32],
    "Salary": [50000, 60000, 70000, 80000, 55000, 65000],
    "performance score": [87, 95, 78, 88, 92, 85],

}

df = pd.DataFrame(data)
# Square brackets df["Column_Name"] =  some_data
print(df)

df["Bonus"] = df['Salary'] * 0.1
print(df)

# using insert()
# df.insert(loc, "Column_Name", some_data)
df.insert(0, "Employee ID", [10,20,30,40,50,60])
print(df)

