## `README_zh.md`

```markdown
# TabularScout 🔭

[English](README.md) | [简体中文](README_zh.md)

一个轻量、可解释的表格回归数据基线评估工具。

TabularScout 接收一个 CSV 数据集以及目标列名称，自动完成基础数据体检、多个代表性回归模型的 5 折交叉验证，并生成排版清晰的 Markdown 分析报告。

## 功能

- **数据体检**  
  自动统计样本数量、特征数量、数值特征数量以及缺失值。

- **多模型基线评估**  
  当前包含四个具有不同意义的回归基线：
  - Dummy Regressor
  - Linear Regression
  - Ridge Regression
  - Random Forest Regressor

- **更稳定的模型评估**  
  使用 5 折交叉验证，并以 RMSE 作为评价指标。

- **自动生成报告**  
  自动对模型结果进行排序，并输出 Markdown 报告。

- **命令行工具**  
  可以直接通过终端完成完整的数据分析流程。

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
2. 运行 TabularScout
python -m tabular_scout.cli \
  --data examples/diabetes.csv \
  --target target \
  --output outputs/report.md

示例输出：

--- TabularScout Finished ---

Dataset: examples/diabetes.csv
Samples: 442
Features: 10

Best baseline: Linear Regression
Report saved to: outputs/report.md
示例结果

在 scikit-learn Diabetes 数据集上的 5 折交叉验证结果：

模型	5-Fold CV RMSE	说明
Linear Regression	54.69	🏆 最佳基线
Random Forest	58.11	非线性集成模型
Ridge	58.45	L2 正则化线性模型
Dummy Baseline	77.26	始终预测均值

RMSE 越小表示预测误差越小。

在这个数据集上，最简单的 Linear Regression 反而取得了最低的平均 RMSE。

这个结果说明：

更复杂的模型并不一定具有更好的泛化能力。

为什么选择这四个模型？

TabularScout 并不追求堆叠大量算法，而是希望用少量具有代表性的模型快速建立基线。

每个模型实际上都在回答一个不同的问题。

Dummy Regressor

Dummy Regressor 不使用任何输入特征，只预测训练数据目标值的平均值。

它提供了一条最基础的参考线：

真正的模型是否至少比“无脑猜平均值”更好？

如果一个模型连 Dummy Baseline 都无法明显超过，那么当前特征可能没有提供足够的有效预测信息。

Linear Regression

Linear Regression 是最基础的线性模型。

它用于测试：

特征与目标之间是否已经存在较明显的线性关系？

它也是整个项目中的核心线性基线。

Ridge Regression

Ridge 在线性回归的基础上加入 L2 正则化。

除了降低预测误差之外，它还会惩罚过大的模型参数，使模型倾向于使用更加平稳的权重。

它主要用于观察：

对线性模型施加正则化以后，模型的泛化表现是否会更加稳定？

Random Forest

Random Forest 由多棵不同的决策树组成，并将它们的预测结果进行平均。

与线性模型不同，它能够捕捉：

非线性关系
阈值关系
特征之间的交互

因此它在 TabularScout 中承担的是一个非线性 baseline 的角色。

TabularScout 的目标并不是成为一个完整的 AutoML 系统，而是在几秒钟内快速得到一组简单、可解释的初始结果。

评估方法

TabularScout 使用 5 折交叉验证（5-Fold Cross Validation）。

数据被划分成五份，每次使用其中一份作为验证数据，其余四份用于训练。

第 1 轮：验证 | 训练 | 训练 | 训练 | 训练
第 2 轮：训练 | 验证 | 训练 | 训练 | 训练
第 3 轮：训练 | 训练 | 验证 | 训练 | 训练
第 4 轮：训练 | 训练 | 训练 | 验证 | 训练
第 5 轮：训练 | 训练 | 训练 | 训练 | 验证

最终计算五次验证 RMSE 的平均值。

相比只进行一次 train_test_split，交叉验证能够减少单次随机划分带来的偶然性，从而对模型的泛化能力做出更加稳定的估计。

项目结构
tabular-scout/
├── tabular_scout/
│   ├── __init__.py
│   ├── data.py        # 数据加载以及特征/目标拆分
│   ├── models.py      # 模型定义和 5 折交叉验证
│   ├── profile.py     # 数据集体检
│   ├── report.py      # Markdown 报告生成
│   └── cli.py         # 命令行入口
│
├── examples/
│   └── diabetes.csv
│
├── outputs/
│   └── report.md
│
├── requirements.txt
├── README.md
├── README_zh.md
└── .gitignore
工作流程
CSV 数据集
     │
     ▼
数据体检
     │
     ▼
拆分 X / y
     │
     ▼
5 折交叉验证
     │
     ├── Dummy Regressor
     ├── Linear Regression
     ├── Ridge Regression
     └── Random Forest
     │
     ▼
按照 RMSE 排名
     │
     ▼
生成 Markdown 报告
当前限制

目前版本主动保持较小的功能范围：

仅支持回归任务
目标列必须为数值类型
输入特征必须为数值类型
暂不自动处理缺失值
暂不自动编码分类特征
模型集合固定
暂不自动进行超参数搜索

这些限制是 v0.1 的主动设计选择，而不是试图做一个功能庞大的 AutoML 系统。

我学到了什么

通过完成 TabularScout，我主要理解了：

为什么正式建模前需要 Dummy Baseline；
Linear Regression 与 Ridge Regression 的区别；
L2 正则化为什么能够限制过大的模型参数；
Random Forest 为什么能够处理非线性关系和特征交互；
为什么复杂模型并不一定优于简单模型；
为什么单次 train/test 划分可能具有偶然性；
为什么 5 折交叉验证能够得到更加稳定的评估结果；
scikit-learn 统一的 .fit() / .predict() 接口为什么方便构建统一评估流程；
如何把一个机器学习实验逐渐封装成一个可以复用的命令行工具。
技术栈
Python
pandas
scikit-learn
argparse
Markdown
后续可能的方向

未来如果继续扩展，可以考虑：

自动处理缺失值
分类特征编码
支持分类任务
可配置交叉验证参数
增加更多评价指标

不过当前 v0.1 的目标仍然是：

保持简单、快速、可解释。

License

本项目主要用于机器学习学习与实验。