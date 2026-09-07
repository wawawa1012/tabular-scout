import argparse
import pandas as pd
from tabular_scout.data import load_and_split
from tabular_scout.models import train_and_evaluate
from tabular_scout.profile import get_data_profile
from tabular_scout.report import generate_markdown_report

def main():
    parser = argparse.ArgumentParser(description="TabularScout - Tabular Baseline Engine")
    parser.add_argument("--data", type=str, required=True, help="Path to the CSV dataset")
    parser.add_argument("--target", type=str, required=True, help="Name of the target column")
    parser.add_argument("--output", type=str, default="report.md", help="Output report path")
    args = parser.parse_args()

    # 1. 统一加载数据
    df = pd.read_csv(args.data)
    profile = get_data_profile(df, args.target)

    # 2. 切分特征与训练评估
    X, y = load_and_split(args.data, args.target)
    results = train_and_evaluate(X, y)

    # 3. 产出报告
    generate_markdown_report(profile, results, args.output)

    # 4. 终端状态摘要
    print("\n--- TabularScout Finished ---")
    print(f"Dataset: {args.data} ({profile['n_rows']} rows, {profile['n_cols']} features)")
    print(f"Report saved to: {args.output}\n")

if __name__ == "__main__":
    main()