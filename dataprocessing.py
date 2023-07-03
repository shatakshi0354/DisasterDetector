import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the collected data from the CSV file
df = pd.read_csv("environmental_data.csv")

# Drop any rows with missing values
df = df.dropna()

# Separate the features and labels
features = df[['temperature', 'humidity', 'wind_speed']]
labels = df['disaster_label']

# Standardize the features using StandardScaler
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Create a new DataFrame with the scaled features and labels
df_scaled = pd.DataFrame(features_scaled, columns=features.columns)
df_scaled['disaster_label'] = labels

# Save the preprocessed data to a new CSV file
df_scaled.to_csv("preprocessed_data.csv", index=False)
