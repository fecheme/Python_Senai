

import json # lidas com arquivo JSON
from pathlib import Path #lidar com caminhos do WIN

class BancoFake:
    def __init__(self, arquivo_db="banco.json"):
        self.arquivo_db = arquivo_db
        self.dados = {"clientes": [], "produtos": []}
        self._carregar()

    def _carregar(self):
        #CARREGA DADOS DO ARQUIVO JSON, SE EXISTIR, CASO NAO EXISTA, INICIA COM DADOS VAZIOS
        caminho = Path(self.arquivo_db)
        if caminho.is_file():
            print("passou aqui")
            # abrindo arquivo no modo leitura em UTF-8 (PT-BR)
            with open(caminho, 'r', encoding="utf-8") as data:
                # salvando dados que ja existem no arquivo na variavel de dados 
                self.dados = json.load(data)
        else:
            self._salvar()

    def _salvar(self):
        # salvar o conteudo de self.dados no arquivo JSON
        # abrindo o arquivo no modo W (escrita) 
        with open(self.arquivo_db, 'w', encoding="utf-8") as data:
            # realizando DUMP (python para JSON) para salvar no banco 
            json.dump(self.dados, data, ensure_ascii=False, indent=4)
        
    def adicionar_cliente(self, cliente_dict):
        self.dados["clientes"].append(cliente_dict)
        self._salvar()

    def listar_clientes(self):
        return self.dados["clientes"]
    
    def adicionar_Produto(self, Produto_dict):
        self.dados["produtos"].append(Produto_dict)
        self._salvar()

    def listar_Produtos(self):
        return self.dados["produtos"]
    