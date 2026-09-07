from tabular_scout.data import load_and_split
from tabular_scout.models import train_and_evaluate
from pathlib import Path
from tabular_scout.profile import get_data_profile
import pandas as pd

basePath=Path(__file__).parent
filePath=basePath/"tabular_scout"/"test_data.csv"
X,y=load_and_split(filePath,"target")
rmse=train_and_evaluate(X, y)
print(get_data_profile(pd.read_csv(filePath)))
print(f"root mean squared error is {rmse}")