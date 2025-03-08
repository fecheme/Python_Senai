from src.controller import produto_controller
from src.controller import usuario_controller

def exibir_menu(): 
    print("\nMAREA TOCA TUDO LTDA!")
    print("\n==== MENU =====")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Atualizar Produto")
    print("4 - Deletar Produto")
    print("5 - Buscar Produto Único")
    print("6 - Cadastrar Usuário")
    print("7 - Listar Usuários")
    print("8 - Atualizar Usuário")
    print("9 - Deletar Usuário")
    print("10 - Buscar Usuário Único")
    print("0 - Sair")

def listar_produtos(): 
    print("\n--- Lista de Produtos ---")
    produtos = produto_controller.listar_produtos()
    if produtos: 
        for produto in produtos: 
            print(f"ID {produto['id']}, Nome: {produto['nome']}, Preço: {produto['preco']}")
    else: 
        print("Não existem produtos cadastrados")

def cadastrar_produto(): 
    print("\n--- Cadastrar Produto ---")
    nome = input("Digite o nome: ")
    preco = input("Digite o preço: ")
    novo_id = produto_controller.cadastrar_produto(nome, preco)
    print(f"Produto cadastrado com sucesso com o novo ID {novo_id}.")

def atualizar_produto():
    print("\nATUALIZANDO O PRODUTO")
    produto_id = input("Digite o ID do produto: ")
    nome = input("Digite o nome do produto: ")
    preco = input("Digite o preço do produto: ")
    linhas = produto_controller.atualizar_produto(produto_id, nome, preco)
    if linhas > 0:
        print("Produto atualizado com sucesso!")
    else:
        print("Nenhum produto foi atualizado")

def deletar_produto():
    print("\nDELETANDO O PRODUTO")
    produto_id = input("Digite o ID do produto: ")
    linhas = produto_controller.deletar_produto(produto_id)
    if linhas > 0:
        print("Produto deletado com sucesso!")
    else:
        print("Nenhum produto foi deletado")

def buscar_produto():
    print("\nBUSCANDO PRODUTO")
    produto_id = input("Digite o ID do produto: ")
    produto = produto_controller.buscar_produto(produto_id)
    if produto:
        print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preço: {produto['preco']}")
    else:
        print("Produto não encontrado")

def listar_usuarios(): 
    print("\n--- Lista de Usuários ---")
    usuarios = usuario_controller.listar_usuarios()
    if usuarios: 
        for usuario in usuarios: 
            print(f"ID: {usuario['id']}, Nome: {usuario['nome']}, Idade: {usuario['idade']}, Email: {usuario['email']}")
    else: 
        print("Não existem usuários cadastrados")

def cadastrar_usuario(): 
    print("\n--- Cadastrar Usuário ---")
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    email = input("Digite o email: ")

    # Verificar se o email já está cadastrado
    if usuario_controller.buscar_usuario_por_email(email):
        print("Email já cadastrado. Tente outro email.")
    else:
        novo_id = usuario_controller.cadastrar_usuario(nome, idade, email)
        if novo_id:
            print(f"Usuário cadastrado com sucesso com o novo ID {novo_id}.")
        else:
            print("Falha ao cadastrar o usuário. Verifique os dados e tente novamente.")

def atualizar_usuario():
    print("\nATUALIZANDO O USUÁRIO")
    usuario_id = input("Digite o ID do usuário: ")
    nome = input("Digite o nome do usuário: ")
    idade = input("Digite a idade do usuário: ")
    email = input("Digite o email do usuário: ")

    # Verificar se o email já está cadastrado (excluindo o usuário atual)
    usuario_existente = usuario_controller.buscar_usuario_por_email(email)
    if usuario_existente and usuario_existente['id'] != usuario_id:
        print("Email já cadastrado. Tente outro email.")
    else:
        linhas = usuario_controller.atualizar_usuario(usuario_id, nome, idade, email)
        if linhas > 0:
            print("Usuário atualizado com sucesso!")
        else:
            print("Nenhum usuário foi atualizado")

def deletar_usuario():
    print("\nDELETANDO O USUÁRIO")
    usuario_id = input("Digite o ID do usuário: ")
    linhas = usuario_controller.deletar_usuario(usuario_id)
    if linhas > 0:
        print("Usuário deletado com sucesso!")
    else:
        print("Nenhum usuário foi deletado")

def buscar_usuario():
    print("\nBUSCANDO USUÁRIO")
    usuario_id = input("Digite o ID do usuário: ")
    usuario = usuario_controller.buscar_usuario(usuario_id)
    if usuario:
        print(f"ID: {usuario['id']}, Nome: {usuario['nome']}, Idade: {usuario['idade']}, Email: {usuario['email']}")
    else:
        print("Usuário não encontrado")

def main():
    while True:
        exibir_menu()
        opc = input("Escolha uma opção: ")

        if opc == "1":
            cadastrar_produto()
        elif opc == "2":
            listar_produtos()
        elif opc == "3":
            atualizar_produto()
        elif opc == "4":
            deletar_produto()
        elif opc == "5":
            buscar_produto()
        elif opc == "6":
            cadastrar_usuario()
        elif opc == "7":
            listar_usuarios()
        elif opc == "8":
            atualizar_usuario()
        elif opc == "9":
            deletar_usuario()
        elif opc == "10":
            buscar_usuario()
        elif opc == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida")

if __name__ == '__main__':
    main()
