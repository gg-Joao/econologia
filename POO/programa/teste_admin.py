from database import Database
from dao.admin_dao import AdminDAO
from models.admin import Admin

Database.criar_tabelas()

admin = Admin(
    nome="Admin",
    email="admin@email.com",
    senha="123"
)

AdminDAO.inserir(admin)
print("Admin criado com sucesso!")
