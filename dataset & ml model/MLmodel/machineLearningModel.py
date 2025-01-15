#  (Trainnig a machine learning model on the dataset )
# getting help from chatgpt
# https://chatgpt.com/c/677e47f2-3784-8006-8a10-2bacf29c628c
#1) Installed these librarires ( pip install pandas numpy scikit-learn matplotlib )

import pandas as pd

#2) Loading the dataset
file_path = "C:\\Users\\Computer Arena\\Desktop\\automaticPlantWateringSystem\\dataset & ml model\\Dataset\\TARP.csv"
data = pd.read_csv(file_path)

# Display the first few rows to understand the dataset
print(data.head())

# 3) Understanding the Data
# Check for missing values
print(data.isnull().sum())

# Get basic statistics
print(data.describe())

# Check column names
print(data.columns)

# 4) Preprocess the Data
# Fill missing values (if any) with the mean of each column
data.fillna(data.mean(), inplace=True)

# Encode the target column ('Status') if it's categorical
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
data['Status'] = encoder.fit_transform(data['Status'])

# 5) Split the Data
from sklearn.model_selection import train_test_split

# Features (X) and target (y)
X = data.drop(columns=['Status'])  # Replace 'Status' with your target column name
y = data['Status']

# Split into train and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6) Choosing  a Machine Learning Model
from sklearn.tree import DecisionTreeClassifier

# Initialize the model
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# 7) Evaluate the Model

from sklearn.metrics import accuracy_score, classification_report

# Predict on test data
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# 8)Save the model
import joblib
joblib.dump(model, 'plant_watering_model.pkl')

# 9)Use the Model

# Load the saved model
model = joblib.load('plant_watering_model.pkl')

# Predict
new_data = [[45, 25, 30, 12, 22, 15, 80, 25, 101.5, 6.5, 0.2, 10, 20, 15]]  # Example input
prediction = model.predict(new_data)
print("Prediction:", encoder.inverse_transform(prediction))







