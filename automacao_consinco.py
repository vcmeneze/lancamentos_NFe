import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = r'C:\Users\vcm70\OneDrive\Área de Trabalho\dev\automação cnsc\chromedriver.exe'
driver = webdriver.Chrome(PATH)

def login():
    # Acessar a página de login
    driver.get('http://portalnfe.bdtecsolucoes.com.br:8090/login')

    # Encontrar o campo de email e preencher com o valor fornecido
    campo_email = driver.find_element("xpath", '//*[@id="telaLogin"]/div[1]/form/div[1]/input')
    campo_email.send_keys('vitor@bispoedantas.com.br')

    # Encontrar o campo de senha e preencher com o valor fornecido
    campo_senha = driver.find_element("xpath", '//*[@id="exampleInputPassword1"]')
    campo_senha.send_keys('123456')

    # Encontrar o botão de login e clicar nele
    botao_login = driver.find_element("xpath", '//*[@id="telaLogin"]/div[1]/form/div[3]/button')
    botao_login.click()

    print('login realizado com sucesso')
login()

def view_notas():
    # Acessar a página onde a pesquisa será realizada
    driver.get('http://portalnfe.bdtecsolucoes.com.br:8090/request/searchRequest')

    # Encontrar o botão para abrir o menu de pesquisa e clicar nele
    botao_menu = driver.find_element("xpath",'/html/body/div[1]/div[1]/section/main/main/div[1]/button')
    botao_menu.click()
    time.sleep(2)

    #configurar filtros para exibir notas alocadas no nome do meu usuário
    driver.find_element("xpath", '//*[@id="inputGroupSelect01"]').send_keys('v', Keys.TAB, 'p', Keys.ENTER)
  
    # Encontrar o botão de pesquisa e clicar nele
    botao_pesquisa = driver.find_element("xpath",'//*[@id="multiCollapseExample1"]/form/div[2]/div/button')
    botao_pesquisa.click()

    # Esperar alguns segundos para a pesquisa ser processada
    time.sleep(2)
view_notas()

element = driver.find_element("xpath", '/html/body/div[1]/div[1]/section/main/main/div[3]/div[6]/table/tbody/tr[1]/td[2]')

# Obter o texto do elemento
texto = element.text

# Atribuir o valor a variável "loja"
loja = texto

# Espera 5 segundos antes de começar a execução
time.sleep(3)

# Realiza o primeiro clique
pyautogui.click(x= 1116 , y= 217 )

# Espera 1 segundo antes de realizar o próximo clique
time.sleep(1)

# Realiza o segundo clique
pyautogui.click(x= 1116 , y= 217 )

# Espera 1 segundo antes de realizar o próximo clique
time.sleep(1)

# Realiza o terceiro clique
pyautogui.click(x= 1116 , y= 217 )

# Espera 1 segundo antes de realizar o próximo clique
time.sleep(1)

# Realiza o quarto clique
pyautogui.click(x= 1116 , y= 217 )