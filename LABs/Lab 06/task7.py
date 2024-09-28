import pandas as pd

df = pd.read_excel("Employee Sample Data.xlsx")

specified_year_employee = df[df["Hire Date"].dt.year == 2019]
print(specified_year_employee)