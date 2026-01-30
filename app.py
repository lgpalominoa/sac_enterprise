import streamlit as st
from sales.ui import render_sales
from auth.login import login
from auth.twofa import iniciar_2fa, validar_otp

st.set_page_config(page_title="SAC Enterprise Pro", layout="wide")

# ==============================
# Inicialización del Session State
# ==============================
if "auth" not in st.session_state:
    st.session_state.auth = False
# if "auth" not in st.session_state:
    # st.session_state.auth = False    
    
if "user" not in st.session_state:
    st.session_state.user = None
 # if "user" not in st.session_state:
    # st.session_state.user = None   
    
if "rol" not in st.session_state:
    st.session_state.rol = None
# if "rol" not in st.session_state:
    # st.session_state.rol = None    
    
if "auth_step" not in st.session_state:
    st.session_state.auth_step = "login"
 # if "auth_step" not in st.session_state:
    # st.session_state.auth_step = "login"   
    
if "auth" not in st.session_state:
    st.session_state.auth = True
    st.session_state.user = "admin"  

if st.session_state.auth:
    render_sales(st.session_state.user)    
    
st.write("Ejecute todo en app.py")















# 




