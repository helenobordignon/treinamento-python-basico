a = 0
for i in range(30):
    if a % 2 == 0:
        a += 1
        continue
    else:
        if a % 5 == 0:
            break
        else:
            a += 3
print (a)

###   Blocos   [ Indentação ] ###

'''
Em Python, os blocos são definidos pela indentação. 
Diferente de C e Java, que usam as chaves { e } para delimitar os blocos.
Em Python, todos os blocos são iniciados com o símbolo : (dois pontos) na linha superior 
e representados pelo acréscimo de 4 (quatro) espaços à esquerda. 
'''

# Linha 1
# Está mais à esquerda, assim como as linhas 2 e 11.

# Linha 2
# Todas as linhas de 3 a 10 estão dentro do bloco do for da linha 2.

# Linha 3
# Observe que a linha 3 tem um if abrindo um bloco, dentro do qual estão as linhas 4 e 5.

# Linha 6
# Por sua vez, a linha 6 tem um else abrindo outro bloco, composto pelas linhas de 7 a 10. 
# Os blocos do if (linha 3) e do else (linha 6) estão no mesmo nível.

# Linha 7
# Mostra outro if abrindo outro bloco – composto apenas pela linha 8 – que está no mesmo nível 
# do bloco do else da linha 9 – composto apenas pela linha 10.

# Linha 11
# Como a linha 11 está no mesmo nível da linha 2, ela não faz parte do bloco do for.

'''
Boas práticas de programação:

- Inclusão de comentários.
Uma prática muito importante é utilizar comentários no seu programa, explicando o que aquele trecho resolve.

- PEP
Uma característica marcante da comunidade de desenvolvedores Python é manter uma lista de propostas de melhorias, chamadas PEP.
'''