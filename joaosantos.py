import pandas as pd
from dash.dependencies import Input,Output,State,Event
import dash_core_components as dcc
import dash_html_components as html
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import dash
import plotly.offline as pyoff
import plotly.plotly as py
import plotly.graph_objs as go
import base64
import html5lib
import os, ssl

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

exp=dict(Customer_Service_AXA=pd.date_range('2010-09-01','2011-02-28'),
        Customer_Service_ALLIANZ=pd.date_range('2010-03-01','2010-08-30'),
        Research_Fellow_ULFAD=pd.date_range('2012-08-01','2013-09-30'),
        Educational_Psychologist_Intern_ESAAA=pd.date_range('2013-10-01','2014-09-01'),
        Tourism_Promoter_CARRISTUR=pd.date_range('2015-03-01','2016-09-30'),
        Tourism_Promoter_CARRISTUR_=pd.date_range('2017-04-02','2017-12-31'),
        Data_Analyst_Intern_EAYE=pd.date_range('2018-01-01','2018-04-30'),
        Data_Analyst_Internship_N26=pd.date_range('2018-05-01','2018-08-30'),
        Data_Analyst_N26=pd.date_range('2018-09-01','2019-05-31')
#         ,Volunteer_Tutor_Team_Leader_AdF=pd.date_range('2015-04-01','2016-09-01')
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
        MachineLearning_DataScience=pd.date_range('2018-11-01','2018-11-30'),
        Python_DataScience_MachineLearning_Bootcamp=pd.date_range('2018-08-01','2018-09-30'),
        WebDevelopment_Bootcamp=pd.date_range('2018-12-01','2018-12-31'),
        Python_PostgreSQL_Developer_Course=pd.date_range('2019-01-01','2019-01-31'),
        Spark_BigData_with_PySpark=pd.date_range('2019-01-16','2019-01-31'),
        Feature_Engineering_for_ML=pd.date_range('2019-03-01','2019-03-31'),
        Web_Scrapping_Python=pd.date_range('2019-05-01','2019-05-31'),
            )


expDict = [
          dict(date='Sep 2018 - Present',name='Data Analyst @N26',skills='Python, Forecast, Project Management, SQL, JIRA',description='Analysis and reporting for all stakeholders in Business Operations as part of Core Operations Intelligence Team. <br>Several projects owner including alert system, C-Level reporting and forecasting for all Business Operations'),
          dict(date='May 2018 - Aug 2018',name='Data Analyst Intern @N26',skills='Python, Google Sheets, SQL, Data Viz',description='Performed Data Mining, Business Intelligence and Data Visualization, using SQL, Python Dashboards and Google <br>Sheets automation with Python and Google Apps Script. Extra knowledge in: JIRA, Metabase and Salesforce.'),
          dict(date='Jan 2018 - Abr 2018',name='Data Analyst Intern @EAYE',skills='Excel, Tableau, Data Wrangling',description='Data Wrangling, Analysis, and Reporting. Data extraction and cleaning in Excel. Data Visualization in Tableau. <br>Data analysis and Reporting the main findings and trends to be used as Discussion boards.'),
          dict(date='Mar 2015 - Sep 2016/ Apr 2017 - Dec 2017',name='Tourism Promoter @CARRISTUR',skills='Sales, Negotiation, Languages',description='Sold tickets for the Yellow Bus tours and gave support to tourists about the city in multiple languages.'),
          dict(date='Oct 2013 - Aug 2014',name='Educational Psychologist Intern @ESAAA',skills='Assessment, Counseling, Intervention',description='Psychological support, with focus on health and well-being, vocational orientation, and learning. <br>Special focus on learning difficulties (assessment and intervention) and bullying.'),
          dict(date='Aug 2012 - Sep 2013',name='Research Fellow @UL/FAD',skills='Qualtrics, SPSS, Research, Presentation',description='Designed a Beliefs, Knowledge, and Attitudes questionnaire assessing non-autistic associated cognitions about <br>autistic subjects in general. Collected and analyzed the data, and reported the results to the general audience.'),
#           dict(date='Sep 2010 - Feb 2011',name='Customer Service @Allianz',skills='Communication, Listening',description='Car insurance support/Car accident claim support'),
#           dict(date='        Feb 2010 - <br>        Aug 2010',name='Customer Service @AXA',skills='Communication, Listening',description='Car insurance support/Car accident claim support')
          ]

