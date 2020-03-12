import dash
import dash_table
import dash_html_components as html
from app import app
from dash.dependencies import Input, Output, State
from api import get_scores


@app.callback(Output('summary', 'children'),
              [Input('analyse', 'n_clicks')],
              [State('text-area', 'value'),
               State('model-list', 'value')])
def analyse_text(n, text, methods):
    if n is not None and text is not None:
        df = get_scores(methods, text)
        return html.Div([
            dash_table.DataTable(
                id='table',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict("records"),
                )
            ])
    else:
        return None