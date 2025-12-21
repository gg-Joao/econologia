from models.usuario import Usuario

class Morador(Usuario):
    def __init__(self, nome, email, fone, pontos=0, senha=""):
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_pontos(pontos)
        self.set_senha(senha)

    def __str__(self):
        return f"{self.nome} ({self.pontos} pontos)"
    
    def set_nome(self, nome):
        self.__nome = nome

    def set_pontos(self, pontos):
        self.__pontos = pontos

    def get_nome(self):
        return self.__nome
    
    def get_pontos(self):
        return self.__pontos