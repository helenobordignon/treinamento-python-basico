# Variáveis

Variáveis são os blocos fundamentais da programação em Python, desempenhando um papel crucial na criação de código dinâmico e flexível. Elas permitem armazenar e manipular dados, tornando possível a criação de programas que respondem a diferentes entradas e condições. O uso correto de variáveis não apenas organiza o código de forma eficiente, mas também facilita a compreensão e manutenção dele. Ao entender e dominar o uso de variáveis, os programadores ganham a capacidade de criar soluções complexas de forma mais clara, impulsionando o desenvolvimento de aplicações mais robustas e eficazes em Python.

# Conceitos

As variáveis são abstrações para endereços de memória que permitem que os programas fiquem mais fáceis de codificar, entender e depurar. Ao nomear uma variável com o identificador x, determinado espaço em memória passará a ter esse apelido. Em outras palavras, será possível acessar esse espaço de memória sabendo o seu apelido e, consequentemente, recuperar o valor guardado nele, que no nosso exemplo é 10.

Uma analogia possível com o mundo real é com aquelas caixas de correio que ficam em frente às casas.
Em Python, o operador de atribuição é o = (símbolo de igual). A instrução x = 10 atribui o valor 10 à variável x.

**Comentário:**
Diferentemente de outras linguagens, como C ou Java, não é necessário declarar uma variável antes de utilizá-la em Python. Basta atribuir um valor inicial à variável e utilizá-la dali em diante. Embora não seja necessário declarar uma variável para utilizá-la, não é possível utilizar uma variável que não tenha recebido alguma atribuição de valor.

# Identificadores de variáveis

Os identificadores das variáveis podem ser compostos por letras, o underline (_) e, com exceção do primeiro caractere, números de 0 a 9. Veja os exemplos.

_São nomes de variáveis válidos:_
MinhaVariavel
_variavel 
salario1
salario1_2 

_Não são válidos:_
1variavel
salario-1

MinhaVariavel e minhavariavel _São identificadores de duas variáveis distintas._

# Conceito de amarração (Binding)