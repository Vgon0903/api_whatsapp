from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd 

navegador = webdriver.Chrome()
#navegador.get("https://web.whatsapp.com/")
#espeta tela do whatsapp carregar 
#while len(navegador.find_elements(By.ID,'side')) < 1: # -> lista for vazia -> o elemento que diz que a tela já carregou
 #       time.sleep(1)
#time.sleep(2) #só por garantia 

#whatsapp carregou

tabela = pd.read_excel("Envios.xlsx")
#display(tabela)

import urllib

for linha in tabela.index:
        #enviar msg para pessoa 
        nome = tabela.loc[linha,"nome"]
        mensagem = tabela.loc[linha,"mensagem"]
        arquivo = tabela.loc[linha,"arquivo"]
        telefone = tabela.loc[linha,"telefone"]

        texto = mensagem.replace("fulano",nome)
        texto = urllib.parse.quote(texto)
        
#enviar mensagem 
link = f"https://web.whatsapp.com/send?phone={telefone}&text={texto}"


navegador.get(link)
#esperar tela do whatsapp carregar -> espera um elemento que só existe na tela já carregada aparecer
while len(navegador.find_elements(By.ID,'side')) < 1: # -> lista for vazia -> o elemento que diz que a tela já carregou
        time.sleep(1)
time.sleep(2) #só por garantia 

# você tem  que verificar se o número é inválido
#if len(navegador.find_element(By.XPATH,'//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[1]')) < 1:
#enviar msg
navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click
time.sleep(2)
