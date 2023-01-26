import streamlit as st
import gspread
import oauth2client
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from PyPDF2 import *
import upload_mine as upMine

#Define Database
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/spreadsheets']
creds = ServiceAccountCredentials.from_json_keyfile_name('gs_credential.json', scope)
client = gspread.authorize(creds)
sheet = client.open('ir4_database')
#Database - IR4 Term
sheet_instance1 = sheet.get_worksheet(0)
records_data1 = sheet_instance1.get_all_records()
df = pd.DataFrame.from_dict(records_data1).dropna()
#Database - IR4 Ontology
sheet_instance2 = sheet.get_worksheet(1)
records_data2 = sheet_instance2.get_all_records()
df1 = pd.DataFrame.from_dict(records_data2).dropna()
#Database - IR4 New
sheet_instance3 = sheet.get_worksheet(2)
records_data3 = sheet_instance3.get_all_records()
df2 = pd.DataFrame.from_dict(records_data3).dropna()
url_image="Resources/Header.png"

#Declaration of variables
word_search=""
classType=["Additive Manufacturing", "Augmented Reality","Autonomous Robots","Big Data","Cloud Computing", "Cyber Physical System","Internet of Service", "Internet of Things","Simulation","Other"]
alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
l_alpha=[]
text_raw="Test"


#DataFrame
eng_word=list(df['EN'])
malay_word=list(df['MY'])
eng_def=list(df['DEF_EN'])
malay_def=list(df['DEF_MY'])
eng_ref=list(df1['EN'])
type0=list(df1['type1'])
type1=list(df1['type2'])
type2=list(df1['type3'])
type3=list(df1['type4'])
type4=list(df1['type5'])
type5=list(df1['type6'])
type6=list(df1['type7'])
type7=list(df1['type8'])
type8=list(df1['type9'])
type9=list(df1['type10'])
sameas0=list(df1['sameas1'])
sameas1=list(df1['sameas2'])
sameas2=list(df1['sameas3'])
sameas3=list(df1['sameas4'])
sameas4=list(df1['sameas5'])
newword=list(df2['new'])

for i in range(len(alpha)):
    l=[]
    for j in eng_word:
        j=str(j)
        if j is not None:
            if j[0].isdigit():
                continue
            if j[0].lower()==alpha[i]:
                l.append(j)
    l_alpha.append(l)

#functions
def printtext(text_w):
    st.text(text_w)

def printwhole(count):
    st.subheader("English Text")
    st.text(word_search)
    eng_definition="\nDefinition: "+eng_def[count]
    st.text(eng_definition)
    
    st.subheader("Malay Translation")
    st.caption("This section shows the Malay Translation of the searched Terminology and it's definition")
    st.text(malay_word[count])
    st.text("Terjemahan: " + malay_def[count])
    
    st.subheader("Synonym")
    st.caption("This section shows any words that are synonym to the searched Terminology")
    if sameas0!="":
        printtext(sameas0[count])
    if sameas1!="":
        printtext(sameas1[count])
    if sameas2!="":
        printtext(sameas2[count])
    if sameas3!="":
        printtext(sameas3[count])
    if sameas4!="":
        printtext(sameas4[count])

    st.subheader("Hierarchy")
    st.caption("This section shows the Parent Class of the searched Terminology in the 4th Industrial Revolution domain")
    printtext(str(type0[count]))
    printtext(str(type1[count]))
    printtext(str(type2[count]))
    printtext(str(type3[count]))
    printtext(str(type4[count]))
    printtext(str(type5[count]))
    printtext(str(type6[count]))
    printtext(str(type7[count]))
    printtext(str(type8[count]))
    printtext(str(type9[count]))

def write_hierarchy():
    classadded=["","","","","","","","","",""]
    add_man = st.checkbox(classType[0])
    if add_man:
             classadded[0]="Additive Manufacturing"
    aug_real = st.checkbox(classType[1])
    if aug_real:
             classadded[1]="Augmented Reality"
    aut_rob = st.checkbox(classType[2])
    if aut_rob:
             classadded[2]="Autonomous Robots"
    big_data = st.checkbox(classType[3])
    if big_data:
             classadded[3]="Big Data"
    cl_comp = st.checkbox(classType[4])
    if cl_comp:
             classadded[4]="Cloud Computing"
    cps = st.checkbox(classType[5])
    if cps:
             classadded[5]="Cyber Physical System"
    ios = st.checkbox(classType[6])
    if ios:
             classadded[6]="Internet of Service"
    iot = st.checkbox(classType[7])
    if iot:
             classadded[7]="Internet of Things"
    sim = st.checkbox(classType[8])
    if sim:
             classadded[8]="Simulation"
    other = st.checkbox(classType[9])
    if other:
             classadded[9]="Other"
    return classadded
            
