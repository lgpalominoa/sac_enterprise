from datetime import datetime
import sqlite3

DB_NAME = "sac_enterprise.db"
        
def get_db():
    conn = sqlite3.connect(DB_NAME)
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()
        
def ejecutar_query(query, params=(), commit=False):
    get_db()
    try:
        conn = sqlite3.connect(DB_NAME, check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute(query, params)
        if commit: conn.commit()
        result = cursor.fetchall()
        conn.close()
        return result
    except Exception as e:
        registrar_log("Sistema", "ERROR_DB", str(e))
        return None
        
#@staticmethod
def registrar_log(user, accion, detalle):
    conn = get_db()
    fecha = datetime.now() #.strftime("%Y-%m-%d %H:%M:%S")
    try:
        #cursor = conn.cursor()
        ejecutar_query("INSERT INTO trazabilidad (fecha, usuario, accion, detalle) VALUES (?,?,?,?)",
                      (fecha, user, accion, str(detalle)))
        conn.commit()
        conn.close()
    except: pass        
