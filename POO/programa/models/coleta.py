from datetime import datetime

class Coleta:
    def __init__(self, id, data, descricao, pontos):
        self.id = id
        self.data = data
        self.confirmado = False
        self.descricao = descricao
        self.pontos = pontos

    def __str__(self):
        return f"Coleta {self.id} - {self.descricao}"
