import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ----------------------
# 1. 读取你已经处理好的干净数据
# ----------------------
df = pd.read_csv("data/processed/methane_clean.csv")

# ----------------------
# 2. 计算人均甲烷排放 (吨/人)
# ----------------------
# ch4 单位通常是 kt (千吨) → 转成 吨
# pop 单位是人
df["per_capita"] = (df["ch4"] * 1000) / df["pop"]

# ----------------------
# 3. 绘图设置（中文正常显示）
# ----------------------
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

plt.figure(figsize=(12, 6))

# ----------------------
# 4. 分别绘制三个国家
# ----------------------
countries = ["China", "Australia", "Aruba"]
colors = ["#E53E3E", "#3182CE", "#38A169"]
markers = ["o", "s", "^"]

for country, color, marker in zip(countries, colors, markers):
    data = df[df["country"] == country]
    plt.plot(
        data["year"],
        data["per_capita"],
        label=country,
        color=color,
        marker=marker,
        linewidth=2.5,
        markersize=6
    )

# ----------------------
# 5. 图表标题与标签
# ----------------------
plt.title("2005–2024 三国人均甲烷排放量对比", fontsize=16, pad=20)
plt.xlabel("年份", fontsize=13)
plt.ylabel("人均甲烷排放量 (吨/人)", fontsize=13)
plt.legend(fontsize=12)
plt.grid(alpha=0.3, linestyle="--")
plt.xticks(np.arange(2005, 2025, 2), rotation=45)
plt.tight_layout()

# ----------------------
# 6. 自动保存到输出目录
# ----------------------
plt.savefig(
    "output/results/三国人均甲烷排放对比图.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

print("✅ 人均甲烷排放图已生成！")
print("📁 保存路径：output/results/三国人均甲烷排放对比图.png")