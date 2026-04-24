# src/04_ch4_correlation.py
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import pearsonr

# 读取数据
df = pd.read_csv("data/processed/methane_clean.csv")
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 创建2子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]
countries = df["country"].unique()

# 子图1：甲烷 vs 人口
for idx, country in enumerate(countries):
    data = df[df["country"] == country]
    corr, p = pearsonr(data["pop"], data["ch4"])
    ax1.scatter(data["pop"], data["ch4"], color=colors[idx], 
                label=f"{country} (r={corr:.3f}, p={p:.3f})", s=60, alpha=0.8)

ax1.set_title("甲烷排放与人口相关性", fontsize=15, pad=15)
ax1.set_xlabel("人口 (对应单位)", fontsize=13)
ax1.set_ylabel("甲烷排放量 (kt)", fontsize=13)
ax1.grid(True, linestyle="--", alpha=0.7)
ax1.legend(fontsize=11)

# 子图2：甲烷 vs GDP
for idx, country in enumerate(countries):
    data = df[df["country"] == country]
    corr, p = pearsonr(data["gdp"], data["ch4"])
    ax2.scatter(data["gdp"], data["ch4"], color=colors[idx], 
                label=f"{country} (r={corr:.3f}, p={p:.3f})", s=60, alpha=0.8)

ax2.set_title("甲烷排放与GDP相关性", fontsize=15, pad=15)
ax2.set_xlabel("GDP (对应单位)", fontsize=13)
ax2.set_ylabel("甲烷排放量 (kt)", fontsize=13)
ax2.grid(True, linestyle="--", alpha=0.7)
ax2.legend(fontsize=11)

plt.tight_layout()
plt.savefig("甲烷排放与人口GDP相关性.png", dpi=300, bbox_inches="tight")
plt.show()
print("✅ 图3：相关性分析图生成完成！")