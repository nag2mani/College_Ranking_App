import pandas as pd
# from home.models import *

# def sort_it():
file_path = "nirf.xlsx"
df = pd.read_excel(file_path)

print(df.columns)
column_to_sort = input("Enter the column name to sort by: ")

if column_to_sort in df.columns:
    sorted_df = df.sort_values(by=column_to_sort)

print(sorted_df.head)
print(df.columns)

