import csv
# criar e escrever um arquivo txt

with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Nome, Idade, Cidade\n")
    arquivo.write("Alberto, 92, Chique-Chique/BA\n")
    arquivo.write("Arthur, 28, Arraial/RJ\n")
    arquivo.write("Matheus, 24, Cotia/SP\n")

# ler o conteudo 
# r -> Read 
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    print("Conteudo do Arquivo txt:")
    print(arquivo.read())

    # crianda arquivo csv

dados = [
        ["Nome", "Idade", "Cidade"],
        ["Carlos", "32", "Santa Isabel"],
        ["Tulio", "18", "Carapicuiba"],
        ["Rafael", "53", "Serra do Taboao"]
        ]

# Criar arquivo CSV

with open("dados.csv", "w", newline="", encoding="utf-8") as csvarquivo:
        escritor = csv.writer (csvarquivo)
        escritor.writerows (dados)

# Ler o arquivo CSV 

with open("dados.csv", "r", encoding="utf-8") as csvarquivo:
    leitor = csv.reader(csvarquivo)
    print("\nConteudo do Arquivo CSV")
    for linha in leitor:
         print(linha)     