priEduDict = [
          dict(date='Sep 2015 - Sep 2017',name='MSc Business Administration @ISCTE',skills='Economics, Marketing, Finance, Statistics, SPSS, Excel',description='Faculty of Economics and Business Administration of ISCTE, Lisbon. Taught in English. <br><b>Relevant Courses</b>: Data Analysis, Modelling and Research, Financial Accounting and Analysis, <br>Introduction to Financial Accounting'),
          dict(date='Sep 2012 - Nov 2014',name='MSc Educational Psychology @FPUL',skills='Assessment, Evaluation, Research, Project Management, SPSS',description='Faculty of Psychology of the University of Lisbon. <br><b>Master Thesis:</b> Evaluation of the social and emotional needs in adolescence'),
          dict(date='Sep 2009 - Aug 2012',name='BSc Behavioural Sciences @FPUL',skills='Research, Psychology, Statistics, SPSS, Excel',description='Faculty of Psychology of the University of Lisbon. <b>Relevant Courses</b>: Introduction to Probability and Statistics to <br>Applied Psychology Statistics Applied to Psychology, Research Methods in Psychology, Psychometry.'),
          ]

secEduDict = [
          dict(date='Mai 2018 - Mai 2018',name='Scrapy: Powerful Web Scraping & Crawling with Python @Udemy',skills='Web Scrapping, Web Crawling, Python, XPATH, HTML',description='9h MOOC by Udemy using Scrapy and Selenium to scrape common web pages with static and dynamic content <a href="https://www.udemy.com/scrapy-tutorial-web-scraping-with-python/">link here</a>'),
          dict(date='Mar 2018 - Mar 2018',name='Feature Engineering for Machine Learning w/Python @Udemy',skills='Pandas, Numpy, Python, Machine Learning, Scikit-Learn',description='7h MOOC by Udemy on Feature Engineering for Machine Learning <a href="https://www.udemy.com/feature-engineering-for-machine-learning/">link here</a>'),
          dict(date='Jan 2018 - Jan 2018',name='Spark and Python for Big Data with PySpark @Udemy',skills='Spark, EC2, PySpark, Python, Big Data',description='11h MOOC by Udemy on Python and Spark Big Data handling using PySpark with an AWS EC2 setup <a href="https://www.udemy.com/spark-and-python-for-big-data-with-pyspark/learn/v4/overview">link here</a>'),
          dict(date='Dec 2018 - Jan 2018',name='PostgreSQL & Python Developer Course @Udemy',skills='PostgreSQL, Python, Flask, OAuth, Bootstrap',description='22h MOOC by Udemy on Python and PostgreSQL advanced programming <a href="https://www.udemy.com/the-complete-python-postgresql-developer-course/learn/v4/overview">link here</a>'),
          dict(date='Dec 2018 - Dec 2018',name='Web Development Bootcamp @Udemy',skills='JavaScript, CSS, HTML, jQuery, NodeJS, MongoDB',description='46h MOOC by Udemy on Web Development using HTML, CSS, and Javascript as main tools with focus on Full Stack Development <a href="https://www.udemy.com/the-web-developer-bootcamp/learn/v4/overview">link here</a>'),
          dict(date='Nov 2018 - Nov 2018',name='Machine Learning w/Python @Udemy',skills='Python, TensorFlow, Keras, SKLearn, ML',description='41h MOOC by Udemy Advanced course on Machine Learning using TensorFlow, Keras, SKLearn, etc. to deploy Neural Networks and other ML Algorithms <a href="https://www.udemy.com/machinelearning/learn/v4/overview">link here</a>'),
          dict(date='Oct 2018 - Oct 2018',name='Interactive Data Viz w/Python @Udemy',skills='Python, Data Viz, Plotly, Dash, HTML, CSS',description='10h MOOC by Udemy that teaches how to use two open source libraries, Plotly and Dash, to build interactive Dashboards, just like this CV <a href="https://www.udemy.com/interactive-python-dashboards-with-plotly-and-dash/learn/v4/overview">link here</a>'),
          dict(date='Aug 2018 - Sep 2018',name='Data Science & ML @Udemy',skills='Python, ML, Matplotlib, Numpy, Pandas, Seaborn',description='23h MOOC by Udemy on how to use libraries like Pandas, Numpy, Matplotlib, Seaborn and Machine Learning Algorithms using the SKLearn library <a href="https://www.udemy.com/python-for-data-science-and-machine-learning-bootcamp/learn/v4/overview">link here</a>'),
          dict(date='Mai 2018 - Jun 2018',name='Complete Python Masterclass @Udemy',skills='Python',description='42h MOOC by Udemy teaching how to code with Python <a href="https://www.udemy.com/python-the-complete-python-developer-course/learn/v4/overview">link here</a>'),
          dict(date='Apr 2018 - Apr 2018',name='PostgreSQL Masterclass @Udemy',skills='SQL',description='9h MOOC by Udemy using PostgreSQL at Intermediate Level <a href="https://www.udemy.com/master-sql-for-data-science/learn/v4/overview">link here</a>'),
          ]

