import streamlit as st
import hashlib
from core.db import get_db, ejecutar_query
from core.security import verify_password
from core.logs import registrar_log
from auth.twofa import iniciar_2fa

def login():
    st.subheader("🔐 Acceso Corporativo")

    usuario = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    password = hashlib.sha256(password.encode()).hexdigest()

    if st.button("Ingresar"):
        query = "SELECT password, rol, celular FROM usuarios WHERE user='"+usuario+"' AND estado=1"
        row = ejecutar_query(query, "", commit=True) 
 
        if not row:
            st.error("Usuario no existe")
            registrar_log(usuario, "LOGIN_FAIL", "Usuario no existe")
            return False
            
        password_bd = row[0][0]
                  
        if password != password_bd:
        #if not verify_password(password, row[0]):
            st.error("Credenciales inválidas")
            registrar_log(usuario, "LOGIN_FAIL", "Password incorrecto")
            return False

        # Credenciales OK
        st.session_state.user = usuario
        st.session_state.rol = row[0][1]

        # Iniciar 2FA
        #st.session_state.otp_data = iniciar_2fa(usuario, row[0][2])

        registrar_log(usuario, "LOGIN_OK", "Credenciales válidas")
        return True

