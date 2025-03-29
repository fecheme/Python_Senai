
# Faça a tabuada

#for x in range(10):
  #  print(x)


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    print(f"tabuada do numero, {numero}:" )
    for x in range(1, 11):
        print(f"{numero} x {x} = {numero * x}")
print()





# modo facil 
for x in range (1, 11):
    for y in range(1, 11):
        print(x, "X", y, "=", x * y)    