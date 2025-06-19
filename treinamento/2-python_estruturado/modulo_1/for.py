# Estrutura de repetição for

# Exemplo 1: Iterando sobre uma lista
lista = [1, 2, 3, 4, 5]
for numero in lista:
    print(numero)

# Exemplo 2: Iterando sobre uma string
string = "Python"
for letra in string:
    print(letra)

# Exemplo 3: Usando range para iterar números
for i in range(5):
    print(i)

# Exemplo 4: Iterando sobre um dicionário
dicionario = {'a': 1, 'b': 2, 'c': 3}
for chave, valor in dicionario.items():
    print(f"Chave: {chave}, Valor: {valor}")

# Exemplo 5: Iterando com índice usando enumerate
lista_numeros = [10, 20, 30, 40]    
for indice, numero in enumerate(lista_numeros):
    print(f"Índice: {indice}, Número: {numero}")

# Exemplo 6: Usando for com listas aninhadas
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  
for linha in matriz:
    for numero in linha:
        print(numero)

# Exemplo 7: Usando for com condicionais
for i in range(10):
    if i % 2 == 0:  # Verifica se o número é par
        print(f"{i} é par")
    else:
        print(f"{i} é ímpar")

# Exemplo 8: Usando for com break e continue
for i in range(10):
    if i == 5:
        print("Encontrou o número 5, saindo do loop.")
        break  # Sai do loop quando i é 5
    if i % 2 == 0:
        continue  # Pula para a próxima iteração se i for par
    print(f"Número ímpar: {i}")

# Exemplo 9: Usando for com else
for i in range(3):
    print(f"Iteração {i}")
else:
    print("Loop for concluído sem interrupções.")

