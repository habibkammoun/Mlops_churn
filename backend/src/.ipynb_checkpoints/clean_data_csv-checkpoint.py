import pandas as pd
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load the saved label encoders and scaler
with open("src/label_encoders.ppkl", "rb") as le_file:
    label_encoders = pickle.load(le_file)

with open("src/scaler.ppkl", "rb") as dc_file:
    scaler = pickle.load(dc_file)

training_cols = [
    'CustomerID', 'Age', 'Gender', 'Tenure', 'Usage Frequency', 'Support Calls', 
    'Payment Delay', 'Subscription Type', 'Contract Length', 'Total Spend', 
    'Last Interaction', 'Churn'
]

def fix_missing_cols(training_cols, new_data):
    missing_cols = set(training_cols) - set(new_data.columns)
    for c in missing_cols:
        new_data[c] = 0  # Add missing columns with default value 0
    new_data = new_data[training_cols]  # Ensure column order matches training
    return new_data

# Clean and preprocess the data
def clean_data(df):
    # Ensure that all necessary columns are present
    df = df[['Gender', 'Subscription Type', 'Contract Length', 'Age', 'Tenure', 
             'Usage Frequency', 'Support Calls', 'Payment Delay', 'Total Spend', 'Last Interaction']]

    # Separate numerical and categorical columns
    numerical_cols = ['Age', 'Tenure', 'Usage Frequency', 'Support Calls', 
                      'Payment Delay', 'Total Spend', 'Last Interaction']
    categorical_cols = ['Gender', 'Subscription Type', 'Contract Length']
    
    # Check that all numerical columns are present in the DataFrame
    missing_numerical_cols = [col for col in numerical_cols if col not in df.columns]
    if missing_numerical_cols:
        raise ValueError(f"Missing numerical columns: {missing_numerical_cols}")

    # Apply StandardScaler to numerical columns (transform all columns at once)
    df[numerical_cols] = scaler.transform(df[numerical_cols])

    # Apply LabelEncoder to categorical columns
    for col in categorical_cols:
        if col in df.columns:
            if col in label_encoders:
                le = label_encoders[col]
                df[col] = le.transform(df[col])  # Apply label encoding
            else:
                raise ValueError(f"No LabelEncoder found for column: {col}")

    # Fix any missing columns in the DataFrame
    df = fix_missing_cols(training_cols, df)

    return df

# Example: Load data from CSV and preprocess
def preprocess_csv(input_file):
    # Load the CSV file
    df = pd.read_csv(input_file)

    # Process the data
    cleaned_data = clean_data(df)

    return cleaned_data
