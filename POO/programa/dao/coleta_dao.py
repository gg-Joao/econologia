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
            (obj.get_data().isoformat(), int(obj.get_confirmado()), obj.get_desc(), obj.get_pontos())
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
            coleta = Coleta(d[0], datetime.fromisoformat(d[1]), bool(d[2]), d[3], d[4])
            lista.append(coleta)
        return lista
