import pandas as pd

#  read data from .csv file into a pandas dataframe
# df = pd.read_csv("employee_data.csv", encoding="latin1")
# df = pd.read_excel("random_data.xlsx")
df  = pd.read_json("random_data.json")
print(df)