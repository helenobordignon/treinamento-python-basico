numero = int(input('Digite um número para ver sua tabuada: '))
# Exemplo de tabuada usando for
print(f'Tabuada do {numero}:')
for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')