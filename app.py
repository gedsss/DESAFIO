import streamlit as st
from livraria import conectar, inserir, ler, update, delete

st.set_page_config(page_title="Livraria", layout="centered")

st.title("Sistema de Gerenciamento de Livros")

conexao = conectar()
cursor = conexao.cursor()

menu = st.sidebar.selectbox("Menu", ["Inserir", "Listar", "Atualizar", "Deletar"])

if menu == "Inserir":
    st.subheader("Adicionar Novo Livro")
    titulo = st.text_input("Título")
    autor = st.text_input("Autor")
    ano = st.text_input("Ano de Publicação (opcional)")
    ano = int(ano) if ano.isdigit() else None
    preco = st.number_input("Preço", min_value=0.0, format="%.2f")

    if st.button("Inserir"):
        if titulo and autor and ano and preco:
            inserir(cursor, conexao, titulo, autor, ano, preco)
            st.success("Livro inserido com sucesso!")
        else:
            st.warning("Preencha todos os campos.")

elif menu == "Listar":
    st.subheader("Lista de Livros")
    livros = ler(cursor)
    if livros:
        for livro in livros:
            st.write(f"ID: {livro[0]} | Título: {livro[1]} | Autor: {livro[2]} | Ano: {livro[3]} | Preço: R$ {livro[4]:.2f}")
    else:
        st.info("Nenhum livro cadastrado.")

elif menu == "Atualizar":
    st.subheader("Atualizar Autor de um Livro")
    id_livro = st.number_input("ID do Livro", min_value=1, step=1)
    novo_autor = st.text_input("Novo Autor")

    if st.button("Atualizar"):
        if novo_autor:
            update(cursor, conexao, novo_autor, id_livro)
            st.success("Autor atualizado com sucesso.")
        else:
            st.warning("Digite o nome do autor.")

elif menu == "Deletar":
    st.subheader("Deletar Livro")
    id_livro = st.number_input("ID do Livro a Deletar", min_value=1, step=1)

    if st.button("Deletar"):
        delete(cursor, conexao, id_livro)
        st.success("Livro deletado com sucesso.")

cursor.close()
conexao.close()
