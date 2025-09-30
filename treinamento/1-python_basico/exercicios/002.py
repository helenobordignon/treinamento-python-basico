# Entrada de dados do usuário:
nome = input("Digite seu nome: ")
print("Olá, " + nome + "!")

# Outra forma de entrada de dados:
idade = int(input("Digite sua idade: "))
print("Você tem {} anos.".format(idade))

# Posso formatar de várias maneiras:
print("{:^10} tem {:^10} anos.".format(nome, idade))