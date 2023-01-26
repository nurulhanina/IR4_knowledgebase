import streamlit as st
import webbrowser

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


           



