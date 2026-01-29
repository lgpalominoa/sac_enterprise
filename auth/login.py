import streamlit as st
from core.db import get_db
from core.security import verify_password
from core.logs import log_event

def login():
    st.subheader("🔐 Acceso Seguro")

    user = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Ingresar"):
        with get_db() as db:
            row = db.execute(
                "SELECT password, rol, celular FROM usuarios WHERE user=? AND estado=1",
                (user,)
            ).fetchone()

        if not row:
            st.error("Credenciales inválidas")
            log_event(user, "LOGIN_FAIL", "Usuario no existe")
            return False

        if not verify_password(password, row[0]):
            st.error("Credenciales inválidas")
            log_event(user, "LOGIN_FAIL", "Password incorrecto")
            return False

        st.session_state.user = user
        st.session_state.rol = row[1]
        st.session_state.celular = row[2]
        st.session_state.auth_step = "2fa"

        return True
