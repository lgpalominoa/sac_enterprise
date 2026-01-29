import os
import streamlit as st

# Base de datos
DB_NAME = os.getenv("DB_NAME", "sac_enterprise.db")

# Seguridad
SESSION_TIMEOUT_MIN = 30
OTP_EXPIRATION_MIN = 5

# Twilio (desde st.secrets o env)
TWILIO_ACCOUNT_SID = st.secrets.get("TWILIO_ACCOUNT_SID", "")
TWILIO_AUTH_TOKEN = st.secrets.get("TWILIO_AUTH_TOKEN", "")
TWILIO_PHONE_NUMBER = st.secrets.get("TWILIO_PHONE_NUMBER", "")

# Overpass / Nominatim
HTTP_TIMEOUT = 15
USER_AGENT = "SAC-Enterprise-Pro/1.0 (security@empresa.com)"
