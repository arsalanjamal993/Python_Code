import pandas as pd

data = {
    "Name": ["John", "Jane", "Doe"],
    "Age": [28, 34, 29],
    "City": ["New York", "Los Angeles", "Chicago"]


}

df = pd.DataFrame(data)
print("Displaying the info of the data set")
print(df.info())
