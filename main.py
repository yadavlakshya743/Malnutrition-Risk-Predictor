import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Simulated sample data (age, weight, MUAC, growth history)
data = {
    'age': [2, 4, 3, 6, 1, 5],
    'weight': [11, 15, 12, 14, 9, 13],
    'muac': [12, 13, 11, 14, 10, 12],
    'growth_history': [1, 2, 1, 2, 1, 1],
    'malnutrition_risk': [1, 0, 2, 0, 2, 1]  # 0: Normal, 1: MAM, 2: SAM
}

df = pd.DataFrame(data)

X = df.drop("malnutrition_risk", axis=1)
y = df["malnutrition_risk"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "malnutrition_model.pkl")
print("✅ Model trained and saved!")
