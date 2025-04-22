import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import base64
import io

# Create a Dash web application
app = dash.Dash(__name__)

# Define layout of the dashboard
app.layout = html.Div(children=[
    html.H1(children='Dashboard'),

    dcc.Upload(
        id='upload-data',
        children=[
            html.Button('Select a File', style={'marginBottom': '10px'}),
            html.P('Drag and Drop or ', style={'marginBottom': '0px'}),
        ],
        multiple=True  # Allow multiple file uploads
    ),

    dcc.Dropdown(
        id='chart-type-dropdown',
        options=[
            {'label': 'Bar Chart', 'value': 'bar'},
            {'label': 'Pie Chart', 'value': 'pie'},
            {'label': 'Line Chart', 'value': 'line'},
            {'label': 'Histogram', 'value': 'histogram'},
            {'label': 'Area Chart', 'value': 'area'},
            {'label': 'Scatter Plot', 'value': 'scatter'},
            # Add more chart types as needed
        ],
        value='bar',  # Default chart type
        style={'width': '50%'}
    ),

    dcc.Graph(
        id='example-graph',
    )
])

# Callback to update the graph based on the uploaded file and selected chart type
@app.callback(
    Output('example-graph', 'figure'),
    [Input('upload-data', 'contents'),
     Input('chart-type-dropdown', 'value')]
)
def update_graph(contents, chart_type):
    if contents is None or len(contents) == 0:
        return px.bar(title='Upload one or more files to start')

    # Create an empty dataframe to store data from multiple files
    combined_df = pd.DataFrame()

    for content in contents:
        content_type, content_string = content.split(',')
        decoded = io.StringIO(base64.b64decode(content_string).decode('utf-8'))

        # Assuming CSV format, you can modify this for PDF parsing if needed
        df = pd.read_csv(decoded)

        # Concatenate data from multiple files
        combined_df = pd.concat([combined_df, df])

    # Create different types of charts based on user selection
    if chart_type == 'bar':
        fig = px.bar(combined_df, x=combined_df.columns[0], y=combined_df.columns[1],
                     color=combined_df.columns[1], title='Bar Chart from Uploaded Data')
    elif chart_type == 'pie':
        fig = px.pie(combined_df, names=combined_df.columns[0], title='Pie Chart from Uploaded Data')
    elif chart_type == 'line':
        fig = px.line(combined_df, x=combined_df.columns[0], y=combined_df.columns[1],
                      title='Line Chart from Uploaded Data')
    elif chart_type == 'histogram':
        fig = px.histogram(combined_df, x=combined_df.columns[1], title='Histogram from Uploaded Data')
    elif chart_type == 'area':
        fig = px.area(combined_df, x=combined_df.columns[0], y=combined_df.columns[1],
                      title='Area Chart from Uploaded Data')
    elif chart_type == 'scatter':
        fig = px.scatter(combined_df, x=combined_df.columns[0], y=combined_df.columns[1],
                         color=combined_df.columns[1], title='Scatter Plot from Uploaded Data')
    # Add more chart types as needed

    return fig

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
