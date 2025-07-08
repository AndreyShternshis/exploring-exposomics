import dash
from dash import dcc, html, Input, Output, State, dash_table
import pandas as pd
import base64
import io

app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "Exposomics Toy App"

app.layout = html.Div([
    html.H1("Exposomics Tool (Demo)"),

    dcc.Tabs([
        dcc.Tab(label='Overview', children=[
            html.Div("Welcome to the exposomics dashboard demo.")
        ]),

        dcc.Tab(label='Upload Data', children=[
            html.H3("Upload your CSV file:"),
            dcc.Upload(
                id='upload-data',
                children=html.Button('Upload CSV'),
                multiple=False,
                style={'margin': '10px'}
            ),
            html.Div(id='output-table')
        ]),

        dcc.Tab(label='Analysis', children=[
            html.Div(id='analysis-output', children="No data yet. Upload a file to start analysis.")
        ])
    ])
])

# Global storage (not recommended for production)
uploaded_data = {}

@app.callback(
    Output('output-table', 'children'),
    Output('analysis-output', 'children'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename')
)
def handle_upload(contents, filename):
    if contents is None:
        return "No file uploaded.", "No data yet."

    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)

    try:
        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        uploaded_data['df'] = df

        table = dash_table.DataTable(
            data=df.head(10).to_dict('records'),
            columns=[{"name": i, "id": i} for i in df.columns],
            style_table={'overflowX': 'auto'},
            page_size=10
        )

        analysis_result = f"Uploaded file with {df.shape[0]} rows and {df.shape[1]} columns."
        return table, analysis_result

    except Exception as e:
        return f"Error processing file: {e}", "No data loaded."

server = app.server  # Needed for Render
if __name__ == '__main__':
    app.run_server(debug=True)