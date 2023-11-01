import requests
from lxml import html
import pandas as pd
import warnings
import urllib3
import b3_fiis as b3

warnings.filterwarnings('ignore', category=urllib3.exceptions.InsecureRequestWarning)

on = True

meus_fiis = pd.read_excel('ibrx.xls')
lista_ativos = meus_fiis['Código'].tolist()
url_base = 'https://www.fundsexplorer.com.br/funds/'


def cotacao_atual_meusfiis():
    
    for ativo in lista_ativos:
        url = url_base + ativo
        response = requests.get(url, verify=False)
        tree = html.fromstring(response.content)
        
        preco = tree.xpath(b3.preco_atual)[0].text_content()
        
        print(f"Preço atual de {ativo}: {preco}", ativo, preco)
    
while on == True:
    selec = int(input("\nSelecione uma opção:\n\n1. Ver todas as minhas cotações.\n\n2. Procurar informções.\n\n0. Sair\n\n"))
    
    if selec == 1:
        cotacao_atual_meusfiis()
    elif selec == 2:
        ativo = input("Digite o código do ativo desejado: ")
        print(b3.cotacao_atual(ativo))
        print(b3.ultimo_dividendo(ativo))
        print(b3.p_vp(ativo))
        print(b3.valor_patrimonial(ativo))
    elif selec == 0:
        on = False
    else:
        print("Opção invalida, tente novamente!")