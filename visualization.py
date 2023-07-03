import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the collected environmental data from the CSV file
df = pd.read_csv("environmental_data.csv")

# Visualize air quality data
sns.lineplot(x="date", y="air_quality", data=df)
plt.title("Air Quality over Time")
plt.xlabel("Date")
plt.ylabel("Air Quality")
plt.show()

# Visualize water pollution data
sns.lineplot(x="date", y="water_pollution", data=df)
plt.title("Water Pollution over Time")
plt.xlabel("Date")
plt.ylabel("Water Pollution")
plt.show()

# Visualize deforestation rates data
sns.lineplot(x="date", y="deforestation_rates", data=df)
plt.title("Deforestation Rates over Time")
plt.xlabel("Date")
plt.ylabel("Deforestation Rates")
plt.show()

# Visualize climate patterns data
sns.lineplot(x="date", y="climate_pattern", data=df)
plt.title("Climate Patterns over Time")
plt.xlabel("Date")
plt.ylabel("Climate Patterns")
plt.show()
