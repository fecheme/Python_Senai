
# definiçao da classe Pessoa

class pessoa:
    

    # metodo construtor 
    # é chamado quando criamos um objeto 
    def __init__(self, nome, idade, altura):
        # atribuir a entidade 
        self.nome = nome  
        self.idade = idade
        self.altura = altura

    def apresentar (self):
        print(f' ola meu nome é {self.nome} e tenho {self.idade} anos, tenho {self.altura} de altura')    



p1 = pessoa("Felipe", 34, "1.80")
p2 = pessoa("Rafael", 7, "1.20")
p3 = pessoa("Paulo", 27, "1.67")

p1.apresentar()
p2.apresentar()
p3.apresentar()

