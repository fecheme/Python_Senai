
"""
def verificaIdade(idade):
    if idade >= 18:
        return "pode ver o filme"
    else:
        return "nao pode ver o filme"

print("Digite sua idade")
idade = int(input())

resultado = verificaIdade(idade)

print(resultado)
"""

def menu():
    print("menu da calculadora")
    print("1 - somar")
    print("2 - subtrair")
    print("9 - sair")

def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 + n2

def verificaOpcao (opcao):
    if opcao == 1:
        num1 = float(input("Digite o numero 1 "))
        num2 = float(input("Digite o numero 2 "))
        print(somar(num1, num2))
    elif opcao == 2:
        num1 = float(input("Digite o numero 1 "))
        num2 = float(input("Digite o numero 2 "))
        print(subtrair(num1, num2))
    elif opcao == 9:
        print("fim")
     
        
def calculadora():
    while True:
        menu()
        opcao = int(input("escolha um opcao"))
        verificaOpcao(opcao)

calculadora()

