import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
nltk.download('wordnet')
from nltk.corpus import stopwords
nltk.download('stopwords') 
import pandas as pd
import math
import re
from scipy.sparse import coo_matrix

def get_top_n_words(corpus, n=None):\
    vec = CountVectorizer().fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0) 
    words_freq = [(word, sum_words[0, idx]) for word, idx in      
                   vec.vocabulary_.items()]
    words_freq =sorted(words_freq, key = lambda x: x[1], 
                       reverse=True)
    return words_freq[:n]

def get_top_n2_words(corpus, n=None):
    vec1 = CountVectorizer(ngram_range=(2,2),  
            max_features=2000).fit(corpus)
    bag_of_words = vec1.transform(corpus)
    sum_words = bag_of_words.sum(axis=0) 
    words_freq = [(word, sum_words[0, idx]) for word, idx in     
                  vec1.vocabulary_.items()]
    words_freq =sorted(words_freq, key = lambda x: x[1], 
                reverse=True)
    return words_freq[:n]

def get_top_n3_words(corpus, n=None):
    vec1 = CountVectorizer(ngram_range=(3,3), 
           max_features=2000).fit(corpus)
    bag_of_words = vec1.transform(corpus)
    sum_words = bag_of_words.sum(axis=0) 
    words_freq = [(word, sum_words[0, idx]) for word, idx in     
                  vec1.vocabulary_.items()]
    words_freq =sorted(words_freq, key = lambda x: x[1], 
                reverse=True)
    return words_freq[:n]
    

def sort_coo(coo_matrix):
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)
 
def extract_topn_from_vector(feature_names, sorted_items, topn=25):
    
    # Use only topn items from vector
    sorted_items = sorted_items[:topn]
    score_vals = []
    feature_vals = []
    
    # Word index and corresponding tf-idf score
    for idx, score in sorted_items:
        
        # Keep track of feature name and its corresponding score
        score_vals.append(round(score, 3))
        feature_vals.append(feature_names[idx])
 
    # Create tuples of feature,score
    # Results = zip(feature_vals,score_vals)
    results= {}
    for idx in range(len(feature_vals)):
        results[feature_vals[idx]]=score_vals[idx]
    return results
    
    
        
def minetext(text):
    text_output={}
    text_dict=text.split(".")
    ds_count=len(text_dict)
    
    #Preprocessing
    stop_words = set(stopwords.words("english"))
    csw = set(line.strip() for line in open('custom-stopwords.txt'))
    csw = [sw.lower() for sw in csw]
    stop_words = stop_words.union(csw)
    
    corpus=[]
    for i in range(0,ds_count):
    
        # Remove punctuation
        txt = text_dict[i].strip(" ")
        txt = re.sub(r'[^a-zA-Z0-9]d+’', '',str(txt))
        txt = txt.strip(" ")
    
        # Convert to lowercase
        txt = txt.lower()
        # Convert to list from string
        txt = txt.split()
        #Remove Stop Words
        texts=[]
        for j in txt:
            if j not in stop_words:
                texts.append(j)
        txt = " ".join(texts)
        corpus.append(txt)
    
    # Tokenize the text and build a vocabulary of known words
    from sklearn.feature_extraction.text import CountVectorizer
    cv=CountVectorizer(max_df=0.8,stop_words=stop_words, max_features=10000, ngram_range=(1,3))
    X=cv.fit_transform(corpus)
    
    from sklearn.feature_extraction.text import CountVectorizer
    cv=CountVectorizer(max_df=0.8,stop_words=stop_words, max_features=1000, ngram_range=(1,3))
    X=cv.fit_transform(corpus)
    
    from sklearn.feature_extraction.text import TfidfTransformer 
    tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
    tfidf_transformer.fit(X)

    # Get feature names
    feature_names=cv.get_feature_names()
    
    tf_idf_list=[]
    for ind in range(ds_count-1):
        doc=corpus[ind]
        tf_idf_vector=tfidf_transformer.transform(cv.transform([doc]))
        tf_idf_list.append(tf_idf_vector)
        
    tfidflist={}
    tfidflist_val=[]
    for index in range(len(tf_idf_list)-1):
        # Sort the tf-idf vectors by descending order of scores
        sorted_items=sort_coo(tf_idf_list[index].tocoo())

        # Extract only the top n; n here is 25
        keywords=extract_topn_from_vector(feature_names,sorted_items,25)
        for inf in keywords:
            tfidflist[inf]=keywords[inf]
        
    sorted_tfidf=sorted(tfidflist.items(),key=lambda x:x[1])
    
    
    return tf_idf_list