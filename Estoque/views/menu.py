from controllers.produto_ctrl import adicionar_produto, listar_produtos, atualizar_produtos, deletar_produto


def exibir_menu():
    while True:

        print("\n--- Sistema de Gerenciamento de Estoque")
        print("1. Cadastrar Produto")
        print("2. Listar Produto")
        print("3. Atualizar Produto")
        print("4. Deletar Produto")
        print("5. Sair")
        opcao = input("Escolha um opção: ")

        if opcao == '1':
            nome = input("Nome do Produto:")
            preco = float(input("Preço do Produto: "))
            quantidade = int(input("Quantidade do Produtos: "))
            adicionar_produto(nome, preco, quantidade)
            print("Produto cadastrado com sucesso!")

        elif opcao == '2':
            produtos = listar_produtos()
            print("\n Produtos em Estoque: ")
            for produtos in produtos:
                print(f"ID: {produtos[0]} | Nome: {produtos[1]} | Preço: {produtos[2]} | Quantidade: {produtos[3]}")
            

        elif opcao == '3':
            id = int(input("ID do Produto a ser atualizado: "))
            nome = input("Novo Nome do Produto: ")
            preco = float(input("Novo Preço do Produto: "))
            quantidade = int(input("Nova Quantidade do Produto: "))
            atualizar_produtos(id, nome, preco, quantidade)
            print("Produto atualizado com sucesso!")


        elif opcao == '4':
            id = int(input("ID do Produto a ser deletado: "))
            deletar_produto(id)
            print("Produto deletado com sucesso!")

        elif opcao == '5': 
            print("Finalizando...")
            break 
        else: 
            print("Opção inválida! Tente novamente")


if __name__ == '__main__':
    exibir_menu()

