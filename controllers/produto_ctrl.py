import sqlite3
from estoque.database import conexao_db

def adicionar_produto(nome, preco, quantidade):
    conexao = conexao_db()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO produto (nome, preco, quantidade) VALUES (?, ?, ?)", (nome, preco, quantidade))
    conexao.commit()
    conexao.close()

def listar_produtos():
    conexao = conexao_db()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produto")
    produtos = cursor.fetchall()
    conexao.close()

    return produtos

def atualizar_produtos(id, nome, preco, quantidade):
    conexao = conexao_db
    cursor = conexao.conexao()
    cursor.execute("UPDATE produto SET nome = ?, preco = ?, quantidade = ?, WHERE id = ?", (nome, preco, quantidade, id))
    
    conexao.commit()
    conexao.close()

def deletar_produto(id):
    conexao = conexao_db()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM produto WHERE id = ? ", (id,))

    conexao.commit()
    conexao.close()
