import pandas as pd
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load the saved label encoders and scaler
with open("src/label_encodersFinal.pkl", "rb") as le_file:
    label_encoders = pickle.load(le_file)

with open("src/scalerFinal.pkl", "rb") as dc_file:
    scaler = pickle.load(dc_file)

training_cols = [
    'CustomerID', 'Age', 'Gender', 'Tenure', 'Usage Frequency', 'Support Calls', 
    'Payment Delay', 'Subscription Type', 'Contract Length', 'Total Spend', 
    'Last Interaction', 'Churn'
]


# Clean and preprocess the data
def clean_data(df):
  # Column renaming to match expected training columns
    df = df.rename(columns={
        "Contract_Length": "Contract Length",
        "Last_Interaction": "Last Interaction",
        "Subscription_Type": "Subscription Type",
        "Usage_Frequency": "Usage Frequency",
        "Payment_Delay": "Payment Delay",
        "Support_Calls": "Support Calls",
        "Total_Spend": "Total Spend"    })

    # Define column types
    numerical_cols = [
        'Age', 'Tenure', 'Usage Frequency', 'Support Calls', 
        'Payment Delay', 'Total Spend', 'Last Interaction'
    ]
    categorical_cols = ["Gender", 'Subscription Type', "Contract Length"]


    # Apply StandardScaler to numerical columns
    df[numerical_cols] = scaler.transform(df[numerical_cols])

    

    # Encode categorical columns
    for col in categorical_cols:
        if col in df.columns:
            if col in label_encoders:
                le = label_encoders[col]
                df[col] = le.transform(df[col])
            else:
                raise ValueError(f"No LabelEncoder found for column: {col}")
        else:
            raise ValueError(f"Missing categorical column: {col}")

    return df
