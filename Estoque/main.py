from views.menu import exibir_menu_opcoes, exibir_menu_fornecedor, exibir_menu_produtos
from estoque.database import create_tables




if __name__ == '__main__':
    create_tables()
    exibir_menu_opcoes(exibir_menu_fornecedor, exibir_menu_produtos)