listOfExp = [pd.Series(index=exp.get(j), name=j, data=np.ones(len(exp.get(j)))*1.15) for j in exp.keys()]
listOfPriEdu = [pd.Series(index=pri_edu.get(j), name=j, data=np.ones(len(pri_edu.get(j)))*1.1) for j in pri_edu.keys()]
listOfSecEdu = [pd.Series(index=sec_edu.get(j), name=j, data=np.ones(len(sec_edu.get(j)))*1.05) for j in sec_edu.keys()]

dataExp = pd.concat(listOfExp, axis=1).stack().reset_index()
dataPriEdu = pd.concat(listOfPriEdu, axis=1).stack().reset_index()
dataSecEdu = pd.concat(listOfSecEdu, axis=1).stack().reset_index()

dataExp.columns = ['dates','names','value']
dataPriEdu.columns = ['dates','names','value']
dataSecEdu.columns = ['dates','names','value']

trace_exp = go.Scatter(
    x=dataExp['dates'],
    y=dataExp['value'],
    text = dataExp['names'],
    mode='markers',
    marker = dict(color='salmon'),
    opacity = 0.8,
    name = 'Experience',
    hoverinfo='text+name',
    connectgaps=False,
    fill='none')

trace_pri_edu = go.Scatter(
    x=dataPriEdu['dates'],
    y=dataPriEdu['value'],
    text = dataPriEdu['names'],
    mode='markers',
    marker = dict(color='paleturquoise'),
    opacity = 0.8,
    name = 'Formal Education',
    hoverinfo='text+name',
    connectgaps=False,
    fill='none')

trace_sec_edu = go.Scatter(
    x=dataSecEdu['dates'],
    y=dataSecEdu['value'],
    text = dataSecEdu['names'],
    mode='markers',
    marker = dict(color='goldenrod'),
    opacity = 0.8,
    name = 'Informal Education',
    hoverinfo='text+name',
    connectgaps=False,
    fill='none')

data = [trace_exp, trace_pri_edu, trace_sec_edu]

layout = go.Layout(
    title='<b>Timeline Overview</b>',
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
              range=[0.98,1.18]
              )
)

initial_range = [
    '2017-06-01', '2019-05-31'
]

fig = dict(data=data, layout=layout)
fig['layout']['xaxis'].update(range=initial_range)

figure=dict(data=[go.Table(
                              columnorder = [1,2,3,4],
                              columnwidth = [43,60,50,207],
                              header = dict(
                                            values = [['<b>DATE</b>'],['<b>NAME</b>'],['<b>SKILLS</b>'],['<b>DESCRIPTION</b>']],
                                            line = dict(color = 'black'),
                                            fill = dict(color = 'white'),
                                            align = ['left','center'],
                                            font = dict(color = 'black', size = 12),
                                            height = 13
                                            ),
                              cells = dict(
                                        values = [[i['date'] for i in expDict],['<em>'+i['name']+'</em>' for i in expDict],[i['skills'] for i in expDict],[i['description'] for i in expDict]],
                                        line = dict(color = ['#506784']), #, width=3
#                                         fill = dict(color = [['red','blue','green'], 'white']),
                                        align = ['left'],
                                        font = dict(color = ['black'], size = 13),
                                        height = 20
                                          )
                                        )
                              ]
                            ,layout=go.Layout(margin=dict(l=15, b=0, t=0, r=15))
                            )

