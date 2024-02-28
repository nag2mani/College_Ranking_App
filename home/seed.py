import pandas as pd
from home.models import *

# def sort_it():
file_path = "nirf.xlsx"
df = pd.read_excel(file_path)

# print(df.columns)
# column_to_sort = input("Enter the column name to sort by: ")

# if column_to_sort in df.columns:
#     sorted_df = df.sort_values(by=column_to_sort)

# print(sorted_df.head)

col = ['Original_Rank', 'New_Rank', 'Change', 'College', 'Fees', 'Faculty',
       'SS', 'FSR', 'FQE', 'FRU', 'PU', 'QP', 'IPR', 'FPPP', 'GPH', 'GUE',
       'GMS', 'GPHD', 'RD', 'WD', 'ESCS', 'PCS', 'PR', 'xx', 'Total']

# Assuming df is your DataFrame containing the data
for index, row in df.iterrows():
    Colleges_model.objects.create(
        Original_Rank=row['Original_Rank'],
        New_Rank=row['New_Rank'],
        Change=row['Change'],
        College=row['College'],
        Fees=row['Fees'],
        Faculty=row['Faculty'],
        SS=row['SS'],
        FSR=row['FSR'],
        FQE=row['FQE'],
        FRU=row['FRU'],
        PU=row['PU'],
        QP=row['QP'],
        IPR=row['IPR'],
        FPPP=row['FPPP'],
        GPH=row['GPH'],
        GUE=row['GUE'],
        GMS=row['GMS'],
        GPHD=row['GPHD'],
        RD=row['RD'],
        WD=row['WD'],
        ESCS=row['ESCS'],
        PCS=row['PCS'],
        PR=row['PR'],
        xx=row['xx'],
        Total=row['Total']
    )

