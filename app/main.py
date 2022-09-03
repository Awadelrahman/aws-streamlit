import streamlit as st
import pandas as pd
CONFIG_DICT = {"page_title": "SIPO", "page_icon": "💚", "layout": "centered"}
st.set_page_config(**CONFIG_DICT)
headerSection = st.container()
mainSection = st.container()


with headerSection:
    st.markdown("<h1 style='text-align: center; color: forestgreen;'>Smart Insulin Parameter Optimization</h1>",
                unsafe_allow_html=True)
    st.markdown(
        "<h1 style='text-align: center; color: forestgreen;'>SIPO</h1>", unsafe_allow_html=True)
with mainSection:

    uploaded_file = st.file_uploader(
        "Choose a CSV file", accept_multiple_files=False)
    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)
        st.write(df.head(10))
