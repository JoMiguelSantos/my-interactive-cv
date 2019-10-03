
# coding: utf-8

# In[1]:


import pandas as pd
from dash.dependencies import Input,Output,State,Event
import dash_core_components as dcc
import dash_html_components as html
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import dash
import plotly.plotly as py
import plotly.graph_objs as go

# In[639]:


expInfo=dict(Customer_Service_AXA='Car insurance support/Car accident claim support',
        Customer_Service_ALLIANZ='Car insurance support/Car accident claim support',
        Research_Fellow_ULFAD='Designed a Beliefs, Knowledge, and Attitudes questionnaire assessing non-autistic associated cognitions about autistic subjects in general. Assessed estereotypical descriptions <br>of autistic persons from non-autistic persons. Analyzed the data and was chosen to report the results to the general audience. Main tools: Qualtrics, Excel and SPSS',
        Educational_Psychologist_Intern_ESAAA='Psychological support, at the educational level, in the areas of health and well-being, vocational orientation, and learning. <br>It stood out the work developed with students with learning difficulties (assessment and intervention) and bullying at the class level.',
        Tourism_Promoter_CARRISTUR='Sold tickets for the Yellow Bus tours and gave support to tourists about the city in multiple languages.',
        Tourism_Promoter_CARRISTUR_='Sold tickets for the Yellow Bus tours and gave support to tourists about the city in multiple languages.',
        Data_Analyst_Intern_EAYE='Data Wrangling, Analysis, and Reporting. Data extraction and cleaning in Excel. Data cleaning and Data Visualization in Tableau. <br>Data analysis and Reporting the main findings and trends to be used as Discussion boards.',
        Data_Analyst_Internship_N26='Performed EDA, Data Mining, Business Intelligence and Data Visualization, accessing the Database with SQL (PostgreSQL), created Dashboards and Google Sheets <br>automation with tools such as Python and Google Apps Script. Got also knowledge in tools such as JIRA, Metabase and Salesforce. ',
        Data_Analyst_N26='Handle analysis and reporting using mainly PostgreSQL, Python and Google Sheets to all stakeholders in CS and Operations as part of the Operations Intelligence Team',
        Volunteer_Tutor_Team_Leader_AdF='Student support to students with learning, emotional and social difficulties. <br>Social and emotional competences development for enabling students to cope with their social and emocional challenges.'
            )

pri_eduInfo=dict(BSc_Behavioural_Sciences_FPUL='Faculty of Psychology of the University of Lisbon. <b>Relevant Courses</b>: Introduction to Probability and Statistics to Applied Psychology (Using Excel and SPSS)<br>Statistics Applied to Psychology (Using SPSS), Research Methods in Psychology, Psychometry.',
        MSc_Educational_Psychology_FPUL='Faculty of Psychology of the University of Lisbon. <br>Master Thesis: Evaluation of the social and emotional needs in adolescence (Excel and SPSS used)',
        MSc_Business_Administration_ISCTE='Faculty of Economics and Business Administration of ISCTE Lisbon. Taught in English. <br><b>Relevant Courses</b>: Data Analysis, Modelling and Research (Using SPSS and Excel), Financial Accounting and Analysis, Introduction to Financial Accounting')

