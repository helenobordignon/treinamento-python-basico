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