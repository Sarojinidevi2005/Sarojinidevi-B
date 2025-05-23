# -*- coding: utf-8 -*-
"""nm final

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SXZa6G8p4R2F-kYKfXOMqFCBfKWmPs9C
"""

import pandas as pd

# Load the dataset
df = pd.read_csv("/content/accidents_india.csv")

# Show basic info
print(df.shape)
df.head()

df.isnull().sum().sort_values(ascending=False)

# Check missing values in percentage
missing_percent = df.isnull().mean().sort_values(ascending=False) * 100
missing_percent[missing_percent > 0]

import pandas as pd

# Load the dataset
df = pd.read_csv("/content/accidents_india.csv")  # Make sure the path is correct

# Now you can use df
df.isnull().sum()

df.dropna(subset=['Day_of_Week', 'Speed_limit', 'Sex_Of_Driver', 'Accident_Severity'], inplace=True)

df['Number_of_Pasengers'].fillna(1, inplace=True)  # or use median

df = df[['Day_of_Week', 'Light_Conditions', 'Sex_Of_Driver',
         'Vehicle_Type', 'Speed_limit', 'Pedestrian_Crossing',
         'Road_Type', 'Special_Conditions_at_Site',
         'Number_of_Pasengers', 'Accident_Severity']]

print(df.columns.tolist())

from sklearn.preprocessing import LabelEncoder

df_clean = df.copy()  # to avoid changing original

# List of categorical columns to encode
cat_cols = ['Day_of_Week', 'Light_Conditions', 'Sex_Of_Driver',
            'Vehicle_Type', 'Pedestrian_Crossing',
            'Road_Type', 'Special_Conditions_at_Site']

# Apply label encoding
le = LabelEncoder()
for col in cat_cols:
    df_clean[col] = le.fit_transform(df_clean[col].astype(str))

# Fill missing numerical values (if any)
df_clean['Number_of_Pasengers'].fillna(df_clean['Number_of_Pasengers'].median(), inplace=True)
df_clean['Speed_limit'].fillna(df_clean['Speed_limit'].median(), inplace=True)

X = df_clean.drop(columns=['Accident_Severity'])
y = df_clean['Accident_Severity']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

import seaborn as sns
import matplotlib.pyplot as plt

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

# Predict on first 5 rows from test data
predictions = model.predict(X_test[:5])
print("Predicted Severity:", predictions)
print("Actual Severity:   ", y_test[:5].values)

required_columns = [
    'Day_of_Week',
    'Light_Conditions',
    'Sex_Of_Driver',
    'Vehicle_Type',
    'Pedestrian_Crossing',
    'Road_Type',
    'Special_Conditions_at_Site',
    'Speed_limit',
    'Number_of_Pasengers'
]

import pandas as pd

# Input with all integer-encoded values
sample_data = {
    'Day_of_Week': [0],                # e.g., Monday
    'Light_Conditions': [1],           # e.g., Darkness
    'Sex_Of_Driver': [0],              # e.g., Male
    'Vehicle_Type': [2],               # e.g., Car
    'Pedestrian_Crossing': [0],        # e.g., None within 50 metres
    'Road_Type': [2],                  # e.g., Single carriageway
    'Special_Conditions_at_Site': [0], # e.g., None
    'Speed_limit': [30],               # numeric
    'Number_of_Pasengers': [1]         # numeric
}

sample_df = pd.DataFrame(sample_data)

sample_df = sample_df[X.columns.tolist()]

sample = {}
sample['Sex_Of_Driver'] = input("Sex of Driver (e.g., Male/Female): ").strip()
sample['Day_of_Week'] = input("Day of Week (e.g., Monday): ").strip()
sample['Light_Conditions'] = input("Light Conditions (e.g., Daylight): ").strip()
sample['Vehicle_Type'] = input("Vehicle Type (e.g., Car): ").strip()
sample['Pedestrian_Crossing'] = input("Pedestrian Crossing (e.g., None within 50 metres): ").strip()
sample['Road_Type'] = input("Road Type (e.g., Single carriageway): ").strip()
sample['Special_Conditions_at_Site'] = input("Special Conditions at Site (e.g., None): ").strip()
sample['Speed_limit'] = int(input("Speed Limit (e.g., 30): "))
sample['Number_of_Pasengers'] = int(input("Number of Passengers (e.g., 1): "))

sample_df = pd.DataFrame([sample])

# Encode using saved encoders
for col in cat_cols:
    try:
        sample_df[col] = encoders[col].transform(sample_df[col].astype(str))
    except ValueError:
        print(f"⚠️ Unseen value in '{col}' — using most common category.")
        most_common = encoders[col].classes_[0]
        sample_df[col] = encoders[col].transform([most_common])

# IMPORTANT: Set column order to match training data
sample_df = sample_df[X.columns.tolist()]

# Predict
prediction = model.predict(sample_df)
print("\n🚦 Predicted Accident Severity:", prediction[0])