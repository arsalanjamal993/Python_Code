# Step 1 sample data frame 

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Age": [25, 30, 35, 40, 28, 32],
    "Salary": [50000, 60000, 70000, 80000, 55000, 65000],
    "performance score": [87, 95, 78, 88, 92, 85],

}

df = pd.DataFrame(data)

print("Sample DataFrame:")
print(df)
print("Descriptive Statistics:")
print(df.describe())    