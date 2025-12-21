import streamlit as st
from database import Database
from dao.admin_dao import AdminDAO
from models.admin import Admin
from models.morador import Morador
from dao.morador_dao import MoradorDAO

Database.criar_tabelas()


if "admin" not in st.session_state:
    st.session_state.admin = None

if "morador" not in st.session_state:
    st.session_state.morador = None


st.title("♻️ Sistema de Coleta Seletiva")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Login Morador",
        "Cadastro Morador",
        "Login Admin",
        "Painel Admin"
    ]
)


if menu == "Login Morador":
    st.header("Login do Morador")

    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        morador = MoradorDAO.login(email, senha)
        if morador:
            st.session_state.morador = morador
            st.success(f"Bem-vindo")
        else:
            st.error("Email ou senha inválidos")

if menu == "Cadastro Morador":
    st.header("Cadastro de Morador")

    nome = st.text_input("Nome")
    email = st.text_input("Email")
    fone = st.text_input("Telefone")
    senha = st.text_input("Senha", type="password")

    if st.button("Cadastrar"):
        morador = Morador(nome, email, fone, senha=senha)
        MoradorDAO.inserir(morador)
        st.success("Morador cadastrado com sucesso!")



if menu == "Login Admin":
    st.header("Login do Administrador")

    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        admin = AdminDAO.login(email, senha)
        if admin:
            st.session_state.admin = admin
            st.success(f"Bem-vindo, {admin.nome}")
        else:
            st.error("Email ou senha inválidos")

elif menu == "Painel Admin":

    if not st.session_state.admin:
        st.warning("Faça login como administrador.")
    else:
        st.header("Painel Administrativo")

        st.write(f" Logado como: **{st.session_state.admin.nome}**")

        admins = AdminDAO.listar()
        st.subheader("Administradores cadastrados")

        for a in admins:
            st.write(a)
