from datetime import datetime

class Recompensa:
    def __init__(self, id, nome, descricao, pontosNecessarios, tipoRecompensa, validade):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.pontosNecessarios = pontosNecessarios
        self.tipoRecompensa = tipoRecompensa
        self.validade = validade

    def __str__(self):
        return self.nome
