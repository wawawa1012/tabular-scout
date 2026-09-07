import pandas as pd

def load_and_split(filepath: str, target_col: str):
    df=pd.read_csv(filepath)
    y=df[target_col]
    X=df.drop(columns=target_col) 
    return X,y
