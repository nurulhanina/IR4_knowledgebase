import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
nltk.download('wordnet')
from nltk.corpus import stopwords
nltk.download('stopwords') 
import pandas as pd
import math
import re


def minetext(text):
    listtext=["Hehehe","HUHUHU"]
    text_dict=text.split(".")
    ds_count=len(text_dict)
    print(text_dict)
    text=text
    return listtext