app = dash.Dash()
server = app.server
app.config['suppress_callback_exceptions'] = True
# app.config.include_asset_files = True
# app.config.assets_folder = '/Users/joaosoares/PycharmProjects/untitled/assets'

# default values
# app.config.assets_folder = 'assets'     # The path to the assets folder.
# app.config.include_asset_files = True   # Include the files in the asset folder
# app.config.assets_external_path = ''    # The external prefix if serve_locally == False
# app.config.assets_url_path = '/assets'  # the local url prefix ie `/assets/*.js`

app.css.append_css({
   'external_url': (
       'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
       'https://use.fontawesome.com/releases/v5.5.0/css/all.css'
   )
})

#TABS
app.layout = html.Div([
    dcc.Tabs(id="tabs", value='basicInfo', children=[
        dcc.Tab(label='Introduction', value='basicInfo', style=dict(fontWeight=800)),
        dcc.Tab(label='Experience and Learning', value='XP', style=dict(fontWeight=800)),
        dcc.Tab(label='Skills', value='Skills', style=dict(fontWeight=800))
    ]),
    html.Div(id='tabs-content')
                      ], style=dict(marginBottom=0, paddingBottom=0)
                     )

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'basicInfo':
        return html.Div([
                        html.Div([
                                  html.Div([html.Img(src='https://www.dropbox.com/s/uy1t6mh5sy33p6l/12077205_1069339203118976_416413355_n.jpg?raw=1',
                                                     className='d-none d-lg-flex img-thumbnail img-fluid col-6 p-1',
                                                     style=dict(width='150px', height='300px')
                                                  ),
                                            html.Div([
                                                      html.H1(id='name',
                                                              children='João Santos',
                                                              className='col-12 d-flex justify-content-start align-items-end px-0'
                                                               ),
                                                      html.Div([html.H3('Data Analyst'),
                                                                html.Span([html.I(className='fas fa-at'),
                                                                           html.A('joaomsglds@gmail.com',href='mailto:joaomsglds@gmail.com'                                                                               )
                                                                          ],className='d-block'
                                                                         ),
                                                                html.Span([html.I(className='fas fa-mobile-alt'),
                                                                           html.P(' +351916067553',
                                                                                   className='font-weight-normal d-inline'
                                                                                  )
                                                                          ],className='py-2 m-0 d-block'
                                                                         ),
                                                                html.Span([html.I(className='fab fa-whatsapp'),
                                                                           html.P(' +351916067553',
                                                                                   className='font-weight-normal d-inline'
                                                                                  )
                                                                          ],className='pb-2 d-block'
                                                                         ),
                                                                html.Span([html.I(className='fab fa-linkedin'),
                                                                           html.A('LinkedIn',href='https://www.linkedin.com/in/joaomiguelopesantos/',
                                                                       style=dict(padding=10)
                                                                                  )
                                                                          ],className='d-block'
                                                                         )
                                                                 ],id='basic-info',
                                                                className='col-12 justify-content-start align-items-start pl-2 m-0'
                                                                )
                                                      ], className='row col-6 p-0 m-0')
                                           ], className='jumbotron row col-5 p-4 mt-2'
                                          ),
                                  html.Div([
                                            html.H1('Random Facts About Me',
                                                    className='display-6 col-9 mb-3 border-bottom pb-1'),
                                            html.Div([html.H3('Volunteering'),
                                                     html.P('Tutor and Team Lead helping middle school children with emotional and learning support')
                                                     ],className='col-6 px-3'),
                                            html.Div([html.H3('Sports'),
                                                     html.P('Winter + Mountains = Snowboard',
                                                           className='mb-0'),
                                                     html.P('Teamwork + Fitness = Football',
                                                           className='mb-0'),
                                                     html.P('Coordenation + Flexibility = Tennis',
                                                           className='mb-0')
                                                     ],className='col-6 px-0 align-content-start'),
                                            html.Div([html.H3('Interests'),
                                                     html.P('Data Science - Psychology, Business, and Technology in one amazing bundle',
                                                           className='mb-0'),
                                                     html.P('Technology - Excited to harness all the power of new technologies',
                                                           className='mb-0'),
                                                     html.P('Motorcycles - Speed freak and adrenaline junky',
                                                           className='mb-0')
                                                     ],className='col-12 mt-0 align-content-start')
                                           ], className='row col-7 align-content-start pt-4 ml-2 pl-5 pr-0')
                                 ], className='row mt-4 bg-light rounded pt-2'),
                        html.Div([
                                 html.Div([
                                     html.H3(['Summary'],
                                            className='pb-0 mb-2'),
                                     html.P(['1 Year Exp in Data Science'],
                                            className='pb-0 mb-1'),
                                     html.P(['1 BSc + 2 MSc'],
                                            className='pb-0 mb-1'),
                                     html.P(['10+ Data Science MOOCs'],
                                            className='pb-0 mb-1'),
                                     html.P(['4 Stats courses @University'])
                                         ], className='col-2 ml-0 pl-3 pt-2 align-content-start'),
                                 html.Div([
                                     html.H3(['Info About This CV']),
                                     html.P(['This CV was built as a demonstration of my skills using programming languages such as Python, HTML and CSS. The intended purpose is to show how Front-End frameworks can work together with Data Science to provide informative Visualizations.'])
                                          ], style=dict(lineHeight=1.6),
                                            className='col-3 pt-2'
                                         ),
                                 html.Div([
                                     html.H3(['Professional Feedback']),
                                     html.Div([
                                             html.P('"Proactively takes tasks, suggests improvements and completes them end to end"',
                                            className='pb-0 mb-1 font-italic'),
                                             html.P('"Puts a lot effort in getting minor issues resolved at 100% which is good but should be weighted against other more urgent tasks"',
                                            className='pb-0 mb-1 font-italic'),
                                             html.P('"Very diligent in completing tasks, spotting errors and fixing them proactively"',
                                            className='pb-0 mb-1 font-italic'),
                                             html.P('"Always eager to learn more and find new ways of solving problems"',
                                            className='pb-0 mb-1 font-italic'),
                                             html.P('"Challenges ideas and processes with the goal of providing improvements"',
                                            className='pb-0 mb-1 font-italic'),
                                             html.P('"Completes all his tasks in time with high quality"',
                                                   className='font-italic')
                                             ],className='pl-1')
                                          ], className='col-7 mx-0 pl-4 pr-1 pt-2'
                                         )
                                 ], className='row mt-4 bg-light rounded'
                                )
                     ],className='container'
                    )
    elif tab == 'XP':
        return html.Div([
                        html.Div([
                                dcc.Graph(id='exp',
                                          figure=fig,
                                          config=dict(displayModeBar=False)
                                         )
                                ],
                                style=dict(height='40vh', width='100vw'),
                                className='col-12'
                               ),
                        html.Div([dcc.RadioItems(id='table-options',
                                                 options=[dict(value=1, label=' Experience'),
                                                          dict(value=2, label=' Formal Education'),
                                                          dict(value=3, label=' Informal Education')
                                                         ],
                                                 labelStyle=dict(marginRight=10,
                                                                 fontWeight='bold'
                                                                ),
                                                 value=1,
                                                 className='btn btn-primary btn-sm'
                                                )
                                 ]
                                ,className='col-4 mx-auto'
                                ),
                        html.Div([
                                dcc.Graph(id='table',
                                          figure=figure,
                                          config=dict(displayModeBar=False)
                                         )
                                ],className='col-12 pt-1 pl-5 pr-3 mt-1'
                               )
                        ]
                       )
    elif tab == 'Skills':
        return html.Div([
                        html.Div(id='buttons',
                                 children=[
                                        html.Div(
                                                 [
                                            html.Button(id='data-skills',
                                                        children='Data Science',
                                                        n_clicks=0,
                                                        n_clicks_timestamp=-1,
                                                       style=dict(display='block', height='60px', width='200px'),
                                                       className='btn'),
                                            html.Button(id='code-skills',
                                                        children='Coding',
                                                        n_clicks=0,
                                                        n_clicks_timestamp=-1,
                                                       style=dict(display='block', height='60px', width='200px'),
                                                       className='btn'),
                                            html.Button(id='biz-skills',
                                                        children='Business Skills',
                                                        n_clicks=0,
                                                        n_clicks_timestamp=-1,
                                                       style=dict(display='block', height='60px', width='200px'),
                                                       className='btn'),
                                            html.Button(id='lang-skills',
                                                        children='Languages',
                                                        n_clicks=0,
                                                        n_clicks_timestamp=-1,
                                                       style=dict(display='block', height='60px', width='200px'),
                                                       className='btn')
                                                 ]
                                                )
                                            ],
                                               className='col-4 d-flex justify-content-end'
                                ),
                        html.Div([
                                dcc.Graph(id='my-skills',
                                         figure=dataSkills,
                                         config=dict(displayModeBar=False)
                                        )
                                 ],
                                    className='col-8')
                        ], className='row mx-auto justify-content-center'
                       )

