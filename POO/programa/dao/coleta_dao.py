from dao.base_dao import BaseDAO
from models.coleta import Coleta
from datetime import datetime

class ColetaDAO(BaseDAO):

    @staticmethod
    def inserir(obj):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO coleta (data, confirmado, descricao, pontos) VALUES (?, ?, ?, ?)",
            (obj.data.isoformat(), int(obj.confirmado), obj.descricao, obj.pontos)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def listar():
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM coleta")
        dados = cursor.fetchall()
        conn.close()

        lista = []
        for d in dados:
            coleta = Coleta(d[0], datetime.fromisoformat(d[1]), d[3], d[4])
            coleta.confirmado = bool(d[2])
            lista.append(coleta)
        return lista
