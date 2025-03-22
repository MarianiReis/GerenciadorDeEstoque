import sqlite3
from database import conexao_db

def adicionar_venda(data, total, produto_id, quantidade):
    conexao = conexao_db()
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO venda (data, total) VALUES (?,?)", (data, total))
    
    venda_id = cursor.lastrowid

    cursor.execute("INSERT INTO item_venda (venda_id, produto_id, quantidade) VALUES (?,?,?)", (venda_id, produto_id, quantidade))

    conexao.commit()
    conexao.close() 


def listar_venda():

    conexao = conexao_db()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT item_venda.id, venda.data, venda.total, item_venda.produto_id, item_venda.quantidade 
        FROM item_venda
        JOIN venda ON item_venda.venda_id = venda.id
    """)
    vendas = cursor.fetchall()
    conexao.close()
    
    return vendas


def deletar_venda(id):

    conexao = conexao_db()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM venda WHERE id = ? ", (id,))
    conexao.commit()
    conexao.close()


