from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
def train_and_evaluate(X, y):
    models = {
        "Linear Regression": LinearRegression(),
        "Dummy Baseline": DummyRegressor(strategy="mean"),
        "Ridge": Ridge(),
        "Random Forest": RandomForestRegressor(n_estimators=50, random_state=42)
    }
    
    results = {}
    for name, model in models.items():
        score = cross_val_score(model, X, y, cv=5, scoring="neg_root_mean_squared_error")
        results[name] = round(-score.mean(), 2)  # round 保留两位小数
        
    return results