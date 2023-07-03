import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# Load the collected environmental data from the CSV file
df = pd.read_csv("environmental_data.csv")

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div(
    children=[
        html.H1("Environmental Data Dashboard"),
        dcc.Graph(
            figure=px.line(df, x="date", y="air_quality", title="Air Quality over Time")
        ),
        dcc.Graph(
            figure=px.line(df, x="date", y="water_pollution", title="Water Pollution over Time")
        ),
        dcc.Graph(
            figure=px.line(df, x="date", y="deforestation_rates", title="Deforestation Rates over Time")
        ),
        dcc.Graph(
            figure=px.line(df, x="date", y="climate_patterns", title="Climate Patterns over Time")
        ),
    ]
)

# Run the Dash app
if __name__ == "__main__":
    app.run_server(debug=True)
