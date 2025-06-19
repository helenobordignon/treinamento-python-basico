# Estrutura de repetição if else

# Exemplo 1

idade = eval(input('Informe a idade da criança: \n'))
if idade < 5:
    print('A criança deve ser vacinada contra a gripe.')
    print('Procure o posto de saúde mais próximo.')
elif idade == 5:
    print('A vacina estará disponível em breve.')
    print('Aguarde as próximas informações.')
else:
    print('A vacinação só ocorrerá daqui a 3 meses.')
    print('Informe-se novamente neste prazo.')
print('Cuide da saúde sempre. Até a próxima.')

# Exemplo 2

idade = int(input("Digite sua idade: "))
if idade < 10:
    print("Você é uma criança.")
elif idade >= 10 and idade <= 15:
    print("Você é um adolescente.")
elif idade >= 16 and idade < 18:
    print("Você é menor de idade.")
elif idade >= 18 and idade < 65:
    print("Você é adulto.")
else:
    print("Você é um idoso.")
