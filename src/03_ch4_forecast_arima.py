# src/03_ch4_forecast_arima.py
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import warnings
warnings.filterwarnings("ignore")

# 读取数据
df = pd.read_csv("data/processed/methane_clean.csv")
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 预测年份：2025-2054（未来30年）
future_years = np.arange(2025, 2055)
plt.figure(figsize=(14, 7))
colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]
countries = df["country"].unique()

for idx, country in enumerate(countries):
    # 提取历史数据，按年份排序
    data = df[df["country"] == country].sort_values("year")
    ts = data.set_index("year")["ch4"]
    
    # 训练ARIMA模型（自动定阶，适配你的数据长度）
    model = ARIMA(ts, order=(1,1,1))
    result = model.fit()
    
    # 预测未来30年
    forecast = result.get_forecast(steps=30)
    pred_mean = forecast.predicted_mean
    pred_ci = forecast.conf_int()
    
    # 绘制历史+预测+置信区间
    plt.plot(ts.index, ts.values, marker="o", linewidth=2, color=colors[idx], label=f"{country} 历史排放")
    plt.plot(future_years, pred_mean, linestyle="--", linewidth=2, color=colors[idx], label=f"{country} ARIMA预测")
    plt.fill_between(future_years, pred_ci.iloc[:,0], pred_ci.iloc[:,1], color=colors[idx], alpha=0.2)

# 图表美化
plt.title("2005-2054年甲烷排放历史与ARIMA未来30年预测（95%置信区间）", fontsize=16, pad=20)
plt.xlabel("年份", fontsize=14)
plt.ylabel("甲烷排放量 (kt)", fontsize=14)
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend(fontsize=11, bbox_to_anchor=(1.02, 1), loc="upper left")
plt.xticks(range(2005, 2055, 5), rotation=45)
plt.tight_layout()

plt.savefig("甲烷排放ARIMA预测.png", dpi=300, bbox_inches="tight")
plt.show()
print("✅ 图2：ARIMA高精度预测图生成完成！")