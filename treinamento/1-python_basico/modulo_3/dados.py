# Exemplos de tipos de dados em Python

# int: números inteiros
idade = 30
ano = 2025
print(type(idade))  # <class 'int'>

# float: números decimais (ponto flutuante)
altura = 1.75
preco = 19.99
print(type(altura))  # <class 'float'>

# bool: valores booleanos (True ou False)
aprovado = True
maior_de_idade = idade >= 18
print(type(aprovado))  # <class 'bool'>

# complex: números complexos (parte real + parte imaginária)
numero_complexo = 2 + 3j
outro_complexo = complex(5, -7)  # 5 - 7j

print(type(numero_complexo))  # <class 'complex'>
print(numero_complexo.real)   # Parte real: 2.0
print(numero_complexo.imag)   # Parte imaginária: 3.0

# Operações com números complexos
soma = numero_complexo + outro_complexo  # (2+3j) + (5-7j) = (7-4j)
produto = numero_complexo * outro_complexo  # (2+3j)*(5-7j)

print("Soma:", soma)
print("Produto:", produto)