dataSkills=dict(data=[go.Scatterpolar(
                          r = [39, 40, 38, 30, 35, 30, 35, 38, 15, 25, 39],
                          theta = ['Pandas','SQL', 'Research', 'Machine Learning', 'Statistics  ', 'Excel', 'Google <br>Sheets', 'Data Viz', 'Tableau', 'SPSS', 'Pandas'],
                          fill = 'toself',
                          line = dict(color='salmon'),
                          hoverinfo='none'
                                            )
                           ],

              layout= go.Layout(xaxis=dict(visible=False),
                                yaxis=dict(visible=False),
                                font=dict(size=14),
                                polar = dict(
                                            radialaxis = dict(
                                                              visible = True,
                                                              range = [0, 50],
                                                              tickvals=[15,25,35],
                                                              ticktext=['Basic','Intermediate','Advanced'],
                                                              tickmode='array',
                                                              tickangle=25,
                                                              tickfont=dict(
                                                                    family='Arial',
                                                                    size=13,
                                                                    color='#acb3bf'
                                                                            )
                                                                )
                                              ),
                                showlegend = False,
                                height=700,
                                width=700
                                )
             )

codeSkills=dict(data=[go.Scatterpolar(
                          r = [39, 30, 20, 15, 20, 35, 35, 28, 39],
                          theta = ['Python','Git', 'HTML', 'JavaScript    ', 'CSS', 'Metabase', '  Google <br>Sheets API', 'Docker', 'Python'],
                          fill = 'toself',
                          line = dict(color='paleturquoise'),
                          hoverinfo='none'
                                            )
                           ],

              layout= go.Layout(xaxis=dict(visible=False),
                                yaxis=dict(visible=False),
                                font=dict(size=14),
                                polar = dict(
                                            radialaxis = dict(
                                                              visible = True,
                                                              range = [0, 50],
                                                              tickvals=[15,25,35],
                                                              ticktext=['Basic','Intermediate','Advanced'],
                                                              tickmode='array',
                                                              tickangle=25,
                                                              tickfont=dict(
                                                                    family='Arial',
                                                                    size=13,
                                                                    color='#acb3bf'
                                                                            )
                                                                )
                                              ),
                                showlegend = False,
                                height=700,
                                width=700
                                )
             )

