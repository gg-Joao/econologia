from database import Database
from models.morador import Morador
from dao.morador_dao import MoradorDAO

Database.criar_tabelas()

m = Morador("Teste", "teste@email.com", "1111", senha="123")
MoradorDAO.inserir(m)

lista = MoradorDAO.listar()
for item in lista:
    print(item)
