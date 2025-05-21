# -*- coding: utf-8 -*-
"""
Created on Tue May 20 04:03:29 2025

@author: USER
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# 讀取資料
file_path = r"C:\Users\USER\Desktop\英文作業\DATA_Kiss_count_gender_and_IQ.xlsx"
df = pd.read_excel(file_path)

# 標準化欄位名稱（去除空格）
df.columns = df.columns.str.strip()

# 轉換相關欄位為數值並清理缺失
df['Kiss Count'] = pd.to_numeric(df['Kiss Count'], errors='coerce')
df['Age of First Kiss'] = pd.to_numeric(df['Age of First Kiss'], errors='coerce')

# 濾除缺失值
clean_df = df[['Kiss Count', 'Age of First Kiss']].dropna()

# 檢查是否有足夠的資料進行分析
if len(clean_df) >= 2:
    # 計算皮爾森相關係數
    r, p = pearsonr(clean_df['Age of First Kiss'], clean_df['Kiss Count'])
    print(f"Pearson correlation r ≈ {r:.3f}")
    print(f"p-value ≈ {p:.3f}")
else:
    print("資料不足，無法進行分析。")

# 繪製散佈圖與線性回歸線
plt.figure(figsize=(7, 5))
sns.regplot(x='Age of First Kiss', y='Kiss Count', data=clean_df, ci=95, scatter_kws={'alpha': 0.6})
plt.title("Scatterplot of Age of First Kiss vs Kiss Count")
plt.xlabel("Age of First Kiss")
plt.ylabel("Number of People Kissed")
plt.tight_layout()
plt.savefig("age_of_first_kiss_vs_kiss_count.png")
plt.show()
