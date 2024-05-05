from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import requests

# Create Dash app
app = Dash(__name__)

# Define app layout
app.layout = html.Div([
    dcc.DatePickerRange(
        id='date-range',
        display_format='YYYY-MM-DD',
        start_date_placeholder_text='Start Date',
        end_date_placeholder_text='End Date',
        start_date=None,
        end_date=None
    ),
    dcc.Graph(id='bar-chart'),
])

# Callback to update the bar chart
@app.callback(
    Output('bar-chart', 'figure'),
    [Input('date-range', 'start_date'), Input('date-range', 'end_date')]
)
def update_bar_chart(start_date, end_date):
    if start_date and end_date:
        try:
            # Make a POST request to fetch data from FastAPI server with date range
            response = requests.post("http://localhost:4000/chart/bar", json={"start_date": start_date, "end_date": end_date})
            data = response.json()

            # Extract dates and counts
            results = data['results']
            dates = [result['date'] for result in results]
            counts = [result['count'] for result in results]

            # Create bar chart
            fig = go.Figure(data=go.Bar(x=dates, y=counts))

            # Update layout
            fig.update_layout(title='Bar Chart - Count per Day', xaxis_title='Date', yaxis_title='Count')

            return fig
        except Exception as e:
            print("Error fetching data from FastAPI:", e)
            return go.Figure()
    else:
        return go.Figure()

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
