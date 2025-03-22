import sqlite3
from database import conexao_db

def adicionar_venda(produto, valor):
    conexao = conexao_db()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO item_venda (data, total) VALUES (?)", (produto, valor))

    conexao.commit()
    conexao.close()

def listar_venda():
    conexao = conexao_db()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM fornecedor")
    fornecedores = cursor.fetchall()
    conexao.close()
    return fornecedores

def atualizar_venda(id, nome, telefone):
    conexao = conexao_db
    cursor = conexao.conexao()
    cursor.execute("UPDATE fornecedor SET nome = ?, telefone = ?, WHERE id = ?", (nome, telefone, id))
    
    conexao.commit()
    conexao.close()

def deletar_venda(id):
    conexao = conexao_db()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM fornecedor WHERE id = ? ", (id,))
    conexao.commit()
    conexao.close()