sec_eduInfo=dict(Erasmus_HUMBOLDT='Faculty of Economics and Business Administration at Humboldt-Universität, Berlin',
        Entrepreneurship='150h course on Entrepreneurship skills and methodologies',
        Tableau_Data_Visualisations='MOOC by Udacity <a href="https://eu.udacity.com/course/data-visualization-in-tableau--ud1006">link here</a>',
        Git_Version_Control='MOOC by Udacity <a href="https://eu.udacity.com/course/version-control-with-git--ud123">link here</a>',
        GitHub_Collaboration='MOOC by Udacity <a href="https://eu.udacity.com/course/github-collaboration--ud456">link here</a>',
        TransactSQL_Querying='MOOC by edX <a href="https://www.edx.org/course/querying-data-with-transact-sql">link here</a>',
        Real_Life_DataScience='20h Video Content MOOC by Udemy using SQL, SSIS and Tableau <a href="https://www.udemy.com/datascience/learn/v4/overview">link here</a>',
        SQL_DatabaseDesign='13h Video Content MOOC by Udemy using PostgreSQL <a href="https://www.udemy.com/sqldatabases/learn/v4/overview">link here</a>',
        MasterSQL_DataScience='9h Video Content MOOC by Udemy using PostgreSQL at Intermediate Level <a href="https://www.udemy.com/master-sql-for-data-science/learn/v4/overview">link here</a>',
        Complete_Python_Masterclass='42h Video Content MOOC by Udemy teaching how to use Python from top to bottom <a href="https://www.udemy.com/python-the-complete-python-developer-course/learn/v4/overview">link here</a>',
        Plotly_Dash_InteractivePythonDashboards='10h MOOC by Udemy that teaches how to use two open source libraries Plotly and Dash to build interactive Dashboards, just like this CV <a href="https://www.udemy.com/interactive-python-dashboards-with-plotly-and-dash/learn/v4/overview">link here</a>',
        MachineLearning_Python_DataScience='41h MOOC by Udemy Advanced course on Machine Learning using TensorFlow, Keras, SKLearn, etc. to deploy Neural Networks and other ML Algorithms <a href="https://www.udemy.com/machinelearning/learn/v4/overview">link here</a>',
        Python_DataScience_MachineLearning_Bootcamp='23h MOOC by Udemy on how to use libraries like Pandas, Numpy, Matplotlib, Seaborn and Machine Learning Algorithms using the SKLearn library <a href="https://www.udemy.com/python-for-data-science-and-machine-learning-bootcamp/learn/v4/overview">link here</a>'
                )

exp=dict(Customer_Service_AXA=pd.date_range('2010-09-01','2011-02-28'),
        Customer_Service_ALLIANZ=pd.date_range('2010-03-01','2010-08-30'),
        Research_Fellow_ULFAD=pd.date_range('2012-08-01','2013-09-30'),
        Educational_Psychologist_Intern_ESAAA=pd.date_range('2013-10-01','2014-09-01'),
        Tourism_Promoter_CARRISTUR=pd.date_range('2015-03-01','2016-09-30'),
        Tourism_Promoter_CARRISTUR_=pd.date_range('2017-04-02','2017-12-31'),
        Data_Analyst_Intern_EAYE=pd.date_range('2018-01-01','2018-04-30'),
        Data_Analyst_Internship_N26=pd.date_range('2018-05-01','2018-08-30'),
        Data_Analyst_N26=pd.date_range('2018-09-01','2018-11-30'),
        Volunteer_Tutor_Team_Leader_AdF=pd.date_range('2015-04-01','2016-09-01')
        )

pri_edu=dict(BSc_Behavioural_Sciences_FPUL=pd.date_range('2009-09-01','2012-09-01'),
        MSc_Educational_Psychology_FPUL=pd.date_range('2012-09-02','2014-11-01'),
        MSc_Business_Administration_ISCTE=pd.date_range('2015-09-01','2017-10-01')
            )

sec_edu=dict(Erasmus_HUMBOLDT=pd.date_range('2016-10-01','2017-04-01'),
        Entrepreneurship=pd.date_range('2014-09-01','2014-12-01'),
        Tableau_Data_Visualisations=pd.date_range('2017-12-01','2017-12-31'),
        Git_Version_Control=pd.date_range('2018-01-01','2018-01-31'),
        GitHub_Collaboration=pd.date_range('2018-01-01','2018-01-31'),
        TransactSQL_Querying=pd.date_range('2018-02-01','2018-02-10'),
        Real_Life_DataScience=pd.date_range('2018-02-11','2018-03-10'),
        SQL_DatabaseDesign=pd.date_range('2018-03-11','2018-03-31'),
        MasterSQL_DataScience=pd.date_range('2018-04-01','2018-04-30'),
        Complete_Python_Masterclass=pd.date_range('2018-05-01','2018-06-30'),
        Plotly_Dash_InteractivePythonDashboards=pd.date_range('2018-10-01','2018-10-31'),
        MachineLearning_Python_DataScience=pd.date_range('2018-11-01','2018-11-30'),
        Python_DataScience_MachineLearning_Bootcamp=pd.date_range('2018-08-01','2018-09-30'))


