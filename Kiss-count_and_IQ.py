# -*- coding: utf-8 -*-
"""
Created on Tue May 20 04:00:12 2025

@author: USER
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# 讀取資料
file_path = r"C:\Users\USER\Desktop\英文作業\DATA_Kiss_count_gender_and_IQ.xlsx"
df = pd.read_excel(file_path)

# 將欄位標準化（若欄位名稱有空格等問題）
df.columns = df.columns.str.strip()

# 將 IQ 與 Kiss Count 轉為數值型態，並清理非數字或缺失值
df['IQ'] = pd.to_numeric(df['IQ'], errors='coerce')
df['Kiss Count'] = pd.to_numeric(df['Kiss Count'], errors='coerce')

# 保留完整資料的部分
clean_df = df[['IQ', 'Kiss Count']].dropna()

# 檢查資料筆數是否足夠
if len(clean_df) >= 2:
    # 計算皮爾森相關係數
    r, p = pearsonr(clean_df['IQ'], clean_df['Kiss Count'])
    print(f"Pearson correlation r ≈ {r:.3f}")
    print(f"p-value ≈ {p:.3f}")
else:
    print("資料不足，無法進行相關分析。")

# 繪製散佈圖與回歸線
plt.figure(figsize=(7, 5))
sns.regplot(x='IQ', y='Kiss Count', data=clean_df, ci=95, scatter_kws={'alpha': 0.6})
plt.title("Scatterplot of IQ vs Kiss Count")
plt.xlabel("IQ")
plt.ylabel("Number of People Kissed")
plt.tight_layout()
plt.savefig("iq_vs_kiss_count_scatterplot.png")
plt.show()
