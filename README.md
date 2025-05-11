Este projeto é um sistema simples de cadastro e gerenciamento de livros, desenvolvido em **Python** com persistência de dados em **MySQL**. O código está organizado em dois arquivos principais: um para a lógica do banco de dados (`banco.py`) e outro para a interface de menu no terminal (`main.py`).

É necessário a instalação do (`mysql.connector`), e tambem é preciso inserir o user e a senha do seu sql no arquivo (`livraria.py`), o local para digitar está entre as linhas 4 e 9.

Para a utilização da interface é necessário a instalação do (`streamlit mysql-connector-python`) e para rodar o mesmo basta dar um **streamlit run app.py** no terminal

O Projeto possui as funções de: 
- Inserir novo livro (título, autor, ano e preço)
- Listar todos os livros cadastrados
- Atualizar o autor de um livro existente
- Deletar um livro por ID
- Encerrar o programa

