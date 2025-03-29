
""" 
desenvolver um sistema que recebe valor de A, valor de B e valor de C

calcular a Bhaskara
Delta = b² - 4 * a * c

"""

print ("calculador de bhaskara")

print ("digite o valor de A")
A = float(input())

print("digite o valor de B")
B = float(input())

print("digite o valor de C")
C = float(input())

Delta = (B ** 2) - 4 * A * C
print ("delta = ", Delta)

if A == 0:
    print("O valor de a, deve ser diferente de 0")
elif Delta < 0:
    print("Sem raízes reais")
else:
    Bhaskarax1 = (-B + Delta ** (1 / 2)) / (2 * A)
    Bhaskarax2 = (-B - Delta ** (1 / 2)) / (2 * A)

    print("x1 = ", Bhaskarax1, "x2 =", Bhaskarax2)


