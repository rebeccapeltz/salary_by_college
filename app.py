from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Sample Data
df = pd.DataFrame({"Degree":["Digital Marketing & Analytics", "Data Science", "Software Engineering","Digital Marketing & Analytics", "Data Science", "Software Engineering"],
                  "Salary":[80000, 70000, 90000,75000, 85000, 95000],
                  "College":["Meridian State University", "Meridian State University", "Meridian State University","Westfield College of Technology", "Westfield College of Technology", "Westfield College of Technology"]
                  })

# Define your color mapping
COLLEGE_COLORS = {
    "Meridian State University": "#9467bd",
    "Westfield College of Technology": "#ff7f0e"
}

fig = px.bar(df, 
             x="Degree", 
             y="Salary", 
             color="College", 
             barmode="group",
             template="plotly_dark",
             color_discrete_map=COLLEGE_COLORS
             )

app.layout = html.Div([
    html.H1(children='Salary by Degree and College', 
            style={
                'textAlign':'center'}),

    dcc.Graph(id='example-graph', 
              figure=fig,
            style={'height': '350px', 'width': '100%'} 
    ),

    html.Div(
        children='Select a college to see the data:',
        style={'textAlign': 'center', 'color': 'white', 'fontSize': '18px'}
    ),

    dcc.Dropdown(
        id='college-dropdown',
        options=[
            {'label': 'Meridian State University', 'value': 'Meridian State University'},
            {'label': 'Westfield College of Technology', 'value': 'Westfield College of Technology'}
        ],
        value='Meridian State University',  # Default value
        style={
            'backgroundColor': 'black',
            'color': 'white'
        }
    ),
    dcc.Graph(id='college-graph',
            style={'height': '350px', 'width': '100%'})
], className="app-container", style={
    'backgroundColor': 'black',
    'color': 'white',
    'minHeight': '100vh'
})


@app.callback(
    Output('college-graph', 'figure'),
    [Input('college-dropdown', 'value')]
)
def update_graph(selected_college):
    filtered_df = df[df.College == selected_college]
    fig = px.bar(
        filtered_df,
        x="Degree",
        y="Salary",
        color="College",
        barmode="group",
        template="plotly_dark",
        color_discrete_map=COLLEGE_COLORS
    )
    return fig
    
if __name__ == '__main__':
    app.run_server(debug=True)