bizSkills=dict(data=[go.Scatterpolar(
                          r = [35, 38, 25, 20, 28, 39, 35, 35],
                          theta = ['Sales', '   Negotiation', 'Marketing', 'Finance  ', 'Economics   ', 'Project <br>Management', '<br> Presentation', 'Sales'],
                          fill = 'toself',
                          line = dict(color='goldenrod'),
                          hoverinfo='none'
                                            )
                           ],

              layout= go.Layout(xaxis=dict(visible=False),
                                yaxis=dict(visible=False),
                                font=dict(size=14),
                                polar = dict(
                                            radialaxis = dict(
                                                              visible = True,
                                                              range = [0, 50],
                                                              tickvals=[15,25,35],
                                                              ticktext=['Basic','Intermediate','Advanced'],
                                                              tickmode='array',
                                                              tickangle=25,
                                                              tickfont=dict(
                                                                    family='Arial',
                                                                    size=13,
                                                                    color='#acb3bf'
                                                                            )
                                                                )
                                              ),
                                showlegend = False,
                                height=700,
                                width=700
                                )
             )

langSkills=dict(data=[go.Scatterpolar(
                          r = [39, 38, 30, 20, 15, 39],
                          theta = ['Portuguese','English','Spanish', 'German', 'French', 'Portuguese'],
                          fill = 'toself',
                          line = dict(color='lightskyblue'),
                          hoverinfo='none'
                                            )
                           ],

              layout= go.Layout(xaxis=dict(visible=False),
                                yaxis=dict(visible=False),
                                font=dict(size=14),
                                polar = dict(
                                            radialaxis = dict(
                                                              visible = True,
                                                              range = [0, 50],
                                                              tickvals=[15,25,35],
                                                              ticktext=['Basic','Intermediate','Advanced'],
                                                              tickmode='array',
                                                              tickangle=25,
                                                              tickfont=dict(
                                                                    family='Arial',
                                                                    size=13,
                                                                    color='#acb3bf'
                                                                            )
                                                                )
                                              ),
                                showlegend = False,
                                height=700,
                                width=700
                                )
             )

