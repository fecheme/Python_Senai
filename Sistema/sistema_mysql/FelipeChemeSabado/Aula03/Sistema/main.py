
from app.controllers.clienteController import clienteController 
from app.controllers.produtocontroller import produtoController 

def exibir_menu():
    print("\n ==== MENU ==== ")
    print("1 - Cadastrar Clientes")
    print("2 - Listar Clientes")
    print("3 - Cadastrar Produtos")
    print("4 - Listar Produtos")
    print("o - Sair do Sistema")

def main():
    cntrClient = clienteController()
    cntrProduto = produtoController()
    while True:
        exibir_menu()
        opc = input("Escolha uma opção: ")

        if opc == "1":
            nome  = input("Nome do Cliente: ")
            email = input("E-mail: ")
            idade = int(input("Idade: "))
            #salvariamos no banco de dados
            cntrClient.criar_cliente(nome, email, idade)

        elif opc == "2":
            # listar nomes dos produtos
            clientes = cntrClient.listar_clientes()

            for index, cliente in enumerate(clientes, 1):
                print(f"{index}. {cliente}")
         
        elif opc == "3":
            nome = input("Nome do Produto: ")
            preco = float(input("Preço: "))
            cntrProduto.criar_produto(nome, preco)

        elif opc == "4":
            produtos = cntrProduto.listar_Produto()

            for index, produto in enumerate(produtos, 1):
                print(f"{index}. {produto}")

        elif opc == "0":
            print("Saindo do sistema.....")
            break


        else:
             print("Opção Invalida. Tente novamente.")

if __name__ == "__main__":
     main()  