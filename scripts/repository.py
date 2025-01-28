import sqlite3
import pandas as pd

def connect_to_database():
    db_name = "Base_extratos"
    try:
        conn = sqlite3.connect(db_name)
        print(f"Conexão estabelecida com o banco de dados '{db_name}'.")
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def execute(conn, query, params=None):
    try:
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        conn.commit()
        print("Consulta executada com sucesso.")
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Erro ao executar a consulta: {e}")
        return None

def query_to_dataframe(conn, query):
    
    try:
        df = pd.read_sql_query(query, conn)
        print("Consulta convertida para DataFrame com sucesso.")
        return df
    except sqlite3.Error as e:
        print(f"Erro ao executar a consulta para DataFrame: {e}")
        return None

def close_connection(conn):
    try:
        conn.close()
        print("Conexão com o banco de dados fechada.")
    except sqlite3.Error as e:
        print(f"Erro ao fechar a conexão: {e}")
