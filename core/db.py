import sqlite3
import hashlib
from datetime import datetime
from core.logs import registrar_log
#from contextlib import contextmanager

DB_NAME = "sac_enterprise.db"

#@contextmanager
def init_db():
    get_db()
    ejecutar_query("DROP TABLE trazabilidad", '' , commit=True)
    ejecutar_query("DROP TABLE usuarios", '' , commit=True)
    ejecutar_query('''CREATE TABLE IF NOT EXISTS usuarios 
                     (user TEXT PRIMARY KEY, password TEXT, rol TEXT, 
                      estado INTEGER DEFAULT 1, email TEXT, celular TEXT)''', commit=True)
    ejecutar_query('''CREATE TABLE IF NOT EXISTS trazabilidad 
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, fecha TEXT, usuario TEXT, accion TEXT, detalle TEXT)''', commit=True)
    
    password = 'admin123'
    admin_pw = hashlib.sha256(password.encode()).hexdigest()
    #admin_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()) 
    ejecutar_query("INSERT OR IGNORE INTO usuarios VALUES (?,?,?,?,?,?)", 
                  ('admin', admin_pw, 'Administrador', 1, 'admin@tuempresa.com', 'PENDIENTE'), commit=True)  

def get_db():
    conn = sqlite3.connect(DB_NAME)
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()
        
def ejecutar_query(query, params=(), commit=False):
    conn = sqlite3.connect(DB_NAME)
    try:
        cursor = conn.cursor()
        cursor = conn.execute(query, params)
        if commit: conn.commit()
        result = cursor.fetchall()
        conn.close()
        return result
    except Exception as e:
        registrar_log("Sistema", "ERROR_DB", str(e))
        return None

               
