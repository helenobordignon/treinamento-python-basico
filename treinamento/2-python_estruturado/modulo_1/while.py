import time

palavra = input('Entre com uma palavra: \n')
while palavra != 'sair':
    palavra = input('Digite sair para encerrar o laço: \n')
print('Você digitou sair e agora está fora do laço')

# Exemplo de laço infinito

while True:
    temperatura = ler_sensor_temperatura()  # type: ignore # Supomos que esta função leia a temperatura do sensor
    registrar_temperatura(temperatura)      # type: ignore # Supomos que esta função registre a temperatura lida
    time.sleep(60)  # Aguarda 60 segundos antes de ler novamente

# Função para demonstrar o uso de break no laço while
def exemplo_laco():
    while True:
        print('Você está dentro do laço.')
        opcao = input('Deseja sair do laço? Digite SIM para isso. \n')
        if opcao == 'SIM':
            break  # sai do laço
    print('Você saiu do laço')

# Função para demonstrar laços aninhados com break
def exemplo_laco_aninhado():
    while True:
        print('Você está no primeiro laço.')
        opcao1 = input('Deseja sair dele? Digite SIM para isso. \n')
        if opcao1 == 'SIM':
            break  # este break é do primeiro laço
        else:
            while True:
                print('Você está no segundo laço.')
                opcao2 = input('Deseja sair dele? Digite SIM para isso. \n')
                if opcao2 == 'SIM':
                    break  # este break é do segundo laço
            print('Você saiu do segundo laço.')
    print('Você saiu do primeiro laço')

# Exemplo com continue

for num in range(1, 11):
    if num == 5:
        continue
    else:
        print(num)
print('Laço encerrado')