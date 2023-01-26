#Import the required Libraries
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# Functions for each of the pages
def home(uploaded_file):
    if uploaded_file:
        st.header('Begin exploring the data using the menu on the left')
    else:
        st.header('To begin please upload a file')

def data_summary(df):
    st.header('Statistics of Dataframe')
    st.write(df.describe())

def data_header(df):
    st.header('Header of Dataframe')
    st.write(df.head())

def displayplot(df):
    st.header('Plot of Data')
    

# Add a title and intro text
st.title('Earthquake Data Explorer')
st.text('This is a web app to allow exploration of Earthquake Data')

# Sidebar setup
st.sidebar.title('Sidebar')
upload_file = st.sidebar.file_uploader('Upload a file containing earthquake data')
#Sidebar navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select what you want to display:', ['Home', 'Data Summary', 'Data Header', 'Scatter Plot'])

# Check if file has been uploaded
if upload_file is not None:
    df = pd.read_csv(upload_file)

# Navigation options
if options == 'Home':
    home(upload_file)
elif options == 'Data Summary':
    data_summary(df)
elif options == 'Data Header':
    data_header(df)
elif options == 'Scatter Plot':
    displayplot(df)