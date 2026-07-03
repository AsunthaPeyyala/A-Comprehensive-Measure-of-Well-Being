from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import joblib

BASE_DIR = Path(__file__).resolve().parents[1]
DATASET_PATH = BASE_DIR / "datasets" / "house_price_dataset.csv"
MODEL_PATH = BASE_DIR / "models" / "model.pkl"

# Read Dataset
data = pd.read_csv(DATASET_PATH)

# Display first rows
print(data.head())

# Check null values
print(data.isnull().sum())

# Data Visualization
sns.heatmap(data.corr(), annot=True)
plt.show()

# Independent variables
X = data[['size_sqft', 'bedrooms']]

# Dependent variable
y = data['price']

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model Training
model = LinearRegression()

model.fit(X_train, y_train)

# Prediction
prediction = model.predict(X_test)

print(prediction)

# Save Model
joblib.dump(model, MODEL_PATH)

print("Model Saved Successfully")
