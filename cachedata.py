import streamlit as st
import pandas as pd

@st.cache_data

def load_data():
    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
    return pd.read_csv(url)

df = load_data() # Now it's cached   
 
st.write(df.head())

