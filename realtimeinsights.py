import pandas as pd
import plotly.express as px

# Load the collected environmental data from the CSV file
df = pd.read_csv("environmental_data.csv")

# Visualize air quality data
fig_air_quality = px.line(df, x="date", y="air_quality", title="Air Quality over Time")
fig_air_quality.show()

# Visualize water pollution data
fig_water_pollution = px.line(df, x="date", y="water_pollution", title="Water Pollution over Time")
fig_water_pollution.show()

# Visualize deforestation rates data
fig_deforestation_rates = px.line(df, x="date", y="deforestation_rates", title="Deforestation Rates over Time")
fig_deforestation_rates.show()

# Visualize climate patterns data
fig_climate_patterns = px.line(df, x="date", y="climate_patterns", title="Climate Patterns over Time")
fig_climate_patterns.show()
