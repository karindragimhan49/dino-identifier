# src/train.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

print("Training process started...")

# Load Data
df = pd.read_csv('data/dinosaur.csv')

# Clean Data
df.columns = df.columns.str.strip()
df.dropna(subset=['diet'], inplace=True)
df = df[df['diet'].isin(['carnivorous', 'herbivorous'])]

numerical_features = ['length_m', 'max_ma', 'min_ma']
for col in numerical_features:
    df[col].fillna(df[col].median(), inplace=True)

# Feature Engineering
df['diet_numeric'] = df['diet'].apply(lambda x: 1 if x == 'carnivorous' else 0)

# Define X and y
X = df[numerical_features]
y = df['diet_numeric']

# Train Model
# Note: We are training on the full dataset now for the final model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)
print("Model training complete.")

# Save Model
os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/dino_identifier_model.joblib')
print("Model saved to models/dino_identifier_model.joblib")