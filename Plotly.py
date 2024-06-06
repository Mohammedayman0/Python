#!/usr/bin/env python
# coding: utf-8

# In[1]:


from jupyter_dash import JupyterDash
from dash import html ,dcc, Dash
from dash.dependencies import Input,Output
import plotly.express as px
import pandas as pd


# In[ ]:


# app=Dash(external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
# app.layout=html.Div(children=[
#                     html.H1('My First Dashboard',style={'Color':'red','background':'black','textAlign':'center'}),
#                     html.P('Mohamed Ayman abbass Mohamed AymanMohamed AymanMohamed Ayman'),
#                     html.Hr(),
                    
#                     html.Div([
#                                 html.Div('My first Diiiiiv',className='four columns'),
#                                 html.Div('My Second Diiiiiv',className='four columns'),
#                                 html.Div( 'My Second Diiiiiv',className='four columns')
# ])
# ])
# #app.run_server()
# app.run_server(port=8051)


# In[ ]:


#https://codepen.io/chriddyp/pen/bWLwgP.css
#http://127.0.0.1:8051/


# In[2]:


from jupyter_dash import JupyterDash
from dash import html ,dcc, Dash
from dash.dependencies import Input,Output,State
import plotly.express as px
import pandas as pd
import dash


# In[3]:


df=px.data.gapminder()
df.head()


# In[7]:


px.scatter(df,x='gdpPercap',y='lifeExp',size='pop',color='continent',hover_name='country')


# In[108]:


