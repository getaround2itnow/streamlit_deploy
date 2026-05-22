import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.DataFrame({
        "Fruit": ["Apple", "Banana", "Coconut", "Cherry", "Apple", "Banana", "Coconut", "Cherry"],
        "Amount": [4, 1, 2, 2, 4, 2, 1, 4],
        "City": ["Osaka", "Osaka", "Osaka", "Osaka", "Tokyo", "Tokyo", "Tokyo", "Tokyo"]
})
fig = px.bar(df, x = "Fruit", y = "Amount", color = "City", barmode = "group")
st.plotly_chart(fig)


# virtual environment
# python3 -m venv .venv
# source .venv/bin/activate
# may need to remove the dot '.' in the above 2 lines   
# your Streamlit virtual environment is active (venv)
# and an Anaconda/Miniconda base environment is also active (base)
# conda deactivate (use to deactivate base)