@app.callback(
    Output('table','figure'),
    [Input('table-options','value')])
def display_table(value):
    if value == 1:
        tableData = expDict
    elif value == 2:
        tableData = priEduDict
    elif value == 3:
        tableData = secEduDict
    figure=dict(data=[go.Table(
                              columnorder = [1,2,3,4],
                              columnwidth = [43,60,50,207],
                              header = dict(
                                            values = [['<b>DATE</b>'],['<b>NAME</b>'],['<b>SKILLS</b>'],['<b>DESCRIPTION</b>']],
                                            line = dict(color = 'black'),
                                            fill = dict(color = 'white'),
                                            align = ['left','center'],
                                            font = dict(color = 'black', size = 12),
                                            height = 13
                                            ),
                              cells = dict(
                                        values = [[i['date'] for i in tableData],['<em>'+i['name']+'</em>' for i in tableData],[i['skills'] for i in tableData],[i['description'] for i in tableData]],
                                        line = dict(color = ['#506784']), #, width=3
                                        align = ['left'],
                                        font = dict(color = ['black'], size = 13),
                                        height = 20
                                          )
                                        )
                              ]
                            ,layout=go.Layout(margin=dict(l=15, b=0, t=0, r=15))
                            )
    return figure

@app.callback(Output('my-skills','figure'),
             [Input('data-skills', 'n_clicks'),
              Input('data-skills', 'n_clicks_timestamp'),
              Input('code-skills', 'n_clicks'),
              Input('code-skills', 'n_clicks_timestamp'),
              Input('biz-skills', 'n_clicks'),
              Input('biz-skills', 'n_clicks_timestamp'),
              Input('lang-skills', 'n_clicks'),
              Input('lang-skills', 'n_clicks_timestamp')])
def update_skills(button_1_clicks, button_1_timestamp, button_2_clicks, button_2_timestamp,button_3_clicks, button_3_timestamp,button_4_clicks, button_4_timestamp):
    if (button_1_timestamp == button_2_timestamp) and (button_1_timestamp == button_3_timestamp) and (button_2_timestamp == button_3_timestamp) and (button_4_timestamp == button_1_timestamp) and (button_4_timestamp == button_2_timestamp) and (button_4_timestamp == button_3_timestamp):
        return dataSkills
    elif (button_1_timestamp > button_2_timestamp) and (button_1_timestamp > button_3_timestamp) and (button_1_timestamp > button_4_timestamp):
        return dataSkills
    elif (button_2_timestamp > button_1_timestamp) and (button_2_timestamp > button_3_timestamp) and (button_2_timestamp > button_4_timestamp):
        return codeSkills
    elif (button_3_timestamp > button_1_timestamp) and (button_3_timestamp > button_2_timestamp) and (button_3_timestamp > button_4_timestamp):
        return bizSkills
    elif (button_4_timestamp > button_1_timestamp) and (button_4_timestamp > button_2_timestamp) and (button_4_timestamp > button_3_timestamp):
        return langSkills


