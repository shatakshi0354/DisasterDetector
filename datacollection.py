import requests
import json
import pandas as pd

# API endpoint for data collection
api_url = "https://api.example.com/environmental_data"

# Parameters for the API request
params = {
    "start_date": "2023-01-01",
    "end_date": "2023-12-31",
    "location": "latitude,longitude",
    "data_types": ["temperature", "humidity", "wind_speed"],
}

# Make API request to collect data
response = requests.get(api_url, params=params)
data = response.json()

# Convert data to pandas DataFrame
df = pd.DataFrame(data)

# Save data to CSV file
df.to_csv("environmental_data.csv", index=False)