def knowexp(cx,text):
    new_defen=""
    new_my=""
    new_defmy=""
    newclass=[]
    newsame=["","","","",""]
    st.text("\nThe word you selected is: "+text)
    new_defen=st.text_input("Insert the English Definition",key="DEF_EN")
    st.caption("Make sure that the spelling is correct")
    new_my=st.text_input("Insert the Terminology's Malay Definition",key="MY")
    st.caption("Make sure that the spelling is correct")
    new_defmy=st.text_input("Insert the Definition of the Terminology's Malay Translation",key="DEF_MY")
    st.caption("Make sure that the spelling is correct")
    classadd=write_hierarchy()
    newclass=classadd
    st.caption("Make sure that the spelling is correct")
    newsame[0]=(st.text_input("Insert the Synonym",key="SA1"))
    newsame[1]=(st.text_input("Insert the Synonym",key="SA2"))
    newsame[2]=(st.text_input("Insert the Synonym",key="SA3"))
    newsame[3]=(st.text_input("Insert the Synonym",key="SA4"))
    newsame[4]=(st.text_input("Insert the Synonym",key="SA5"))
    if st.button("Save"):
        new_row1=[text,new_my,new_defen,new_defmy]
        df.append(new_row1,ignore_index=True)
        new_row2=[text,newclass[0],newclass[1],newclass[2],newclass[3],newclass[4],newclass[5],newclass[6],newclass[7],newclass[8],newclass[9],newsame[0],newsame[1],newsame[2],newsame[3],newsame[4]]
        sheet_instance1.append_row(new_row1)
        sheet_instance2.append_row(new_row2)
        if cx>0 :
            sheet_instance3.delete_row(cx)
            
def gloss_column(ij):
    l=l_alpha[ij]
    if l:gloss_err(ij)
    else:st.write("There is no terminology that starts with this letter")
          
def gloss_err(i):
    l=l_alpha[i]
    url="https://www.google.com/"  #for testing purpose
    
    colms=st.columns((1,2,1))
    field=["No.","Terminology","Search"]
    
    for col, field_Name in zip(colms, field):
        col.write(field_Name)
        
    for x, idx in enumerate(l):
        col1,col2,col3=st.columns((1,2,1))
        col1.write(x)
        col2.write(l[x])
        button="Search" 
        button_phold=col3.empty()
        do_action=button_phold.button(button,key=x+(i*1000))
        if do_action:
            printquery(l[x])
            button_phold.empty()
            
def printquery(textq):
    count=0
    for i in eng_word:
        if textq.lower()==i.lower():
            printwhole(count)
            break
        count+=1

def show_text(t):
    st.caption("This is the text that has been uploaded")
    st.markdown(t)
    st.caption("Press Process to begin")
    text_raw=t
    return text_raw
        
#Functions for PDF extraction
def pdf_page_num(pdf_file):
    reader = PdfReader(pdf_file)
    page_num = len(reader.pages)
    return page_num

def clean_pdf(pdf):
    lines = [line for line in pdf.split('\n') if line.strip()]
    return lines

def extract_pdf(pdf_file,s,e):
    reader = PdfFileReader(pdf_file)
    pdftext=[]
    for page in range(s,e):
            content=reader.getPage(page).extract_text()
            pdftext.append(content)
    pdf_text="".join(pdftext)
    pdf_text=clean_pdf(pdf_text)
    pdf_text="".join(pdf_text)
    return pdf_text

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

def searchpage(searchtext):
    st.title("Sistem Istilah Dwibahasa")
    st.image(url_image)
    st.header("Search Query")
    word_search=st.text_input("Enter Text")
    st.caption("Do write the exact spelling of the terminology you want to search, or the result will be [Word Not Found]")
    if word_search:
        count=0
        for i in eng_word:
            if word_search.lower()==i.lower():
                printwhole(count)
                break
            count+=1
        if count>len(eng_word):
            printtext("Word Not Found")
            
def knowledgepage():
    
    st.title("Sistem Istilah Dwibahasa")
    st.image(url_image)
    st.header("Update Knowledge Base")
    
    knowledge_option=st.radio("What would you like to do?",('Automated Entry','New Entry'))
    
    if knowledge_option=='Automated Entry':
        colms=st.columns((1,2,1))
        field=["No.","Terminology","Select"]
        for cole, field_Namee in zip(colms, field):
            cole.write(field_Namee)
        for xe, idxe in enumerate(newword):
            cole1,cole2,cole3=st.columns((1,2,1))
            cole1.write(xe)
            cole2.write(newword[xe])
            button="Select" 
            button_phold=cole3.empty()
            do_action=button_phold.button(button,key=xe+(1000))
            if do_action:
                knowexp(xe+1,newword[xe])
                button_phold.empty() 
    
    
    elif knowledge_option=='New Entry':    
        exist=""
        new_entry=st.text_input("Enter New Terminology")
        for i in eng_word:
            if new_entry.lower()==i.lower():
                exist="The Terminology already existed in the Knowledge Base"
                printtext(exist)
                break
        if exist=="":
                knowexp(0,new_entry)
                                    