# In[640]:


listOfExp = [pd.Series(index=exp.get(j), name=j, data=np.ones(len(exp.get(j)))*1.15) for j in exp.keys()]
listOfPriEdu = [pd.Series(index=pri_edu.get(j), name=j, data=np.ones(len(pri_edu.get(j)))*1.1) for j in pri_edu.keys()]
listOfSecEdu = [pd.Series(index=sec_edu.get(j), name=j, data=np.ones(len(sec_edu.get(j)))*1.05) for j in sec_edu.keys()]


# In[641]:


dataExp = pd.concat(listOfExp, axis=1).stack()
dataExp.index.set_names(['dates','names'], inplace=True)
dataExp = pd.concat([dataExp.reset_index(),dataExp.reset_index()['names'].map(expInfo)], axis=1)
dataPriEdu = pd.concat(listOfPriEdu, axis=1).stack()
dataPriEdu.index.set_names(['dates','names'], inplace=True)
dataPriEdu = pd.concat([dataPriEdu.reset_index(),dataPriEdu.reset_index()['names'].map(pri_eduInfo)], axis=1)
dataSecEdu = pd.concat(listOfSecEdu, axis=1).stack()
dataSecEdu.index.set_names(['dates','names'], inplace=True)
dataSecEdu = pd.concat([dataSecEdu.reset_index(),dataSecEdu.reset_index()['names'].map(sec_eduInfo)], axis=1)


# In[642]:


dataExp.columns = [['dates','names','value','description']]
dataPriEdu.columns = [['dates','names','value','description']]
dataSecEdu.columns = [['dates','names','value','description']]
# dataExp[dataExp.iloc[:,1] == 'Volunteer_Tutor_Team_Leader_AdF'] = 0.95


# In[643]:


all_df = pd.concat([dataExp,dataPriEdu,dataSecEdu], axis=0)


# In[644]:


trace_exp = go.Scatter(
    x=dataExp['dates'].iloc[:,0],
    y=dataExp['value'].iloc[:,0],
    text = dataExp['names'].iloc[:,0].astype(str),
    mode='markers',
    line = dict(color = 'red'),
    marker = dict(colorscale='jet'),
    opacity = 0.8,
    name = 'Experience',
    hoverinfo='text+name',
    connectgaps=False,
    fill='none')

trace_pri_edu = go.Scatter(
    x=dataPriEdu['dates'].iloc[:,0],
    y=dataPriEdu['value'].iloc[:,0],
    text = dataPriEdu['names'].iloc[:,0].astype(str),
    mode='markers',
    line = dict(color = 'blue'),
    marker = dict(colorscale='jet'),
    opacity = 0.8,
    name = 'Primary Education',
    hoverinfo='text+name',
    connectgaps=False,
    fill='none')

trace_sec_edu = go.Scatter(
    x=dataSecEdu['dates'].iloc[:,0],
    y=dataSecEdu['value'].iloc[:,0],
    text = dataSecEdu['names'].iloc[:,0].astype(str),
    mode='markers',
    line = dict(color = 'green'),
    marker = dict(color='green'),
    opacity = 0.8,
    name = 'Secondary Education',
    hoverinfo='text+name',
    connectgaps=False,
    fill='none')

data = [trace_exp, trace_pri_edu, trace_sec_edu]

