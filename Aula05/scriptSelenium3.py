from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configurar o navegador
options = webdriver.ChromeOptions()

# Argumentos adicionais para evitar bloqueios
options.add_argument('--headless')  # Executar sem interface gráfica
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
options.add_argument('--disable-infobars')  # Ocultar infobars do Chrome
options.add_argument('--disable-extensions')  # Desativar extensões
options.add_argument('--no-sandbox')  # Desativar sandbox (apenas em sistemas confiáveis)
options.add_argument('--disable-dev-shm-usage')  # Melhorar desempenho em sistemas com pouca memória compartilhada
options.add_argument('--lang=pt-BR')  # Configurar idioma para português brasileiro
options.add_argument('--start-maximized')  # Simular inicialização em tela cheia
options.add_experimental_option('excludeSwitches', ['enable-automation'])  # Remover marcas de automação
options.add_experimental_option('useAutomationExtension', False)  # Evitar detecção de extensão

# Inicializar o WebDriver com as opções configuradas
driver = webdriver.Chrome(options=options)

try:
    # Acessar a URL da Shopee para buscar "teclado"
    url = 'https://shopee.com.br/search?keyword=teclado'
    driver.get(url)
    time.sleep(5)  # Esperar a página carregar completamente

    # Extrair dados dos produtos
    produtos = driver.find_elements(By.CSS_SELECTOR, ".shopee-search-item-result__item")

    # Armazenar resultados em uma lista para análise
    resultados = []

    for produto in produtos[:10]:  # Limitar aos 10 primeiros resultados
        try:
            nome = produto.find_element(By.CSS_SELECTOR, ".Cve6sh").text
            preco = produto.find_element(By.CSS_SELECTOR, ".ZEgDH9").text
            link = produto.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
            
            resultados.append({
                'nome': nome,
                'preco': preco,
                'link': link
            })
        except Exception as e:
            print(f'Erro ao processar produto: {e}')

    # Exibir os produtos
    for produto in resultados:
        print(f"Nome: {produto['nome']}")
        print(f"Preço: {produto['preco']}")
        print(f"Link: {produto['link']}")
        print('-' * 50)

finally:
    # Fechar o navegador
    driver.quit()
