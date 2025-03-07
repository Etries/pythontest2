import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


df = pd.read_csv("dataset.csv")

keys_string = [x for x in df.columns if "Households_With_Internet_Access" 
               in x and "Perc_Households_With_Internet_Access" not in x]


df2 = df.loc[df["County"]  == "Carlow" , keys_string]
# df1 = df2._append(df2.sum(axis=0, numeric_only= True, skipna=True), ignore_index = True)
df2 = pd.concat([df2, (df2.sum(axis=0, numeric_only= True, skipna=True).to_frame()).transpose()], axis=0)
new_columns = ["Broadband", "Other_connection", "with_out access", "Not_stated", "Total_Access"]
df2.columns = new_columns
print(df2.rename(index = {df2.index[-1]:"Total"}, inplace = True))

df2.to_csv("Carlow_dataset.csv")
