from datetime import datetime
import random

print('----------- Sejam bem vindo -----------')

nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))
data_cadastro = datetime.now()
cartoes = ['R$ 50,00', 'R$ 250,00', 'R$ 120,00']
cartao = random.choices(cartoes)
datanasc = datetime.strptime(
    input('Digite sua data de aniversário no formato dd/mm/aaaa: '), '%d/%m/%Y')

print(f'Olá {nome}, seu registro foi concluído com sucesso no dia {data_cadastro.day}/{data_cadastro.month}/{data_cadastro.year}.\nParabéns, houve um sorteio e você recebeu um cartão de compras no valor de: {cartao}')
