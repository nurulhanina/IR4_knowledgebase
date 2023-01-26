#Import the required Libraries
import streamlit as st
import pandas as pd
import gspread
import oauth2client
from oauth2client.service_account import ServiceAccountCredentials

# define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/spreadsheets']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('gs_credential.json', scope)

client = gspread.authorize(creds)

# get the instance of the Spreadsheet
sheet = client.open('ir4_database')

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)

# authorize the clientsheet 
client = gspread.authorize(creds)
st.write(sheet_instance.cell(col=3,row=2))