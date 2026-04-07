# ==============================================
# 甲烷排放、GDP、人口 相关性热力图
# 自动保存到 output/results/
# ==============================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------
# 1. 读取处理好的数据
# ----------------------
df = pd.read_csv("data/processed/methane_clean.csv")

# ----------------------
# 2. 提取需要计算相关性的列
# ----------------------
# 只保留数值型变量：甲烷排放、GDP、人口
corr_data = df[["ch4", "gdp", "pop"]]

# ----------------------
# 3. 计算相关系数矩阵
# ----------------------
corr_matrix = corr_data.corr()

# ----------------------
# 4. 绘图设置（中文正常显示）
# ----------------------
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

plt.figure(figsize=(8, 6))

# ----------------------
# 5. 绘制热力图
# ----------------------
heatmap = sns.heatmap(
    corr_matrix,
    annot=True,        # 显示相关系数数字
    cmap="coolwarm",   # 红蓝色系（专业好看）
    vmin=-1, vmax=1,   # 相关系数范围
    linewidths=0.5,    # 格子边框
    fmt=".2f"          # 保留2位小数
)

# ----------------------
# 6. 设置标题和标签
# ----------------------
plt.title("甲烷排放、GDP、人口 相关性热力图", fontsize=14, pad=20)
plt.tight_layout()

# ----------------------
# 7. 保存图片
# ----------------------
plt.savefig(
    "output/results/相关性热力图.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

print("✅ 相关性热力图生成成功！")
print("📁 保存路径：output/results/相关性热力图.png")