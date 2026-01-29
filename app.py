import streamlit as st
from sales.ui import render_sales

st.set_page_config(page_title="SAC Enterprise Pro", layout="wide")

if "auth" not in st.session_state:
    st.session_state.auth = True
    st.session_state.user = "admin"

if st.session_state.auth:
    render_sales(st.session_state.user)
