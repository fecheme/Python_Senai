
from ..models.produto import produto
from ..database.database import BancoFake

class produtoController:

    def __init__(self):
        self.db = BancoFake()

    def criar_produto(self, nome, preco):
        novo_produto = produto(nome, preco)
        dict_produto = {
            "nome": novo_produto.nome,
            "preco": novo_produto.preco 
        }

        self.db.adicionar_Produto(dict_produto)
        print("Produto cadastrado com sucesso!")

    def listar_Produto(self):
        # retorna uma lista com todos os clientes
        return self.db.listar_Produtos()
 
        
    