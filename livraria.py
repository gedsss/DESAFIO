import mysql.connector

def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='Seu user',
        password='Sua senha',
        database='livraria'
    )

def inserir(cursor, conexao, titulo, autor, ano_publicacao, preco):
    comando = '''INSERT INTO livros (titulo, autor, ano_publicacao, preco) VALUES (%s, %s, %s, %s)'''
    dados = (titulo, autor, ano_publicacao, preco)
    cursor.execute(comando, dados)
    conexao.commit()

def ler(cursor):
    comando = '''SELECT * FROM livros'''
    cursor.execute(comando)
    return cursor.fetchall()

def update(cursor, conexao, novo_autor, id_livro):
    comando = '''UPDATE livros SET autor = %s WHERE id = %s'''
    dados = (novo_autor, id_livro)
    cursor.execute(comando, dados)
    conexao.commit()

def delete(cursor, conexao, id_livro):
    comando = '''DELETE FROM livros WHERE id = %s'''
    cursor.execute(comando, (id_livro,))
    conexao.commit()
