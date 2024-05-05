from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import requests

# Create Dash app
app = Dash(__name__)

# Define app layout
app.layout = html.Div([
    dcc.Input(id='input-number', type='number', min=2, max=5, step=1, value=2),  # Input field for number
    html.Button('Submit', id='submit-button', n_clicks=0),  # Submit button
    dcc.Graph(id='pie-chart'),  # Pie chart display
    html.Div(id='message-output')  # Div for displaying messages
])

# Callback to update the pie chart and display message
@app.callback(
    [Output('pie-chart', 'figure'), Output('message-output', 'children')],
    [Input('submit-button', 'n_clicks')],
    [Input('input-number', 'value')]
)
def update_pie_chart(n_clicks, input_number):
    if n_clicks > 0:
        try:
            if input_number is not None and 2 <= input_number <= 5:
                # Make a POST request to fetch data from FastAPI server
                response = requests.post("http://localhost:4000/chart/pie", json={"number": input_number})
                data = response.json()

                # Ensure the API response contains the expected data structure
                if 'results' not in data:
                    raise ValueError("Invalid API response format")

                # Extract subject names and marks
                results = data['results']
                subjects = [result['subject'] for result in results]
                marks = [result['marks'] for result in results]

                # Normalize marks to ensure sum equals 100
                total_marks = sum(abs(grade) for grade in marks)
                proportions = [abs(grade) / total_marks * 100 for grade in marks]

                # Create pie chart
                fig = go.Figure(data=[go.Pie(labels=subjects, values=proportions, hole=0.3)])

                # Add custom hover information
                hover_text = [f"{subject}: {mark}" for subject, mark in zip(subjects, marks)]
                fig.update_traces(hoverinfo='label+percent+text', text=hover_text)

                fig.update_layout(title='Pie chart - Marks Distribution')
                return fig, ''  # Return pie chart and empty message
            else:
                # Return empty pie chart and error message if input number is invalid
                return go.Figure(data=[go.Pie(labels=[], values=[], hole=0.3)]), html.Div("Please enter a number between 2 and 5", style={'color': 'red'})
        except Exception as e:
            # Return empty pie chart and error message if there's an error fetching data
            print("Error fetching data from FastAPI:", e)
            return go.Figure(data=[go.Pie(labels=[], values=[], hole=0.3)]), html.Div("Error fetching data from FastAPI", style={'color': 'red'})
    else:
        return go.Figure(data=[go.Pie(labels=[], values=[], hole=0.3)]), ''  # Empty pie chart and empty message

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
