# -*- coding: utf-8 -*-
"""
Created on Tue May 20 03:52:03 2025

@author: USER
"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pointbiserialr

# Step 1: 讀取 Excel 資料
file_path = r"C:\Users\USER\Desktop\英文作業\DATA.xlsx"
df = pd.read_excel(file_path)

# 確認欄位名稱（可依實際內容做修正）
print(df.columns)

# Step 2: 將 Gender 轉換為二元變數（例如 Male=1, Female=0）
df['Gender_binary'] = df['Gender'].map({'male': 1, 'female': 0})



# Step 3: 計算 point-biserial correlation
r, p = pointbiserialr(df['Gender_binary'], df['Kiss Count'])

print(f"Point-biserial correlation r ≈ {r:.3f}")
print(f"p-value ≈ {p:.3f}")

# Step 4: 計算分組描述性統計
desc_stats = df.groupby('Gender')['Kiss Count'].agg(['mean', 'std', 'count'])
print("\n分組描述性統計：")
print(desc_stats)

# Step 5: 繪製 Boxplot 圖
plt.figure(figsize=(6, 5))
sns.boxplot(x='Gender', y='Kiss Count', data=df, palette='Set2')
plt.title("Kiss count by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of People Kissed")
plt.tight_layout()
plt.savefig("kiss_count_by_gender_boxplot.png")  # 儲存圖表
plt.show()
