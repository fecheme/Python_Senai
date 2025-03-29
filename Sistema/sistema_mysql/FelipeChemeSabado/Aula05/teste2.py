from selenium import webdriver
from selenium.webdriver.common.by import By
import schedule
import time
import pywhatkit

# Função principal para realizar a pesquisa
def realizar_pesquisa():
    # Configurar o navegador
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Executar em modo headless (sem interface gráfica)
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

    driver = webdriver.Chrome(options=options)

    try:
        # Acessar a URL
        url = 'https://www.webmotors.com.br/carros/sp-cotia/volkswagen/golf?tipoveiculo=carros&localizacao=-23.6026684%2C-46.9194693x100km&estadocidade=S%C3%A3o%20Paulo-Cotia&marca1=VOLKSWAGEN&modelo1=GOLF&lkid=1042&page=1'
        driver.get(url)
        time.sleep(5)  # Esperar a página carregar

        # Extrair dados
        mensagem = ""
        carros = driver.find_elements(By.CLASS_NAME, '_Container_70j0p_1')
        for carro in carros:
            nome = carro.find_element(By.CLASS_NAME, '_web-title-medium_qtpsh_51').text
            modelo = carro.find_element(By.CLASS_NAME, '_body-regular-small_qtpsh_152').text
            ano = carro.find_element(By.CLASS_NAME, '_body-regular-small_qtpsh_152').text
            km = carro.find_elements(By.CLASS_NAME, '_body-regular-small_qtpsh_152')[1].text
            localizacao = carro.find_element(By.CLASS_NAME, '_body-regular-small_qtpsh_152').text
            preco = carro.find_element(By.CLASS_NAME, '_body-bold-large_qtpsh_78').text
            
            mensagem += f"Nome: {nome}\nModelo: {modelo}\nAno: {ano}\nQuilometragem: {km}\nLocalização: {localizacao}\nPreço: {preco}\n{'-' * 50}\n"

        # Enviar resultados via WhatsApp
        numero_destino = "+5511998837967"  # Substitua pelo número do destinatário
        pywhatkit.sendwhatmsg_instantly(numero_destino, mensagem)
        print("Mensagem enviada com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    finally:
        driver.quit()

# Agendamento diário
schedule.every().day.at("07:00").do(realizar_pesquisa)

# Menu de interação para execução manual ou agendada
if __name__ == "__main__":
    print("Escolha uma opção:")
    print("1. Executar pesquisa manual agora")
    print("2. Aguardar pela execução automática às 7 da manhã")
    opcao = input("Digite o número da sua escolha: ")

    if opcao == "1":
        print("Executando pesquisa manual...")
        realizar_pesquisa()  # Executa a pesquisa manualmente
    elif opcao == "2":
        print("Aguardando execução automática. Não feche o script.")
        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Opção inválida. Por favor, reinicie o script.")




        """
        import pywhatkit

numero_destino = "+55SEUNUMEROAQUI"  # Substitua pelo seu número completo
mensagem = "Teste de envio pelo pywhatkit"
pywhatkit.sendwhatmsg_instantly(numero_destino, mensagem)

        
        
        """