layout = go.Layout(
    hovermode='x',
    legend=dict(x=0.7,
                y=1.2,
                orientation='h'),
    xaxis=dict(
        rangeselector=dict(bgcolor='black',
                           activecolor='red',
                           font=dict(color='white'),
                           y=1.1,
            buttons=list([
                dict(count=6,
                     label='6months',
                     step='month',
                     stepmode='backward'),
                dict(count=1,
                     label='1year',
                     step='year',
                     stepmode='backward'),
                dict(count=2,
                     label='2years',
                     step='year',
                     stepmode='backward'),
                dict(count=9,
                     label='9years',
                     step='year',
                     stepmode='backward')
            ])
        ),
#         rangeslider=dict(
#             visible = True
#         ),
        type='date',
        side='top'
    ),
    yaxis=dict(visible=False,
              range=[0.8,1.2]
              ),
#     annotations=[
#                     dict(
#                         x='2018-11-30',
#                         y=1.2,
#                         xref='x',
#                         yref='y',
#                         text='Instructions',
#                         showarrow=False,
#                         arrowhead=7,
#                         ax=0,
#                         ay=-40,
#                         font=dict(
#                                 family='Courier New, monospace',
#                                 size=16,
#                                 color='white'
#                                  ),
#                         bordercolor='#c7c7c7',
#                         borderwidth=2,
#                         borderpad=4,
#                         bgcolor='black',
#                         opacity=0.8,
#                         hovertext='Hover Over Things To Get More Info| Use The Buttons On The Left To Select The Time Period'
#                         )
#                 ]
# #     margin=dict(l=50, b=0, t=50, r=15)
)

initial_range = [
    '2018-01-01', '2018-11-30'
]

fig = dict(data=data, layout=layout)
fig['layout']['xaxis'].update(range=initial_range)


# In[645]:


def shuffeler(imshuffling,n):
    if type(imshuffling) != type([]):
        imshuffling = list(imshuffling)
    shuffledList = []
    for i in range(n):
        np.random.shuffle(imshuffling)
        shuffledList.append(imshuffling.pop())
    return shuffledList


# In[646]:


basicSkills = ['Tableau','French']
intermediateSkills = ['SPSS','German','Marketing','Economics','Project Management']
advancedSkills = ['Python','Excel','SQL','Business Intelligence','Data Mining','Statistics','Spanish','Portuguese','English','Negotiation', 'Communication','Flexibility','Diligence']



x_data = basicSkills+intermediateSkills+advancedSkills
y1 = np.random.randn(50)+2
y2 = np.random.randn(50)+4
y3 = np.random.randn(50)+6

y_data = [y1]*len(basicSkills)+[y2]*len(intermediateSkills)+[y3]*len(advancedSkills)

colors = ['green']*1+['red']*1+['green']+['red']+['blue']*3+['green']*6+['red']*3+['blue']*4

data = []
for xd, yd, cls in zip(x_data, y_data, colors):
        data.append(go.Box(
            y=yd,
            name=xd,
            text=x_data,
            hoverinfo='name',
#             boxpoints='all',
#             jitter=0.5,
            whiskerwidth=0.2,
            fillcolor=cls,
            marker=dict(
                size=2,
            ),
            line=dict(width=1),
        ))


