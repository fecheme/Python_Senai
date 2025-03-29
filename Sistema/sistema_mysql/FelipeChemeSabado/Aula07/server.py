from flask import Flask, jsonify, request, render_template

# criando aplicaçao em flask
app =   Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# GET -> Buscar algo 

@app.route('/helloworld', methods=['GET'])
def helloworld():
    return jsonify({
        "msg": "Ola mundo como estao voces"
    })

# Lista de tarefas
tarefas = [
    { "id": 1, "titulo": "Estudar Python", "feito": False },
    { "id": 2, "titulo": "Ler a doc", "feito": True}
]


@app.route('/tarefas', methods=['GET'])
def get_tarefas():
    return jsonify(tarefas)


# POST -  Criar uma nova tarefa
"""
JavaScript (Front) -> fetch
ReactJS (front) -> axios
Insomnia (aplicativo) -> simular um Front
Postman (Aplicativo) -> Simular um Front

Back-end -> Modelo de API -> FULL REST
Full-stack -> Arquiterura MVC (MODEL, VIEL, CONTROLLER)

"""
@app.route('/tarefas', mothods=['POST'])
def add_tarefa():
    nova_tarefa = request.json # pegar a informaçao do body
    nova_tarefa = ['id'] = len(tarefas) + 1 # adicionando novo id
    tarefas.append(nova_tarefa) # adicionando nova tarefa na lista
    return jsonify(nova_tarefa), 201 # 201 -> created -> criando com sucesso

# Iniciar servidor 

if __name__ == '__main__':
    app.run(debug=True)
 
# http://localhost:5000/helloworld/tarefas 