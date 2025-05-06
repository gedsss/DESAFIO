from livraria import conectar, inserir, ler, update, delete

def exibir_menu():
    print("\nMenu:")
    print("1. Inserir livro")
    print("2. Listar livros")
    print("3. Atualizar autor de um livro")
    print("4. Deletar livro")
    print("5. Sair")

def menu():
    conexao = conectar()
    cursor = conexao.cursor()

    while True:
        exibir_menu()
        escolha = int(input("Escolha uma das opções: "))

        if escolha == 1:
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano_publicacao = int(input("Digite o ano de publicação: "))
            preco = float(input("Digite o preço do livro: "))
            inserir(cursor, conexao, titulo, autor, ano_publicacao, preco)

        elif escolha == 2:
            livros = ler(cursor)
            for livro in livros:
                print(livro)

        elif escolha == 3:
            id_livro = int(input("Digite o ID do livro a atualizar: "))
            novo_autor = input("Digite o novo autor: ")
            update(cursor, conexao, novo_autor, id_livro)

        elif escolha == 4:
            id_livro = int(input("Digite o ID do livro a excluir: "))
            delete(cursor, conexao, id_livro)

        elif escolha == 5:
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")

    cursor.close()
    conexao.close()

if __name__ == "__main__":
    menu()