# format the layout
layout = go.Layout(showlegend=False,
                   height=300,
                   width=1400,
                   autosize=False,
        margin=dict(
        l=100,
        r=0,
        b=10,
        t=0,
                ),
        yaxis=dict(zeroline=False,
                   showgrid=False,
                   visible=True,
                  range=[0,8.5],
                  tickvals=[2,4,6],
                  ticktext=['Basic -->','Intermediate-->','Advanced-->'],
                  tickmode='array'),
        xaxis=dict(showgrid=False,
                   zeroline=False,
                   showticklabels=True,
                   visible=False),
        annotations=[
                    dict(
                        x=0.81,
                        y=8.12,
                        xref='x',
                        yref='y',
                        width=255,
                        height=13,
                        text='<b>Data Science</b>',
                        showarrow=False,
                        arrowhead=7,
                        ax=0,
                        ay=-40,
                        font=dict(
                                family='Courier New, monospace',
                                size=13,
                                color='white'
                                 ),
                        align='right',
                        bordercolor='#c7c7c7',
                        borderwidth=0.5,
                        borderpad=4,
                        bgcolor='green',
                        opacity=0.8,
                        hovertext='Python, Excel, SQL, Business Intelligence, Data Mining, Statistics, SPSS, Tableau'
                        ),
                    dict(
                        x=0.81,
                        y=7.5,
                        xref='x',
                        yref='y',
                        width=255,
                        height=15,
                        text='<b>Languages</b>',
                        showarrow=False,
                        arrowhead=7,
                        ax=0,
                        ay=-40,
                        font=dict(
                                family='Courier New, monospace',
                                size=12,
                                color='white'
                                ),
                        align='right',
                        bordercolor='#c7c7c7',
                        borderwidth=0.5,
                        borderpad=4,
                        bgcolor='red',
                        opacity=0.8,
                        hovertext='Spanish, Portuguese, English, German, French'
                        ),
                    dict(
                        x=0.81,
                        y=6.9,
                        width=255,
                        height=14,
                        xref='x',
                        yref='y',
                        text='<b>Soft Skills</b>',
                        showarrow=False,
                        arrowhead=7,
                        ax=0,
                        ay=-40,
                        font=dict(
                                family='Courier New, monospace',
                                size=13,
                                color='white'
                                ),
                        align='right',
                        bordercolor='#c7c7c7',
                        borderwidth=0.5,
                        borderpad=4,
                        bgcolor='blue',
                        opacity=0.8,
                        hovertext='Negotiation, Communication, Flexibility, Diligence, Marketing, Economics, Project Management'
                        ),
                    dict(
                        x=0,
                        y=7.5,
                        xref='x',
                        yref='y',
                        width=150,
                        height=52,
                        text='<b>Skills</b>',
                        showarrow=False,
                        arrowhead=7,
                        ax=0,
                        ay=-40,
                        font=dict(
                                family='Courier New, monospace',
                                size=36,
                                color='black'
                                ),
                        bordercolor='#c7c7c7',
                        borderwidth=2,
                        borderpad=4,
                        bgcolor='white',
                        opacity=0.8,
                        hovertext='Each Color = Each Different Skill | The Higher, The More Proficient'
                        )
                    ]
                )

figure = go.Figure(data,layout)


# In[647]:


app = dash.Dash()
server = app.server

# In[648]:


app.layout = html.Div([
                        html.H1(id='name',
                                children='João Santos',
                                style=dict(textAlign='center')
                               ),
                        html.Div([
#                                 html.P('Location: Berlin',style=dict(display='inline',padding=20)),
                                html.A('Email',href='mailto:joaomsglds@gmail.com',style=dict(display='inline', padding=20)),
                                html.P('Phone: 015224659774',style=dict(display='inline', padding=20)),
                                html.A('LinkedIn',href='https://www.linkedin.com/in/joaomiguelopesantos/',style=dict(display='inline', padding=20))
                                 ],id='basic-info', style=dict(textAlign='center')
                                ),
                        html.Div([
                                dcc.Graph(id='exp',
                                          figure=fig)
                                ], style=dict(height='30vh')),
                       html.Div([
                                dcc.Graph(id='tables',
                                          figure=dict(data=[go.Table(
                                                          columnorder = [1,2],
                                                          columnwidth = [80,400],
                                                          header = dict(
                                                                        values = [['<b>TYPE</b>'],['<b>DESCRIPTION</b>']],
                                                                        line = dict(color = '#506784'),
                                                                        fill = dict(color = 'gray'),
                                                                        align = ['left','center'],
                                                                        font = dict(color = 'white', size = 12),
                                                                        height = 30
                                                                        ),
                                                          cells = dict(
                                                                    values = [['','',''],['','','']],
                                                                    line = dict(color = '#506784'),
                                                                    fill = dict(color = ['#25FEFD', 'white']),
                                                                    align = ['left','center'],
                                                                    font = dict(color = '#506784', size = 12),
                                                                    height = 30
                                                                      )
                                                                    )
                                                          ]
                                                        ,layout=go.Layout(margin=dict(l=20, b=10, t=0, r=10))
                                                        )
                                         )
                                ], style=dict(width='100%', height='20vh', verticalAlign='top', marginBottom=5, padding=0, float='top')
                               ),
                        html.Div([
                                dcc.Graph(id='skills',
                                          figure=figure)
                                ], style=dict(width='100%',height='30vh', marginTop=10, padding=10, float='top')
                                )
                    ])




