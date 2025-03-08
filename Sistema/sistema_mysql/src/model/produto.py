import mysql.connector
from config import Config

class ProdutoModel:
    
    def __init__(self):
        # Iniciando configuração
        self.config = Config()

        self.connection = mysql.connector.connect(
            host=self.config.MYSQL_HOST,
            user=self.config.MYSQL_USER,
            password=self.config.MYSQL_PASSWORD,
            database=self.config.MYSQL_DB
        )

        # Faz o cursor trazer o resultado em dicionários
        self.cursor = self.connection.cursor(dictionary=True)
    
    def get_all_products(self): 
        """ Retornar a lista de todos os produtos """
        query = "SELECT id, nome, preco FROM produtos"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def insert_product(self, nome, preco): 
        """ Inserir um produto na tabela produtos """
        query = "INSERT INTO produtos (nome, preco) VALUES (%s, %s)"
        self.cursor.execute(query, (nome, preco))
        self.connection.commit() # confirma a transação
        return self.cursor.lastrowid
    
    def get_product_by_id(self, product_id): 
        """Buscar o produto pelo ID """
        query = "SELECT id, nome, preco FROM produtos WHERE id = %s"
        self.cursor.execute(query, (product_id,))
        return self.cursor.fetchone()

    def delete_product_by_id(self, product_id): 
        """Deletar um produto pelo id """
        query = "DELETE FROM produtos WHERE id = %s"
        self.cursor.execute(query, (product_id,))
        self.connection.commit()
        return self.cursor.rowcount
    
    def update_product_by_id(self, product_id, nome, preco): 
        """Atualizar um produto pelo id """
        query = "UPDATE produtos SET nome = %s, preco = %s WHERE id = %s"
        self.cursor.execute(query, (nome, preco, product_id))
        self.connection.commit()
        return self.cursor.rowcount
    
    def close_connection(self): 
        self.cursor.close()
        self.connection.close()

produto_model = ProdutoModel()

# Chamar o método correto para obter todos os produtos
produtos = produto_model.get_all_products() 

# Você pode imprimir ou usar a lista de produtos retornada pelo método
print(produtos)
