def get_data_profile(df):
    return {
        "n_rows": df.shape[0],
        "n_cols": df.shape[1],
        "missing_values": int(df.isnull().sum().sum()),
        "numeric_features": len(df.select_dtypes(include=["number"]).columns)
    }