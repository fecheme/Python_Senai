import mysql.connector
from config import Config

class UsuarioModel:
    
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
    
    def get_all_users(self): 
        query = "SELECT id, nome, idade, email FROM usuarios"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def insert_user(self, nome, idade, email):    
        query = "INSERT INTO usuarios (nome, idade, email) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (nome, idade, email))
        self.connection.commit() # confirma a transação
        return self.cursor.lastrowid
    
    def get_user_by_id(self, user_id): 
        query = "SELECT id, nome, idade, email FROM usuarios WHERE id = %s"
        self.cursor.execute(query, (user_id,))
        return self.cursor.fetchone()

    def get_user_by_email(self, email):
        query = "SELECT id, nome, idade, email FROM usuarios WHERE email = %s"
        self.cursor.execute(query, (email,))
        return self.cursor.fetchone()
    
    def delete_user_by_id(self, user_id): 
        query = "DELETE FROM usuarios WHERE id = %s"
        self.cursor.execute(query, (user_id,))
        self.connection.commit()
        return self.cursor.rowcount
    
    def update_user_by_id(self, user_id, nome, idade, email): 
        query = "UPDATE usuarios SET nome = %s, idade = %s, email = %s WHERE id = %s"
        self.cursor.execute(query, (nome, idade, email, user_id))
        self.connection.commit()
        return self.cursor.rowcount
    
    def close_connection(self): 
        self.cursor.close()
        self.connection.close()

usuario_model = UsuarioModel()

# Chamar o método correto para obter todos os usuários
usuarios = usuario_model.get_all_users() 

# Você pode imprimir ou usar a lista de usuários retornada pelo método
print(usuarios)
