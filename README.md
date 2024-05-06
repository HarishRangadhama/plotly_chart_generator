# Dash Plotly Charts Project

This project demonstrates how to create an interactive pie/line/bar chart using Plotly and Dash in python. The chart is generated based on data fetched from a FastAPI server.

## Installation

1. Clone the repository to your local machine: git clone <repository_url>
2. Navigate to the project directory:cd <project_directory>
3. Install the required Python packages using pip:

- pip install plotly
- pip install dash
- pip install requests

## Running the Application

1. Ensure that you have Python installed on your machine.
2. Run the following command to start the Dash application: python <pie_chart.py/line_chart.py/bar_chart.py>
3. Once the application is running, open a web browser and go to [http://127.0.0.1:8050/] to view the application.

## Usage (Pie chart)

1. The application will display an input field and a submit button.
2. Enter a number between 2 and 5 in the input field.
3. Click the submit button to fetch data from the FastAPI endpoint and display the pie chart.
4. If the input is invalid or there is an error fetching data, error messages will be displayed.

## Usage (Line chart)

1. The application will display a line chart that will dynamically fetch data from a FastAPI server.
2. The X and Y coordinates for the line chart will be obtained from the FastAPI response.
3. The line chart will update automatically whenever new data is available from the FastAPI.

## Usage (Bar chart)

1. The application will display a date range picker allowing the selection of start and end dates.
2. Select a start date and an end date to specify the date range for fetching data.
3. Upon selecting the date range, the application will make a POST request to the FastAPI server with the selected date range.
   The FastAPI server will respond with data containing dates and counts.
4. The application will create a bar chart using the dates as x-values and the counts as y-values.
5. The bar chart will dynamically update based on the selected date range, displaying the count per day.