# In[649]:


@app.callback(
    Output('tables','figure'),
    [Input('exp','hoverData')])
def display_hover_data(hoverData):
    textExp = ''
    textSecEdu = ''
    textPriEdu = ''
    try:
        if hoverData['points'][0]['text'] in dataPriEdu['names'].iloc[:,0].unique():
            infoPriEdu = hoverData['points'][0]['text']
            textPriEdu = dataPriEdu[dataPriEdu.iloc[:,1] == infoPriEdu]['description'].values[0]
        elif hoverData['points'][0]['text'] in dataSecEdu['names'].iloc[:,0].unique():
            infoSecEdu = hoverData['points'][0]['text']
            textSecEdu = dataSecEdu[dataSecEdu.iloc[:,1] == infoSecEdu]['description'].values[0]
        elif hoverData['points'][0]['text'] in dataExp['names'].iloc[:,0].unique():
            infoExp = hoverData['points'][0]['text']
            textExp = dataExp[dataExp.iloc[:,1] == infoExp]['description'].values[0]
    except:
        pass
    try:
        if hoverData['points'][1]['text'] in dataPriEdu['names'].iloc[:,0].unique():
            infoPriEdu = hoverData['points'][1]['text']
            textPriEdu = dataPriEdu[dataPriEdu.iloc[:,1] == infoPriEdu]['description'].values[0]
        elif hoverData['points'][1]['text'] in dataSecEdu['names'].iloc[:,0].unique():
            infoSecEdu = hoverData['points'][1]['text']
            textSecEdu = dataSecEdu[dataSecEdu.iloc[:,1] == infoSecEdu]['description'].values[0]
        elif hoverData['points'][1]['text'] in dataExp['names'].iloc[:,0].unique():
            infoExp = hoverData['points'][1]['text']
            textExp = dataExp[dataExp.iloc[:,1] == infoExp]['description'].values[0]
    except:
        pass
    try:
        if hoverData['points'][2]['text'] in dataPriEdu['names'].iloc[:,0].unique():
            infoPriEdu = hoverData['points'][2]['text']
            textPriEdu = dataPriEdu[dataPriEdu.iloc[:,1] == infoPriEdu]['description'].values[0]
        elif hoverData['points'][2]['text'] in dataSecEdu['names'].iloc[:,0].unique():
            infoSecEdu = hoverData['points'][2]['text']
            textSecEdu = dataSecEdu[dataSecEdu.iloc[:,1] == infoSecEdu]['description'].values[0]
        elif hoverData['points'][2]['text'] in dataExp['names'].iloc[:,0].unique():
            infoExp = hoverData['points'][2]['text']
            textExp = dataExp[dataExp.iloc[:,1] == infoExp]['description'].values[0]
    except:
        pass

    figure=dict(data=[go.Table(
                              columnorder = [1,2],
                              columnwidth = [80,400],
                              header = dict(
                                            values = [['<b>TYPE</b>'],['<b>DESCRIPTION</b>']],
                                            line = dict(color = 'black'),
                                            fill = dict(color = 'white'),
                                            align = ['left','center'],
                                            font = dict(color = 'black', size = 12),
                                            height = 20
                                            ),
                              cells = dict(
                                        values = [['<b>Experience</b>','<b>Primary Education</b>','<b>Secondary Education</b>'],[str(textExp)[2:-2],str(textPriEdu)[2:-2],str(textSecEdu)[2:-2]]],
                                        line = dict(color = ['#506784']), #, width=3
                                        fill = dict(color = [['red','blue','green'], 'white']),
                                        align = ['left'],
                                        font = dict(color = ['white','black'], size = 13),
                                        height = 35
                                          )
                                        )
                              ]
                            ,layout=go.Layout(margin=dict(l=15, b=0, t=0, r=10))
                            )
    return figure
#     return json.dumps(hoverData)


# In[650]:


if __name__ == '__main__':
    app.run_server()
