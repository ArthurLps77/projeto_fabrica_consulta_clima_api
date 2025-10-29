# etapa
#1. definir chave de api e o link da requisitão

import requests

api_key ='2a1ac38a32354cb7b19133643251408'
cidade = input('digite o nome da cidade: ').strip() # imput para receber ainformação do usuario e a função

url= f'https://api.weatherapi.com/v1/current.json' # usar url

#2.  parametros da requisisão
parametros ={
    'key':api_key,
    'q':cidade,
    'lang':'pt'  # define a lingua da resposta como português
}

# 3. Fazer a requisisão
respostas =  requests.get(url, params=parametros) # o metodo qure utilizamos é get e informamos o parametros dressa requisisão

# 4. verificar a se a requisisão foi bem sucedida
if respostas.status_code == 200:
    dados = respostas.json() # convertendo a resposta json em um dicionario em Python
    temperatura = dados['current']['temp_c']
    descricao = dados['current']['condition']['text']
    print(f'Temperatura na cidade {cidade} é {temperatura}°c.')
    print(f'Descrição: {descricao}')
else:
    print(f'Erro na requisição: {respostas.status_code}')
    print(respostas.content)