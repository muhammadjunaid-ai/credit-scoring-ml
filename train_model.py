# train_model.py
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv("data/credit_data.csv")

# Map target column (replace with your column name if different)
data["target"] = data["target"].map({"good": 1, "bad": 0})

# Select features that exist in dataset
selected_features = [
    "status_account",
    "month_duration",
    "credit_history",
    "purpose",
    "credit_amount",
    "status_savings"
]

X = data[selected_features].copy()
y = data["target"]

# Encode categorical features and save mappings
categorical_cols = ["status_account", "credit_history", "purpose", "status_savings"]
mappings = {}

for col in categorical_cols:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    # Save mapping: original value -> integer
    mappings[col] = dict(zip(le.classes_, le.transform(le.classes_)))

# Save mappings
joblib.dump(mappings, "model/mappings.pkl")

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Random Forest
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Evaluate
pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))
print(classification_report(y_test, pred))

# Save model
joblib.dump(model, "model/credit_model.pkl")
print("✅ Model and mappings saved successfully!")