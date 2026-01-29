import re

def validar_telefono(numero: str) -> bool:
    return bool(re.match(r"^\+\d{10,15}$", numero))

def limpiar_texto(texto: str) -> str:
    return re.sub(r"[<>\"']", "", texto.strip())

def validar_email(email: str) -> bool:
    return bool(re.match(r"^[^@]+@[^@]+\.[^@]+$", email))
