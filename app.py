import streamlit as st
import pandas as pd
import plotly_express as px

#title
st.title("Sales Insights with Streamlit")

#description
st.write(""" 
# Explore different sales insights
""")


uploaded_file=st.sidebar.file_uploader(label="upload your CSV or Excel File.(200 max)",
                         type=['csv','xlsx'])


global df
if uploaded_file is not None:
        global df
        try:
            df = pd.read_csv(uploaded_file)
        except Exception as e:
            print(e)
            df = pd.read_excel(uploaded_file)

global columns
try:
    st.write(df)
    columns = list(df.select_dtypes(['float','int','object','category','datetime','timedelta']).columns)
except Exception as e:
    print(e)
    st.write("please upload the file")

chart_select = st.sidebar.selectbox(
    label = "Select the Chart Type",
    options=['Scatterplots', 'lineplots', 'barchart', 'areachart'])

if chart_select == 'Scatterplots':
    st.sidebar.subheader("Scatterplot Settings")
    try:
        x_values = st.sidebar.selectbox('X axis', options=columns)
        y_values = st.sidebar.selectbox('Y axis', options=columns)

        plot = px.scatter(data_frame=df, x=x_values, y=y_values)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if  chart_select == 'lineplots':
    try:
        x_values = st.sidebar.selectbox('X axis', options=columns)
        y_values = st.sidebar.selectbox('Y axis', options=columns)

        plot = px.line(data_frame=df, x=x_values, y=y_values)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == 'barchart':
    try:
        x_values = st.sidebar.selectbox('X axis', options=columns)
        y_values = st.sidebar.selectbox('Y axis', options=columns)

        plot = px.bar(data_frame=df, x=x_values, y=y_values)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)


if chart_select == 'areachart':
    try:
        x_values = st.sidebar.selectbox('X axis', options=columns)
        y_values = st.sidebar.selectbox('Y axis', options=columns)

        plot = px.area(data_frame=df, x=x_values, y=y_values)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)





