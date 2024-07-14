import time # Importa a biblioteca de tempo para aguardar a execução
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager # Importa o gerenciador de driver do Chrome
from selenium.webdriver.chrome.service import Service # Importa o serviço do Selenium para executar o driver

service = Service(ChromeDriverManager().install()) # Instala o driver do Chrome verificando a versão atual

navegador = webdriver.Chrome(service=service) # Inicia o navegador Chrome

navegador.get('https://www.instagram.com/') # Acessa o site conforme a url informada

#para fazer login
navegador.find_element('xpath',
                       '//*[@id="loginForm"]/div/div[1]/div/label/input' ).send_keys("seu login") # como vc vai encontrar o elemento & qual é o xpath dele

#para colocar a senha
navegador.find_element('xpath',
                       '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("sua senha") # como vc vai encontrar o elemento & qual é o xpath dele

navegador.find_element('xpath',
                       '//*[@id="loginForm"]/div/div[3]').click()

try:
    while True:
        pass
except KeyboardInterrupt:
    navegador.quit()

