import sqlite3
from estoque.database import conexao_db


def adicionar_fornecedor(nome, telefone):
    conexao = conexao_db()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO fornecedor (nome, telefone) VALUES (?, ?)", (nome, telefone))

    conexao.commit()
    conexao.close()

def listar_fornecedores():
    conexao = conexao_db()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM fornecedor")
    fornecedores = cursor.fetchall()

    conexao.close()
    return fornecedores

def atualizar_fornecedor(id, nome, telefone):
    conexao = conexao_db
    cursor = conexao.conexao()
    cursor.execute("UPDATE fornecedor SET nome = ?, telefone = ?, WHERE id = ?", (nome, telefone, id))
    
    conexao.commit()
    conexao.close()


def deletar_fornecedor(id):
    conexao = conexao_db()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM fornecedor WHERE id = ? ", (id,))

    conexao.commit()
    conexao.close()
