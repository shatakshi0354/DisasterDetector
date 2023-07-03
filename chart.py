from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# Load the collected environmental data from the CSV file
df = pd.read_csv("environmental_data.csv")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/air_quality')
def get_air_quality():
    air_quality_data = df[['date', 'air_quality']]
    return jsonify(air_quality_data.to_dict(orient='records'))

@app.route('/api/water_pollution')
def get_water_pollution():
    water_pollution_data = df[['date', 'water_pollution']]
    return jsonify(water_pollution_data.to_dict(orient='records'))

@app.route('/api/deforestation_rates')
def get_deforestation_rates():
    deforestation_rates_data = df[['date', 'deforestation_rates']]
    return jsonify(deforestation_rates_data.to_dict(orient='records'))

@app.route('/api/climate_patterns')
def get_climate_patterns():
    climate_patterns_data = df[['date', 'climate_patterns']]
    return jsonify(climate_patterns_data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
