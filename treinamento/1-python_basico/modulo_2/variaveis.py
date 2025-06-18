# As variáveis são abstrações para endereços de memória que permitem que os programas fiquem mais fáceis de codificar, entender e depurar.
# Os identificadores das variáveis podem ser compostos por letras, o underline (_) e, com exceção do primeiro caractere, números de 0 a 9.

# Variáveis:

# Inteiro (int)
idade = 30

# Ponto flutuante (float)
altura = 1.75

# String (str)
nome = "Maria"

# Booleano (bool)
eh_maior_de_idade = True

# Lista (list)
frutas = ["maçã", "banana", "laranja"]

# Tupla (tuple)
coordenadas = (10.0, 20.0)

# Dicionário (dict)
pessoa = {"nome": "João", "idade": 25}

# Conjunto (set)
numeros_unicos = {1, 2, 3, 4}

# NoneType (None)
valor_nulo = None

# Variáveis na prática:

# Passo 1: Definir a função imprimir_dados
def imprimir_dados(texto, numero):
    print("Número:", numero)
    print("Texto:", texto)
 
# Passo 2: Chamar a função imprimir_dados com dois argumentos
imprimir_dados("Ano: ", 2025) 


# Variáveis locais e globais:
# As variáveis locais são aquelas definidas dentro de uma função e só podem ser acessadas dentro dessa função.
# As variáveis globais são aquelas definidas fora de qualquer função e podem ser acessadas em qualquer parte do código.

# Exemplo de variáveis locais e globais:
def multiplicador(numero):
        a = 2 # esta variável tem escopo local
        print(f"Dentro da função, a variável vale: {a}")
        return a * numero

a = 3 # esta variável tem escopo global
b = multiplicador(5)
print(f"Fora da função, a variável a vale: {a}")

# Constantes

# Em Python, não há uma maneira nativa de definir constantes como em outras linguagens, mas é uma convenção usar letras maiúsculas para indicar que uma variável deve ser tratada como constante.
PI = 3.14159  # Constante para o valor de pi

# Operadores matemáticos

# <	    Menor que
# <=	Menor ou igual a
# >	    Maior que
# >=	Maior ou igual a
# ==	Igual
# !=	Não igual