def uploadpage():
    text_mine=""
    st.title("Sistem Istilah Dwibahasa")
    st.image(url_image)
    st.header("Upload Sources")
    
    with st.expander("Uploading text"):
        st.caption("Upload a paragraph of a journal, research paper, newsletter to get your keywords.")
        text_upload=st.text_input("Enter Text")
        if text_upload:
            show_text(text_upload)
            text_mine=text_upload
            
    with st.expander("Uploading PDF File"):
        st.caption("Upload a PDF file of a journal, research paper, newsletter to get your keywords.")
        uploaded_file = st.file_uploader("Choose a file", "pdf")
        if uploaded_file is not None:
            st.caption("Choose the pages to be process")
            start=st.slider("Start Page",0,pdf_page_num(uploaded_file),3)
            end=st.slider("End Page",0,pdf_page_num(uploaded_file),3)
            if st.button("Confirm Pages"):
                upload_text=extract_pdf(uploaded_file,start,end)
                show_text(upload_text)
                text_mine=upload_text
                
    st.markdown("The Keywords Extracted")
    if text_mine!="":
        listmine=upMine.minetext(text_mine)
        for index_mine in range(len(listmine)):
            st.markdown(listmine[index_mine],key=index_mine)
    if st.button("Show"):
        st.markdown("reaction controlling', 0.116")
        st.markdown('proved system pedestrians, 0.116')
        st.markdown('proved system, 0.116')
        st.markdown('passing light gateway, 0.153')
            
    
def glossarypage():
    st.title("Sistem Istilah Dwibahasa")
    st.image(url_image)
    st.header("Glossary")
    with st.expander("A Glossary"):
        st.write("Letter A")
        gloss_column(0)
    
    with st.expander("B Glossary"):
        st.write("Letter B")
        gloss_column(1)
    
    with st.expander("C Glossary"):
        st.write("Letter C")
        gloss_column(2)
    
    with st.expander("D Glossary"):
        gloss_column(3)
    
    with st.expander("E Glossary"):
        gloss_column(4)
    
    with st.expander("F Glossary"):
        gloss_column(5)
    
    with st.expander("G Glossary"):
        gloss_column(6)
    
    with st.expander("H Glossary"):
        gloss_column(7)

    with st.expander("I Glossary"):
        gloss_column(8)
    
    with st.expander("J Glossary"):
        gloss_column(9)
    
    with st.expander("K Glossary"):
        gloss_column(10)
    
    with st.expander("L Glossary"):
        st.write("Letter L")
        gloss_column(11)
    
    with st.expander("M Glossary"):
        st.write("Letter M")
        gloss_column(12)
    
    with st.expander("N Glossary"):
        st.write("Letter N")
        gloss_column(13)
    
    with st.expander("O Glossary"):
        st.write("Letter O")
        gloss_column(14)
    
    with st.expander("P Glossary"):
        st.write("Letter P")
        gloss_column(15)
    
    with st.expander("Q Glossary"):
        st.write("Letter Q")
        gloss_column(16)
    
    with st.expander("R Glossary"):
        st.write("Letter R")
        gloss_column(17)

    with st.expander("S Glossary"):
        st.write("Letter S")
        gloss_column(18)
    
    with st.expander("T Glossary"):
        st.write("Letter T")
        gloss_column(19)
    
    with st.expander("U Glossary"):
        st.write("Letter U")
        gloss_column(20)
    
    with st.expander("V Glossary"):
        st.write("Letter V")
        gloss_column(21)
    
    with st.expander("W Glossary"):
        st.write("Letter W")
        gloss_column(22)
        
    with st.expander("X Glossary"):
        st.write("Letter X")
        gloss_column(23)
    
    with st.expander("Y Glossary"):
        st.write("Letter Y")
        gloss_column(24)
    
    with st.expander("Z Glossary"):
        st.write("Letter Z")
        gloss_column(25)
    
st.sidebar.title('Navigation Pane')
options = st.sidebar.radio('Select what you want to display:', ['Home', 'Search Page', 'Knowledge Expert Page', 'Upload Page','Glossary Page'])

if options=='Home':
    homepage()
elif options=='Search Page':
    searchpage("")
elif options=='Knowledge Expert Page':
    knowledgepage()
elif options=='Upload Page':
    uploadpage()
elif options=='Glossary Page':
    glossarypage()