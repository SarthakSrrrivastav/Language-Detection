import streamlit as st
import numpy as np
import pickle


st.title('LANGUAGE DETECTION')


load_model=pickle.load(open('trainedmodel.sav','rb'))

def predict(text):
    lang=load_model.predict([text])
    print('THE LANGUAGE IS : ',lang[0])