

print("digite seu peso")
n1 = float(input())

print("digite sua altura")
n2 = float(input())

IMC = n1 / (n2 * n2)
print (IMC)


if IMC < 18.5:
    print("abaixo do peso")
elif IMC >= 18.6 < 24.9:
    print ("peso normal")
elif IMC >=25 < 29.9:
    print ("sobre peso")
elif IMC > 30:
    print("obesidade")