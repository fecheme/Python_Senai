from ..model.usuario import UsuarioModel

def listar_usuarios():
    usuario_model = UsuarioModel()
    usuarios = usuario_model.get_all_users()
    return usuarios

def cadastrar_usuario(nome, idade, email):
    usuario_model = UsuarioModel()
    
    # Verificar se o email já está cadastrado
    if usuario_model.get_user_by_email(email):
        print("Email já cadastrado. Tente outro email.")
        return None
    
    novo_id = usuario_model.insert_user(nome, idade, email)
    return novo_id

def atualizar_usuario(user_id, nome, idade, email):
    usuario_model = UsuarioModel()
    

    usuario_existente = usuario_model.get_user_by_email(email)
    if usuario_existente and usuario_existente['id'] != user_id:
        print("Email já cadastrado. Tente outro email.")
        return 

    linhas = usuario_model.update_user_by_id(user_id, nome, idade, email)
    return linhas

def deletar_usuario(user_id):
    usuario_model = UsuarioModel()
    linhas = usuario_model.delete_user_by_id(user_id)
    return linhas

def buscar_usuario(user_id):
    usuario_model = UsuarioModel()
    usuario = usuario_model.get_user_by_id(user_id)
    return usuario


def buscar_usuario_por_email(email):
    usuario_model = UsuarioModel()
    usuario = usuario_model.get_user_by_email(email)
    return usuario