#pp= dash.Dash()
app=Dash(external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

df=px.data.gapminder()
app.layout=html.Div([
    
    html.H1('My Dashboard'
            ,style={'textAlign':'center'}),
    
     dcc.Dropdown(['Asia', 'Europe', 'Africa', 'Americas', 'Oceania'],id='demo_dropdown',value=None,multi=True, placeholder='choose a continent...'
                 ), 
    
    dcc.Graph(id='myGraph'),
    
    
    
    dcc.Slider(
    id='my-slider',
    min=df['year'].min(),
    max=df['year'].max(),
    value=df['year'].min(),
    step=None,
    marks={str(year):str(year)
           for year in df['year'].unique()}
                )
   #dcc.Dropdown(['Asia', 'Europe', 'Africa', 'Americas', 'Oceania'],id='demo_dropdown',value=None,multi=True, placeholder='choose a continent...'
 #               )   
            ])



@app.callback(
    Output('myGraph', 'figure'),
    Input('my-slider', 'value'),
    Input('demo_dropdown', 'value')
)
def updategraph(value1, value2):
    if value2 is None or value2 == []:
        filtered_df = df[df['year'] == value1]
        fig = px.scatter(filtered_df, x='gdpPercap', y='lifeExp', size='pop', color='continent', hover_name='country') 
    else:
        filtered_df = df[(df['year'] == value1) & (df['continent'].isin(value2))]  
        fig = px.scatter(filtered_df, x='gdpPercap', y='lifeExp', size='pop', color='continent', hover_name='country')
       
    return fig 
    


# In[109]:


app.run_server()


# In[35]:


app2 = dash.Dash()
df = px.data.gapminder()

app2.layout = html.Div([
    html.H1('call back my example 2', style={'textAlign': 'center'}),
    dcc.Graph(id='myGraph'),
    dcc.Slider(
        id='my-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        step=None,
        marks={str(year): str(year) for year in df['year'].unique()}
    )
])


@app2.callback(Output('myGraph', 'figure'), [Input('my-slider', 'value')])
def updategraph(slidervalue):
    filtered_df = df[df['year'] == slidervalue]
    fig = px.scatter(filtered_df, x='gdpPercap', y='lifeExp', size='pop', color='continent', hover_name='country')
    return fig


# In[110]:


#app2.run_server()


# In[ ]:





# In[151]:


app3=Dash(external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

df=px.data.gapminder()
app3.layout=html.Div([
    
    html.H1('My Dashboard'
            ,style={'textAlign':'center'}),

    dcc.Graph(id='myGraph',className='twelve columns'),
    
    dcc.Graph(id='myGraph2',className='twelve columns'),

    dcc.Dropdown(['Asia', 'Europe', 'Africa', 'Americas', 'Oceania'],id='demo_dropdown',value=None,multi=True, placeholder='choose a continent...'
                 ),
    
    dcc.Slider(
    id='my-slider',
    min=df['year'].min(),
    max=df['year'].max(),
    value=df['year'].min(),
    step=None,
    marks={str(year):str(year)
           for year in df['year'].unique()}
                ),

    html.Button("Submit",id="Button")
            ])
@app3.callback(
    Output('myGraph', 'figure'),
    Output('myGraph2', 'figure'),
    State('my-slider', 'value'),
    State('demo_dropdown', 'value'),
    Input('Button','n_clicks')
)
def updategraph(value1, value2,n_clicks):
    if value2 is None or value2 == []:
        filtered_df = df[df['year'] == value1]
        fig = px.scatter(filtered_df, x='gdpPercap', y='lifeExp', size='pop', color='continent', hover_name='country',log_x=True ,size_max=60) 
        fig2 = px.scatter(filtered_df, x='gdpPercap', y='pop', size='pop', color='continent', hover_name='country',log_x=True ,size_max=60) 

    else:
        filtered_df = df[(df['year'] == value1) & (df['continent'].isin(value2))]  
        fig = px.scatter(filtered_df, x='gdpPercap', y='lifeExp', size='pop', color='continent', hover_name='country',log_x=True ,size_max=60)
        fig2 = px.scatter(filtered_df, x='gdpPercap', y='pop', size='pop', color='continent', hover_name='country',log_x=True ,size_max=60)

       
    return fig , fig2
    


# In[152]:


app3.run_server()


# In[4]:


app4=Dash(external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

df=px.data.gapminder()
app4.layout=html.Div([
    
    html.H1('My Dashboard'
            ,style={'textAlign':'center'}),

    dcc.Slider(
    id='my-slider',
    min=df['year'].min(),
    max=df['year'].max(),
    value=df['year'].min(),
    step=None,
    marks={str(year):str(year)
           for year in df['year'].unique()}
                ),
    
    dcc.Dropdown(['Asia', 'Europe', 'Africa', 'Americas', 'Oceania'],id='demo_dropdown',value=None,multi=True, placeholder='choose a continent...'
                 ),
    
    html.Button("Submit",id="Button"),
    
    dcc.Graph(id='myGraph',className='twilve columns'),
    
    dcc.Graph(id='myGraph2',className='twilve columns')
            ])


@app4.callback(
    Output('myGraph', 'figure'),
    Output('myGraph2', 'figure'),
    State('my-slider', 'value'),
    State('demo_dropdown', 'value'),
    Input('Button','n_clicks')
)
def updategraph(value1, value2,n_clicks):
    if value2 is None or value2 == []:
        filtered_df = df[df['year'] == value1]
        fig = px.scatter(filtered_df, x='gdpPercap', y='lifeExp', size='pop',color='continent', hover_name='country',log_x=True ,size_max=60) 
        fig2 = px.scatter(filtered_df, x='gdpPercap', y='pop', size='pop', color='continent', hover_name='country',log_x=True ,size_max=60) 

    else:
        filtered_df = df[(df['year'] == value1) & (df['continent'].isin(value2))]  
        fig = px.scatter(filtered_df, x='gdpPercap', y='lifeExp', size='pop',color='continent', hover_name='country',log_x=True ,size_max=60)
        fig2 = px.scatter(filtered_df, x='gdpPercap', y='pop', size='pop', color='continent', hover_name='country',log_x=True ,size_max=60)

       
    return fig , fig2
    


# In[5]:


app4.run_server()


# In[ ]:




