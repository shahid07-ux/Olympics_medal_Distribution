import matplotlib
matplotlib.use('TkAgg')  # 🔥 FIX

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Program started...")

df = pd.read_csv("Tokyo Medals 2021.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Create Total column
df['Total'] = df['Gold Medal'] + df['Silver Medal'] + df['Bronze Medal']

df_sorted = df.sort_values(by="Total", ascending=False)
top10 = df_sorted.head(10)

x = np.arange(len(top10['Country']))
width = 0.25

plt.figure(figsize=(12,6))

plt.bar(x - width, top10['Gold Medal'], width, label='Gold')
plt.bar(x, top10['Silver Medal'], width, label='Silver')
plt.bar(x + width, top10['Bronze Medal'], width, label='Bronze')

plt.xticks(x, top10['Country'], rotation=45)

plt.legend()

print("Showing graph...")
plt.show()