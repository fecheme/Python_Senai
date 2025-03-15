import pandas as pd
import matplotlib.pyplot as plt
# criar os dados para o dataframa

dados = {
    
    "Nome": ["Bruno", "Maria", "Felipe", "Paulo", "Carlos"],
    "Idade": [28, 32, 19, 55, 18],
    "Cidade": ["Cotia", "Carapicuiba", "Ibiuna", "Sao Paulo", "Sao Paulo"]
    }



df = pd.DataFrame(dados)
# exibir o dataframe
print(df)

# salvar dataframe no CSV 
df.to_csv("pandas_dados.csv", index=False)

# visualizar em data frame o csv

df_csv = pd.read_csv("pandas_dados.csv")

df_filtrado = df[df["Idade"] > 25] 
print (df_filtrado)

df_ordenado = df.sort_values(by="Idade", ascending=False)
print(df_ordenado) # do maior para o menor (decrescente)

# Exibir estatisticas 
print(df.describe())

df.plot(kind="bar", x="Nome", y="Idade", color="blue")
plt.title("Idade das pessoas")
plt.xlabel("nome")
plt.ylabel("Idade")
plt.show()

