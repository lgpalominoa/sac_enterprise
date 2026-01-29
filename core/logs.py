from datetime import datetime
from core.db import get_db

def log_event(user, action, detail):
    with get_db() as db:
        db.execute(
            "INSERT INTO trazabilidad (fecha, usuario, accion, detalle) VALUES (?,?,?,?)",
            (datetime.now(), user, action, detail)
        )
