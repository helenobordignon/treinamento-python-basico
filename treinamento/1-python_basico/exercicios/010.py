# Conversor de moeda
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

dolar = 3.27

real = float(input('Quanto dinheiro você tem na carteira? R$ '))
conversao = real / dolar
print(f'Com R$ {real:.2f} você pode comprar US$ {conversao:.2f}')