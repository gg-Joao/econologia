from dao.base_dao import BaseDAO
from models.morador import Morador

class MoradorDAO:

    @staticmethod
    def inserir(obj):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO morador (nome, email, fone, pontos, senha)
            VALUES (?, ?, ?, ?, ?)
        """, (obj.get_nome(), obj.get_email(), obj.get_fone(), obj.get_pontos(), obj.get_senha()))
        conn.commit()
        conn.close()
    
    @staticmethod
    def login(email, senha):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM morador WHERE email=? AND senha=?
        """, (email, senha))
        dado = cursor.fetchone()
        conn.close()

        if dado:
            return Morador(dado[0], dado[1], dado[2], dado[3])
        return None


    @staticmethod
    def listar():
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM morador")
        dados = cursor.fetchall()
        conn.close()

        lista = []
        for d in dados:
            lista.append(Morador(d[1], d[2], d[3], d[4], d[5]))
        return lista
