from pathlib import Path
def generate_markdown_report(profile: dict, results: dict, output_path: str = "report.md"):
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    # 1. 找出 RMSE 最小（误差最低）的最优模型
    sorted_results = sorted(results.items(), key=lambda item: item[1])
    best_model, best_rmse = sorted_results[0]

    # 2. 动态拼接模型排行榜的 Markdown 表格行
    model_rows = ""
    for name, rmse in sorted_results:
        is_best = " 🏆 (Best)" if name == best_model else ""
        model_rows += f"| {name} | {rmse:.2f} | {is_best} |\n"

    # 3. 模板填充
    md_content = f"""# TabularScout Baseline Report

## Data Quality Profile
| Metric | Value |
| :--- | :--- |
| Rows (Samples) | {profile['n_rows']} |
| Features | {profile['n_cols']} |
| Missing Values | {profile['missing_values']} |
| Numeric Features | {profile['numeric_features']} |

## Baseline Model Leaderboard (5-Fold CV)
| Model | RMSE | Notes |
| :--- | :--- | :--- |
{model_rows.strip()}

> **Verdict**: **{best_model}** achieved the lowest CV RMSE of **{best_rmse:.2f}**.
"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md_content)