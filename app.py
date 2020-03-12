import callbacks
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'Sentiment Analysis Comparison'
server = app.server
app.config.suppress_callback_exceptions = True


app.layout = html.Div([
    # Sidebar
    html.H1("Sentiment Analysis Comparison", className='text-center m-2'),
    # Center card
    dbc.Card([
        dcc.Textarea(id='text-area', rows=6, style={"resize": 'none'})
    ], className='col-m-12 m-2'),
    html.H3("Choose models:", className='m-2'),
    dcc.Checklist(id='model-list', options=[
        {"label": "NLTKSentiment", "value": "NLTKSentiment"}, 
        {"label": "TextBlob", "value": "TextBlob"}],
    inputStyle={
        "margin-left": "20px",
        "margin-right": "10px", 
    }, className='m-2'),
    # Submit button
    dbc.Button("Analyse Text!", id='analyse', 
    n_clicks=0, className='btn-default m-2'),
    dbc.Row(id="summary", className='col-m-6 m-2 justify-content-around')
])