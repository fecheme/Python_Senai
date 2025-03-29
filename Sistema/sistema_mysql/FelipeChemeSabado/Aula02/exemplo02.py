
"""
sistema de descontos de veiculo solicite o nome do veiculo e o preço do veiculo
se o preço for > 80k -> 60% de desconto
se o preço for > 50k -> 30% de desconto 
se po preço for , 30k -> nao existe desconto 

"""
Modelo = input(" diga o modelo do veiculo ")
print("")

valor = float(input(" Digite o valor do veiculo "))
print("")

if valor >= 80000:
    print(" o valor final do veiculo com desconto é", valor * 0.40)   
    print("")
elif valor >= 50000:
    print(" o valor final do veiculo com desconto é", valor * 0.70)
    print("")
elif valor <= 50000:
    print(" o veiculo nao tem desconto")


