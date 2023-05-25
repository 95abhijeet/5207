import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly
import plotly.figure_factory as ff
import plotly.express as px



st.header("Exploration of streetlights & criminal offences")
st.subheader("1. Ottawa Map")
#1. map display
import streamlit as st
import streamlit.components.v1 as components

st.markdown("A visual representation of map of Ottawa that displays the count of "
            " crime with an ability to filter by year and the type of primary violation."
"The plot has filters, equip with slider button and check boxes to select the primary violation."
"Upon hover, selecting a specific neighbourhood will give you details as part of tooltip feature.")
HtmlFile = open("map2.html", 'r', encoding='utf-8')
htmlsample1 = HtmlFile.read()
print(htmlsample1)
components.html(htmlsample1,height=800,width=1000)

# 2.facet bubble-crime severity,brightness, population and crime rate
st.subheader("2. Facetted Bubble plots")
st.markdown("The facetted bubble plots display the correlation between population and brightness and crime rate, comparing individual factors. "
   "The legend shows crime severity level, safe: crime rate<30; less safe: crime rate 30-50; risky: crime rate 50-100, high risky: crime rate >100."
"To map the ordinal features of crime severity levels in a continuous color map, we encode the crime severity level with 1-4. "
 " 4 represents the high-risk level, 3 represents the risk level, 2 represents the less safe level, 1 represents the safe level. "
"When the mouse hovers on the bubbles, details about population, crime rate, severity, security appear. "
"The visual also has interactive tools, including play/pause that displays attributes over the years."
            )

st.text('Bubble size= brightness value')
import plotly.express as px
df2121 = pd.read_csv('new2.csv')
fig2121=px.scatter(df2121, x="population", y="crimerate", animation_frame="year", animation_group="neighborhood",
           size="brightness", color="crime severity level",color_continuous_scale=px.colors.sequential.Viridis, hover_name="neighborhood",facet_col="crime severity",

           log_x=True, size_max=65, range_x=[1000,40000], range_y=[0,200])
fig2121.update_layout(legend_traceorder="reversed")
st.plotly_chart(fig2121)

#3.parallel- crime type
st.subheader('3. Parallel Coordinate plot')
st.markdown('we use parallel coordinate plot for exploring the correlation between street lights, different crime types'
            ',population and crime rate. Due to limitation of the API, the neighborhood name cannot be labeled. We can observe'
            'the quantitative relation between different variables. Each line represent a neighborhood. '
       'This plot helps to plot multiple variables on parallel vertical axes. This can be useful for'
'the project as we have multiple variables like Neighbourhoods, Street light counts, Crime'
'rate, Crime types, time period of street light installation, time of crimes committed and'
'more. The Parallel Coordinate plot can showcase all the variables in a single plot and'
'can highlight the trend/pattern of the relations between different variables. ')
st.markdown('When pressing mouse and selects a specific line on the y axis, '
'we can observe the whole area/variables which the line represents. The selected area will be highlighted, '
            ' the rest will become dark.')

import plotly.express as px
df1414 = pd.read_csv('2019crimetype3.csv')
fig1414 = px.parallel_coordinates(df1414, color="brightness", labels={"Type": "brightness",
                  "Threat of violence": "threatofviolence", "Theft": "theft",
                  "Break in": "breakandenter", "Assaults": "assaults", },
                    color_continuous_scale=px.colors.sequential.Inferno, color_continuous_midpoint=300)
st.plotly_chart(fig1414)

#4.triangle-crime type in neighbourhood
# st.subheader('4. To what extent does a certain type of crime affect different neighborhoods?')
#
# df1616 = pd.read_csv('2019crimetype5.csv')
# fig1616 = px.scatter_ternary(df1616, a="assaults", b="theft", c="breakandenter", color="crimerate", size="brightness", hover_name="neighbourhoodd",
#                    size_max=35, color_continuous_scale=px.colors.sequential.Viridis,color_continuous_midpoint=20,animation_frame="crime severity", )
# st.plotly_chart(fig1616)


#5. the representative neighborhood
#st.subheader('5. Four types of correlation extracted from our observation')
# st.subheader('5. Freezing point:positive or negative')
#
# if st.button('Click and get the answer'):
#     st.write("Kanata-Katimavik")
# else:
#     st.write('Please continue to explore')
# import plotly.express as px
# st.text('Each piece of square represents one year')
# #kanata
# df2626 = pd.read_csv('casebycase4.csv')
# fig2626 = px.bar(df2626, x="neighbourhoodd", y="crimerate", color="brightness",animation_frame="type",
#              )
# st.plotly_chart(fig2626)


#5.Machine learning method to show the features ranking
st.subheader('4.Decision Tree approach')

if st.button('Press and check which neighborhood presents the positive correlation'):
    st.write("Kanata-Katimavik")
else:
    st.write(' ') #space with no statement
if st.button('Press and check the neighborhood safety factors ranking!'):
    st.write("1.lowincome 0.280341;\n\t 2.population 0.230722;\n\t 3.employed 0.205628;\n\t 4.medianage 0.182241;\n\t 5.brightness 0.101068;\n\t")
else:
    st.write(' ') #space with no statement

st.markdown("We use Decision Tree for analysis based on historical data. Decision Tree is a supervised machine learning"
            "method. Every branch represents an output, and each leaf node represents a classification. We use the trained model "
            "classifier for applying classification new data/objects. "
            "We introduce average age, population, employment and income to combine with brightness to observe the "
        "correlation between brightness and criminal offences. The below visualization show the inference process of "
        " Decision Tree- the machine learning method we used in this project. We want to get the factors importance "
        " ranking based on historical data for additional analysis. We also realize that machine learning is just "
        "a solution used in the process, and it cannot replace the analysis generated from our visualizations. ")
import streamlit as st
import streamlit.components.v1 as components

HtmlFile = open("viztree2.svg", 'r', encoding='utf-8')
htmlsample1 = HtmlFile.read()
print(htmlsample1)
components.html(htmlsample1,height=600,width=1000)


import time
with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Page loading complete')
st.balloons()

st.subheader('Summary')
st.markdown('Our system provides users the data on crime rates, street lights and population over 111 neighbourhoods in Ottawa city. '
            'This will allow the users to make informed decisions on the relevant matter.')

st.subheader('Credits')
st.markdown('This project was created by Ayushy Jain, Abhijeet Singh and Cathy Zhang for a graduate course 5207-Data Interaction Techniques '
            'at Carleton University taught by Dr.David Sprague.')

st.subheader("References")
st.write('1."Streamlit", https://docs.streamlit.io',)
st.write('2."Plotly",https://plotly.com/python')
st.write('3."Dreeviz",https://github.com/parrt/dtreeviz')
st.write('4."Skikit-learn",Scikit-learn: Machine Learning in Python, Pedregosa et al., JMLR 12, pp. 2825-2830, 2011.')
st.write('5."Pandas",Data structures for statistical computing in python, McKinney, Proceedings of the 9th Python in Science Conference, Volume 445, 2010.')
st.write('6.Ottawa map is produced by Tableau and Tableau public')
st.write("7.Ottawa Neighbourhood Study (ONS):https://open.ottawa.ca/datasets/ottawa-neighbourhood-study-ons-neighbourhood-boundaries-gen-2/explore?location=45.807893%2C-75.733052%2C0.00")
st.write("8.Criminal offences:https://open.ottawa.ca/documents/criminal-offences-/about")
st.write('10.Street lights:https://open.ottawa.ca/datasets/street-lights')
st.write('11.Crime rate and type: https://www.neighbourhoodstudy.ca')
