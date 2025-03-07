import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


df = pd.read_csv("Carlow_dataset.csv")
df.rename(index= {df.index[-1]: "Total"}, inplace= True)
total_df = df.loc["Total"]
total_df = pd.to_numeric(total_df, errors="coerce")
print(total_df)
plt.plot(total_df)
plt.xlabel("Total")
plt.xticks(rotation = 30)
plt.show()
