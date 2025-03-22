import os 
import sqlite3 

def conexao_db():
    caminho_db = os.path.join(os.path.dirname(__file__), 'estoque.db')
    conexao = sqlite3.connect(caminho_db) 
    return conexao

def create_tables():

    conexao = conexao_db()
    cursor = conexao.cursor()
    cursor.execute ('''
        CREATE TABLE IF NOT EXISTS produto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL)''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS fornecedor (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT)''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS  venda (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            total REAL NOT NULL)''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS  item_venda (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            venda_id INTEGER,
            produto_id INTEGER,
            quantidade INTEGER,
            FOREIGN KEY (venda_id) REFERENCES venda(id) ON DELETE CASCADE,
            FOREIGN KEY (produto_id) REFERENCES produto(id)) ON DELETE CASCADE ''')
    
    conexao.commit()
    conexao.close()
    
    
    

if __name__ == '__main__':
    create_tables()
