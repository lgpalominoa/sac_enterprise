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
    
# ==============================
# ORQUESTADOR PRINCIPAL
# ==============================

# 1️⃣ NO autenticado → LOGIN
if not st.session_state.auth:

    # Paso 1: Login usuario/clave
    if st.session_state.auth_step == "login":
        ok = login()
        
        if ok:
            st.session_state.auth = True
            # st.session_state.auth_step = "2fa"
            # st.rerun()

    # Paso 2: 2FA
    # elif st.session_state.auth_step == "2fa":
        # st.subheader("🔐 Verificación de seguridad")

        # codigo = st.text_input("Código de verificación", type="password")

        # if st.button("Verificar código"):
            # if validar_otp(codigo, st.session_state.otp_data, st.session_state.user):
                # st.session_state.auth = True
                # st.session_state.auth_step = "app"
                # st.rerun()
            # else:
                # st.error("Código inválido o expirado")

# 2️⃣ AUTENTICADO → APP
else:
    st.sidebar.success(f"Sesión activa: {st.session_state.user}")

    if st.sidebar.button("🚪 Cerrar sesión"):
        st.session_state.auth = False
        st.session_state.auth_step = "login"
        st.session_state.user = None
        st.session_state.otp_data = None
        st.rerun()

if st.session_state.auth:
    render_sales(st.session_state.user)    
















# 




