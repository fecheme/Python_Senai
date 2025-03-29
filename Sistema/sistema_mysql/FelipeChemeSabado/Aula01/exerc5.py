
print("me diga um numero")
n1 = int(input())

print("me diga outro numero")
n2 = int(input())

for y in range(n1, n2 + 1): 
    if y % 2 == 0:
        print("o Numero é par:", y)
