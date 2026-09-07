import pandas as pd
def get_data_profile(df: pd.DataFrame, target_col: str):
    feature_df=df.drop(columns=target_col)
    return {
        "n_rows": df.shape[0],
        "n_cols": feature_df.shape[1],
        "missing_values": int(df.isnull().sum().sum()),
        "numeric_features": len(df.select_dtypes(include=["number"]).columns)
    }