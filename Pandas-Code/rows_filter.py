import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Age": [25, 30, 35, 40, 28, 32],
    "Salary": [50000, 60000, 70000, 80000, 55000, 65000],
    "performance score": [87, 95, 78, 88, 92, 85],

}

df = pd.DataFrame(data)

high_salary = df[df['Salary'] > 50000]
print("Employee with salary > 50000:")
print(high_salary)

# filtered rows salary > 50k & age > 30
filtered = df[(df['Age'] > 30) & (df['salary'] > 50000)]
print(f"Employee list Age > 30 + Salary > 50000")
print(filtered)

#  using Or Condition
filtered_or = df[(df['Age'] > 35) | (df["performance_score > 90"])]
print(filtered_or)
