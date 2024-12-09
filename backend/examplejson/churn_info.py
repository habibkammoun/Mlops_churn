from pydantic import BaseModel, Field
from typing import Union

class ChurnPredictionModel(BaseModel):
    Age: int = Field(..., example=22)
    Gender: str = Field(..., example="Female")
    Tenure: int = Field(..., example=25)
    Usage_Frequency: int = Field(..., alias="Usage Frequency", example=14)  # Alias for space
    Support_Calls: int = Field(..., alias="Support Calls", example=4)  # Alias for space
    Payment_Delay: int = Field(..., alias="Payment Delay", example=27)  # Alias for space
    Subscription_Type: str = Field(..., alias="Subscription Type", example="Basic")  # Alias for space
    Contract_Length: str = Field(..., alias="Contract Length", example="Monthly")
    Total_Spend: float = Field(..., alias="Total Spend", example=598.0)
    Last_Interaction: int = Field(..., alias="Last Interaction", example=9)

    class Config:
        allow_population_by_field_name = True  # Enables usage of both aliases and field names
        schema_extra = {
            "example": {
                "Age": 22,
                "Gender": "Female",
                "Tenure": 25,
                "Usage Frequency": 14,
                "Support Calls": 4,
                "Payment Delay": 27,
                "Subscription Type": "Basic",
                "Contract Length": "Monthly",
                "Total Spend": 598.0,
                "Last Interaction": 9,
            }
        }
