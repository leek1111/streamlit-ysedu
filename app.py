# -*- coding:utf-8 -*-
import streamlit as st
from utils import html_temp
from utils import dec_temp
from eda_app import run_eda_app
from ml_app import run_ml_app
def main():
    st.markdown(html_temp, unsafe_allow_html=True)
    menu = ['HOME', 'EDA', 'ML', 'About']
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == 'HOME':
        st.subheader('HOME')
        st.markdown(dec_temp, unsafe_allow_html=True)
    elif choice == 'EDA':
        run_eda_app()
    elif choice == 'ML':
        run_ml_app()
    else:
        st.subheader('About')
if __name__ == "__main__":
    main()
