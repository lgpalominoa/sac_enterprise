import streamlit as st
from sales.ui import render_sales

# ==============================
# Inicialización del Session State
# ==============================
if "auth" not in st.session_state:
    st.session_state.auth = False

if "user" not in st.session_state:
    st.session_state.user = None

if "rol" not in st.session_state:
    st.session_state.rol = None

if "auth_step" not in st.session_state:
    st.session_state.auth_step = "login"

st.set_page_config(page_title="SAC Enterprise Pro", layout="wide")

if "auth" not in st.session_state:
    st.session_state.auth = True
    st.session_state.user = "admin"

if st.session_state.auth:
    render_sales(st.session_state.user)