def buttons_config(button_clicked,button):
    buttons_dict = {
                    '1':{'id':'data-skills',
                          'children':'Data Science',
                          'backgroundColor':'salmon'},
                    '2':{'id':'code-skills',
                          'children':'Programming',
                          'backgroundColor':'paleturquoise'},
                    '3':{'id':'biz-skills',
                          'children':'Business',
                          'backgroundColor':'goldenrod'},
                    '4':{'id':'lang-skills',
                          'children':'Languages',
                          'backgroundColor':'lightskyblue'}
                    }
    if button_clicked:
        return html.Button(id=buttons_dict[button]['id'],
                            children=buttons_dict[button]['children'],
                            n_clicks=1,
                            n_clicks_timestamp=0,
                            style=dict(display='block', height='60px', width='200px', backgroundColor=buttons_dict[button]['backgroundColor'])
                            )
    else:
        return html.Button(id=buttons_dict[button]['id'],
                            children=buttons_dict[button]['children'],
                            n_clicks=0,
                            n_clicks_timestamp=-1,
                            style=dict(display='block', height='60px', width='200px'))


@app.callback(Output('buttons','children'),
             [Input('data-skills', 'n_clicks'),
              Input('data-skills', 'n_clicks_timestamp'),
              Input('code-skills', 'n_clicks'),
              Input('code-skills', 'n_clicks_timestamp'),
              Input('biz-skills', 'n_clicks'),
              Input('biz-skills', 'n_clicks_timestamp'),
              Input('lang-skills', 'n_clicks'),
              Input('lang-skills', 'n_clicks_timestamp')])
def update_buttons_skills(button_1_clicks, button_1_timestamp, button_2_clicks, button_2_timestamp,button_3_clicks, button_3_timestamp,button_4_clicks, button_4_timestamp):
    if (button_1_timestamp == button_2_timestamp) and (button_1_timestamp == button_3_timestamp) and (button_2_timestamp == button_3_timestamp) and (button_4_timestamp == button_1_timestamp) and (button_4_timestamp == button_2_timestamp) and (button_4_timestamp == button_3_timestamp):
        return html.Div([
                                buttons_config(True,'1'),
                                buttons_config(False,'2'),
                                buttons_config(False,'3'),
                                buttons_config(False,'4')
                                ], style=dict(display='inline-block', marginTop=50)
                        )
    elif (button_1_timestamp > button_2_timestamp) and (button_1_timestamp > button_3_timestamp) and (button_1_timestamp > button_4_timestamp):
        return html.Div([
                                buttons_config(True,'1'),
                                buttons_config(False,'2'),
                                buttons_config(False,'3'),
                                buttons_config(False,'4')
                                ], style=dict(display='inline-block', marginTop=50)
                        )
    elif (button_2_timestamp > button_1_timestamp) and (button_2_timestamp > button_3_timestamp) and (button_2_timestamp > button_4_timestamp):
        return html.Div([
                                buttons_config(False,'1'),
                                buttons_config(True,'2'),
                                buttons_config(False,'3'),
                                buttons_config(False,'4')
                                ], style=dict(display='inline-block', marginTop=50)
                        )
    elif (button_3_timestamp > button_1_timestamp) and (button_3_timestamp > button_2_timestamp) and (button_3_timestamp > button_4_timestamp):
        return html.Div([
                                buttons_config(False,'1'),
                                buttons_config(False,'2'),
                                buttons_config(True,'3'),
                                buttons_config(False,'4')
                                ], style=dict(display='inline-block', marginTop=50)
                        )
    elif (button_4_timestamp > button_1_timestamp) and (button_4_timestamp > button_2_timestamp) and (button_4_timestamp > button_3_timestamp):
        return html.Div([
                                buttons_config(False,'1'),
                                buttons_config(False,'2'),
                                buttons_config(False,'3'),
                                buttons_config(True,'4')
                                ], style=dict(display='inline-block', marginTop=50)
                        )

if __name__ == '__main__':
    app.run_server()
