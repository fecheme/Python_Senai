

palavra = input("qual a palavra").lower().replace(" " , "")
print()
palindromo = palavra == palavra[::-1]

if palindromo:
    print(f"a palavra '{palavra}' é um palindromo") 
else:
    print(f"a palavra '{palavra}' nao é um palindromo") 