import streamlit as st
import gspread
import oauth2client
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

#Define Database
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/spreadsheets']
creds = ServiceAccountCredentials.from_json_keyfile_name('gs_credential.json', scope)
client = gspread.authorize(creds)
sheet = client.open('ir4_database')
#Database - IR4 Term
sheet_instance1 = sheet.get_worksheet(0)
records_data1 = sheet_instance1.get_all_records()
df_term = pd.DataFrame.from_dict(records_data1)
#Database - IR4 Ontology
sheet_instance2 = sheet.get_worksheet(1)
records_data2 = sheet_instance2.get_all_records()
df_ont = pd.DataFrame.from_dict(records_data2)
#Database - IR4 New
sheet_instance3 = sheet.get_worksheet(2)
records_data3 = sheet_instance3.get_all_records()
df_new = pd.DataFrame.from_dict(records_data3)
url_image="Resources/Header.png"

def homepage():
    st.title("SISTEM ISTILAH DWIBAHASA")
    st.image(url_image)
    st.caption("Hello and Good Day. This is Nurul Hanina's Final Year Project. \nThis project is about a web Dictionary Application that allows user to search terminologies that are related to the domain of the 4th Industrial Revolution")

    st.write("Do Hover to the Left Navigation Pane to use the Application")

    st.write("\nDo give your feedback :)")

    link = '[FORM](https://forms.gle/gx4zfkXVRBXCw9M87)'
    st.markdown(link, unsafe_allow_html=True)

    st.write("\nHere are some helpful tips")

    with st.expander("Search Page"):
        st.caption("This page allows users to search for the terminology that they are looking for. The application also provides the Malay Translation, Synonms and its Ontological Parent Class of the terminology.")
    with st.expander("Knowledge Expert Page"):
        st.caption("This page is for users that are experts within the domain who can add to the knowledge base.")
    with st.expander("Upload Page"):
        st.caption("This page allows users to add any articles/journals/research papers that is related to the domain where the application can retrieve the keywords of the sources to be added to the knowledge base.")
    with st.expander("Glossary Page"):
        st.caption("This page displays all the terminologies that are within the knowledge base.")
    
#TODO - Add more explanation to each of the expanders

def searchpage():
    st.title("Sistem Istilah Dwibahasa")
    st.image(url_image)
    st.header("Search Query")
    # define the scope
    
    
def knowledgepage():
    st.title("Sistem Istilah Dwibahasa")
    st.markdown("Search Query")
    
def uploadpage():
    st.title("Sistem Istilah Dwibahasa")
    st.markdown("Search Query")
    
def glossarypage():
    st.title("Sistem Istilah Dwibahasa")
    st.markdown("Search Query")
    
st.sidebar.title('Navigation Pane')
options = st.sidebar.radio('Select what you want to display:', ['Home', 'Search Page', 'Knowledge Expert', 'Upload Page','Glossary Page'])


if options=='Home':
    homepage()
elif options=='Search Page':
    searchpage()
elif options=='Knowledge Expert Page':
    knowledgepage()
elif options=='Upload Page':
    uploadpage()
elif options=='Glossary Page':
    glossarypage()
  


           



