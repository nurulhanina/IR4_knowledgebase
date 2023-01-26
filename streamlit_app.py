import streamlit as st

def homepage():
    st.title("SISTEM ISTILAH DWIBAHASA")

    url="Resources/Header.png"
    st.image(url)
    #st.caption("")
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
    st.markdown("Search Query")
    # define the scope
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/spreadsheets']
    creds = ServiceAccountCredentials.from_json_keyfile_name('gs_credential.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('ir4_database')
    sheet_instance = sheet.get_worksheet(0)
    client = gspread.authorize(creds)
    st.write(sheet_instance.cell(col=3,row=2))
    
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
  


           



