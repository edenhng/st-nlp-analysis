#Import Library
import streamlit as st
import os

#Work with Core NLP Libraries
import spacy_streamlit
import spacy
import gensim
import nltk
nltk.download('punkt')

#Sumy Summary Packages
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

#The Main Function
def main():
    #Title
    st.title("A policy briefing tool to assist Net Zero policy analysis")
    st.subheader("An internal product to deliver to DITT Economics")
    st.markdown("""
    ###Description
    +This is an app in the testing phased. Developed by Eden Hoang - a DITT graduate for DITT EAA.
    """)
    nlp = spacy.load('en_core_web_sm')
    menu = ["Home", "NER"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Home":
        st.subheader("Tokenization")
        raw_text = st.text_area("Your Text", "Enter Text Here")
        docx = nlp(raw_text)
        if st.button("Tokenize"):
            spacy_streamlit.visualize_tokens(docx, atrrs=['text', 'pos_', 'dep_', 'ent_type_'])
            
    elif choice == "NER":
        st.subheader("Named Entity Recognition")
        raw_text = st.text_area("Your Text", "Enter Text Here")
        docx = nlp(raw_text)
        spacy_streamlit.visualize_ner(docx, labels=nlp.get_pipe('ner').labels)

if __name__ == '__main__':
    main()
