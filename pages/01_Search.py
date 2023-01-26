import streamlit as st
import pandas as pd
import oauth2client
from oauth2client.service_account import ServiceAccountCredentials
import gspread

#UI Stuff
st.title("Sistem Istilah Dwibahasa")
st.markdown("Search Query")


