# Estruturas de decisão

Você irá descobrir o poder do condicional if em Python, compreendendo a estrutura de controle de fluxo mais fundamental da linguagem. Aprenderá a criar condições, tomar decisões e controlar o fluxo do seu código de maneira eficiente e clara.

**Tratamento das condições:**

As estruturas de controle permitem selecionar quais partes do código (chamadas de estruturas de decisão) serão executadas e repetir blocos de instruções com base em algum critério, como uma variável de controle ou a validade de alguma condição (denominadas estruturas de repetição).

**if**
Em Python, usamos o if para executar um bloco de código se uma condição for verdadeira. A sintaxe básica é a que mostraremos a seguir.

Exemplo:

if condição:
   bloco_de_codigo

Se a condição for verdadeira, o bloco_de_codigo será executado.

**if-else**
Podemos adicionar uma condição alternativa usando else. Isso nos permite definir o que fazer se a condição do if for falsa. A sintaxe é a que mostraremos a seguir.

Exemplo:

if condição:
    bloco_de_codigo_if
else:
    bloco_de_codigo_else

**elif**
Além do if e else, Python nos oferece o elif, que é uma combinação de else if. O elif nos permite testar várias condições de forma sequencial. Confira a sintaxe no código.

Exemplo:

if condição_1:
    bloco_de_codigo_if
elif condição_2:
    bloco_de_codigo_elif
else:
    bloco_de_codigo_else

# Estrutura de repetição for

Aqui você vai compreender o universo do loop for e da função range em Python. Veja de forma clara e prática como usar essas ferramentas para iterar sobre sequências e executar tarefas repetitivas.

As _estruturas de repetição for_ permitem repetir um bloco de código para cada item de uma sequência.
Antes de detalharmos o for, vamos conhecer uma função de Python que gera uma lista de valores numéricos. Essa lista nos ajudará a entender a repetição e deixará mais claro o funcionamento do laço.

**As listas do tipo range()**
Ao chamar o método range(), Python cria uma sequência de números inteiros, desde uma maneira simples até a mais complexa. 
Observe:

_Simples_
Envolve apenas um argumento. Nesse caso, a sequência começará em 0 e será incrementada de uma unidade até o limite do parâmetro passado (exclusive).
Exemplo: range(3) # Cria a sequência (0, 1, 2)

_Não iniciadas em 0_
Para que a sequência não comece em 0, pode-se informar o início e o fim como parâmetros. Lembre-se de que o parâmetro fim não entra na lista (exclusive o fim). O padrão é incrementar cada termo em uma unidade.
Exemplo: range(2, 7) # Cria a sequência (2, 3, 4, 5, 6)

_Indicando início, fim e passo_
É possível criar sequências mais complexas indicando, na ordem, os parâmetros de início, fim e passo. O passo é o valor que será incrementado de um termo para o próximo.
Exemplo: range(2, 9, 3) # Cria a sequência (2, 5, 8)

A sintaxe da estrutura for
A estrutura for tem a seguinte sintaxe em Python:
for <variável> in <sequência>:
     Bloco que será repetido para todos os itens da sequência
 Instrução fora do for

 # Estrutura de repetição while e instruções auxiliares

 Agora você vai descobrir os segredos do loop while e das declarações break, continue e pass em Python. Confira a lógica por trás dessas estruturas de controle de fluxo e aprenda a criar loops eficientes, interromper iterações indesejadas, continuar para a próxima iteração ou simplesmente passar adiante.

**Estrutura de repetição while:**
Permite executar repetidamente um bloco de código enquanto uma condição for verdadeira. Vamos aprender como utilizá-la e ver alguns exemplos para entender melhor.
A sintaxe do while é a apresentada a seguir:

while condição:
    bloco_de_codigo

O bloco_de_codigo será repetido enquanto a condição for verdadeira. Assim que a condição se tornar falsa, a execução sai do laço while.

O laço while infinito
Laços infinitos são úteis quando queremos executar um bloco de instruções indefinidamente. O laço while infinito tem o formato que mostraremos a seguir:

while True:
    bloco_de_codigo