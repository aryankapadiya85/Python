import pandas as pd

data = pd.read_excel("students.xlsx")

print("Columns:")
print(data.columns)

print("\nData Types:")
print(data.dtypes)
