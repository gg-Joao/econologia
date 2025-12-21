import sqlite3

class Database:
    @staticmethod
    def conectar():
        return sqlite3.connect("sistema.db", check_same_thread=False)

    @staticmethod
    def criar_tabelas():
        conn = Database.conectar()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS admin (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT UNIQUE,
            senha TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS morador (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            fone TEXT,
            pontos INTEGER,
            senha TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS coleta (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            confirmado INTEGER,
            descricao TEXT,
            pontos INTEGER
        )
        """)

        conn.commit()
        conn.close()
