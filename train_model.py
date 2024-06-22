import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Sample data
data = {
    "CustomerID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Age": [25, 32, 45, 28, 36, 23, 50, 29, 40, 34],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
    "AnnualIncome": [50000, 60000, 80000, 45000, 75000, 30000, 100000, 52000, 90000, 65000],
    "PurchaseAmount": [200, 150, 300, 50, 250, 100, 400, 70, 350, 180],
    "PurchasedCategory": ["Electronics", "Clothing", "HomeGoods", "Books", "Electronics", "Clothing", "HomeGoods", "Books", "Electronics", "Clothing"],
    "DaysSinceLastPurchase": [10, 20, 5, 15, 2, 30, 1, 25, 8, 12],
    "RepeatPurchase": ["Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Preprocess the data
label_encoder = LabelEncoder()
df['Gender'] = label_encoder.fit_transform(df['Gender'])
df['PurchasedCategory'] = label_encoder.fit_transform(df['PurchasedCategory'])
df['RepeatPurchase'] = label_encoder.fit_transform(df['RepeatPurchase'])

# Features and target variable
X = df.drop(['CustomerID', 'RepeatPurchase'], axis=1)
y = df['RepeatPurchase']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(report)

# Save the model
joblib.dump(model, 'model.pkl')
