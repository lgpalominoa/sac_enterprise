import random
from datetime import datetime, timedelta
from twilio.rest import Client
from config.settings import (
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_PHONE_NUMBER,
    OTP_EXPIRATION_MIN
)
from core.logs import log_event

def generar_otp():
    return str(random.randint(100000, 999999))

def enviar_otp(celular, codigo):
    if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN]):
        return False

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        body=f"SAC Enterprise - Código de acceso: {codigo}",
        from_=TWILIO_PHONE_NUMBER,
        to=celular
    )
    return True

def iniciar_2fa(user, celular):
    otp = generar_otp()
    enviado = enviar_otp(celular, otp)

    if enviado:
        log_event(user, "OTP_SENT", f"Enviado a {celular}")

    return {
        "otp": otp,
        "expires": datetime.now() + timedelta(minutes=OTP_EXPIRATION_MIN)
    }

def validar_otp(input_otp, otp_data, user):
    if datetime.now() > otp_data["expires"]:
        log_event(user, "OTP_FAIL", "OTP expirado")
        return False

    if input_otp == otp_data["otp"]:
        log_event(user, "LOGIN_2FA", "Acceso exitoso")
        return True

    log_event(user, "OTP_FAIL", "OTP incorrecto")
    return False
