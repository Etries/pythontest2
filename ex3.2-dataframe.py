#! /usr/bin/env python3

import pandas as pd
from matplotlib import pyplot as plt


df1 = pd.read_csv("dataset.csv", low_memory = False)
col_keys = [x for x in df1.columns if ('Households_With_Internet_Access' in x and 'Perc_Households_With_Internet_Access' not in x)]
df2 = df1[df1['County'] == 'Carlow' ][col_keys]
df3 = pd.concat([df2, pd.DataFrame(df2.sum(numeric_only = True)).T], ignore_index = True)
df3.rename(index={210 : "Total"})
df3.to_csv("new_dataset.csv", header =True, index = None)
new_df = pd.read_csv("new_dataset.csv")
new_df.rename(index = {210:"Total"}, inplace = True)
chart_df = pd.DataFrame(new_df.loc['Total']).T
chart_df.plot(kind ="bar")
plt.ylabel("Number of Households")
plt.yticks(rotation=45)
plt.xticks(rotation=0)
plt.show()
