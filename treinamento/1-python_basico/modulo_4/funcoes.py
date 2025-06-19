# A função eval()
numero = eval(input("Digite um número: "))
# Imprimindo o número digitado  
print(f"Você digitou o número: {numero}")

# A função type()   
print("O tipo de dado da variável 'numero' é:", type(numero))

# A função len()    
texto = input("Digite um texto: ")
# Imprimindo o tamanho do texto digitado
print(f"O tamanho do texto digitado é: {len(texto)} caracteres")

# A função str()
numero_str = str(numero)
# Imprimindo o número convertido para string
print(f"O número {numero} como string é: {numero_str}")

# A função int()
numero_int = int(numero)    
# Imprimindo o número convertido para inteiro
print(f"O número {numero} como inteiro é: {numero_int}")

# A função float()
numero_float = float(numero)
# Imprimindo o número convertido para float
print(f"O número {numero} como float é: {numero_float}")

# A função bool()
numero_bool = bool(numero)
# Imprimindo o número convertido para booleano
print(f"O número {numero} como booleano é: {numero_bool}")

# A função round()
numero_arredondado = round(numero_float)
# Imprimindo o número arredondado
print(f"O número {numero_float} arredondado é: {numero_arredondado}")

# A função abs()
numero_absoluto = abs(numero_int)
# Imprimindo o valor absoluto do número
print(f"O valor absoluto de {numero_int} é: {numero_absoluto}")

# A função max() e min()
numeros = [1, 2, 3, 4, 5]
# Imprimindo o maior e o menor número da lista
print(f"O maior número da lista é: {max(numeros)}")
print(f"O menor número da lista é: {min(numeros)}")

# A função sum()
soma_numeros = sum(numeros) 
# Imprimindo a soma dos números da lista
print(f"A soma dos números da lista é: {soma_numeros}")

# A função sorted()
numeros_ordenados = sorted(numeros)
# Imprimindo a lista de números ordenados   
print(f"A lista de números ordenados é: {numeros_ordenados}")

# A função reversed()
numeros_reversos = list(reversed(numeros))
# Imprimindo a lista de números em ordem reversa
print(f"A lista de números em ordem reversa é: {numeros_reversos}")

# A função zip()
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
# Imprimindo a lista de tuplas combinando elementos das duas listas
lista_zip = list(zip(lista1, lista2))
print(f"A lista de tuplas combinando elementos das duas listas é: {lista_zip}")

# A função enumerate()
lista3 = ['x', 'y', 'z']
# Imprimindo a lista de tuplas com índice e valor
lista_enum = list(enumerate(lista3))
print(f"A lista de tuplas com índice e valor é: {lista_enum}")

# A função filter()
def is_even(num):
    return num % 2 == 0
lista_filtrada = list(filter(is_even, numeros))
# Imprimindo a lista filtrada com números pares
print(f"A lista filtrada com números pares é: {lista_filtrada}")

# A função map()
def square(num):
    return num ** 2
lista_map = list(map(square, numeros))
# Imprimindo a lista com os números ao quadrado
print(f"A lista com os números ao quadrado é: {lista_map}")

# A função reduce() (necessário importar do módulo functools)
from functools import reduce
def multiply(x, y):
    return x * y
lista_reduzida = reduce(multiply, numeros)
# Imprimindo o resultado da redução da lista
print(f"O resultado da redução da lista (multiplicação) é: {lista_reduzida}")

# A função any() e all()
lista_booleanos = [True, False, True]
# Imprimindo se algum elemento da lista é True
print(f"Algum elemento da lista é True? {any(lista_booleanos)}")
# Imprimindo se todos os elementos da lista são True
print(f"Todos os elementos da lista são True? {all(lista_booleanos)}")

# A função input() com validação
def validar_numero():
    while True:
        try:
            numero = float(input("Digite um número: "))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
numero_validado = validar_numero()
print(f"Você digitou o número validado: {numero_validado}") 

# A função input() com validação de string
def validar_texto():
    while True:
        texto = input("Digite um texto: ")
        if texto.strip():  # Verifica se o texto não está vazio
            return texto
        else:
            print("Entrada inválida. Por favor, digite um texto não vazio.")
texto_validado = validar_texto()
print(f"Você digitou o texto validado: {texto_validado}")

# A função input() com validação de número inteiro
def validar_numero_inteiro():
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro válido.")
numero_inteiro_validado = validar_numero_inteiro()
print(f"Você digitou o número inteiro validado: {numero_inteiro_validado}") 
