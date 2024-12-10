import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load the saved label encoders and scaler
with open("src/label_encoders.ppkl", "rb") as le_file:
    label_encoders = pickle.load(le_file)

with open("src/scaler.ppkl", "rb") as dc_file:
    scaler = pickle.load(dc_file)

training_cols = [
 'Age', 'Gender', 'Tenure', 'Usage Frequency', 'Support Calls', 
    'Payment Delay', 'Subscription Type', 'Contract Length', 'Total Spend', 
    'Last Interaction'
]

def fix_missing_cols(training_cols, new_data):
    missing_cols = set(training_cols) - set(new_data.columns)
    for c in missing_cols:
        new_data[c] = 0  # Add missing columns with default value 0
    new_data = new_data[training_cols]  # Ensure column order matches training
    return new_data

# Clean and preprocess the data
def clean_data_json(df):
    # Define column types
    numerical_cols = ['Age', 'Tenure', 'Usage Frequency', 'Support Calls', 
                      'Payment Delay', 'Total Spend', 'Last Interaction']
    categorical_cols = ['Gender', 'Subscription Type', 'Contract Length']
    
    # Fill missing numerical columns with 0
    for col in numerical_cols:
        if col not in df.columns:
            df[col] = 0

    # Apply StandardScaler to numerical columns
    df[numerical_cols] = scaler.transform(df[numerical_cols])

    # Handle categorical columns
    for col in categorical_cols:
        if col in df.columns:
            # Apply LabelEncoder if the column exists
            df[col] = label_encoders[col].transform(df[col])
        else:
            # Add missing categorical columns with default value
            df[col] = label_encoders[col].transform([label_encoders[col].classes_[0]])[0]

    # Ensure all training columns are present
    df = fix_missing_cols(training_cols, df)
    return df
