import requests #responsavel pela requisiçao
from bs4 import BeautifulSoup

#feed-post-link
url = "https://tntsports.com.br/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; 64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.26"
}
resposta = requests.get(url)

if resposta.status_code == 200:
    print("requisao feita com sucesso")
    # print(resposta.text)


    soup = BeautifulSoup(resposta.text, "html.parser")

    noticias = soup.find_all("h2", class_="news__title")

    print("ultimas noticias do G1:")
    for index, noticia in enumerate(noticias):
        print(f"{index + 1}. {noticia.text.strip()}")
else: 
    print(resposta)
    print("deu erro")