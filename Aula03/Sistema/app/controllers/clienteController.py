
from ..models.cliente import cliente
from ..database.database import BancoFake

class clienteController:

    def __init__(self):
        # Conexao com o banco
        self.db = BancoFake()      

    def criar_cliente(self, nome, email, idade):
        # cria objeto cleinte e salva no banco
        novo_cliente = cliente(nome, email, idade)
        # converter para dict (JSON)
        dict_cliente = {
            "nome": novo_cliente.nome,
            "email": novo_cliente.email,
            "idade": novo_cliente.idade
        }

    # salvar no banco 
        self.db.adicionar_cliente(dict_cliente)
        print("Cliente cadastrado com sucesso!")

    def listar_clientes(self):
        # retorna uma lista com todos os clientes
        return self.db.listar_clientes()

