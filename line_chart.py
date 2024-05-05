from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import requests

# Create Dash app
app = Dash(__name__)

# Define app layout
app.layout = html.Div([
    dcc.Graph(id='line-chart'),
])

# Callback to update the line chart
@app.callback(
    Output('line-chart', 'figure'),  # Output component: Line chart figure
    [Input('line-chart', 'id')]      # Input component: Triggering the callback
)
def update_line_chart(_):
    try:
        # Make a GET request to fetch data from FastAPI server
        response = requests.get("http://localhost:4000/chart/line")
        data = response.json()

        # Extract X and Y coordinates
        coordinates = data['coordinates']
        x_values = [point['x'] for point in coordinates]
        y_values = [point['y'] for point in coordinates]

        # Create line chart
        fig = go.Figure(data=go.Scatter(x=x_values, y=y_values, mode='lines+markers'))

        # Update layout
        fig.update_layout(title='Line Chart', xaxis_title='X', yaxis_title='Y')

        return fig  # Return updated line chart figure
    except Exception as e:
        print("Error fetching data from FastAPI:", e)
        return go.Figure()  # Return empty figure in case of error

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
