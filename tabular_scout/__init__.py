# 生成测试数据脚本 make_data.py
from sklearn.datasets import load_diabetes
import pandas as pd

data = load_diabetes(as_frame=True)
df = data.frame
df.to_csv("test_data.csv", index=False)
print("已生成测试集 test_data.csv，目标列名为 target")