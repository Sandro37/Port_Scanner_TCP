import socket

#variáveis
ports = []
count = 0

qtdPortas = int(input("Quantidade de portas que deseja:"))
ip = input('Digite o host ou ip a ser verificado:')

while count < qtdPortas:
    ports.append(int(input("Digite a porta a ser verificada:")))
    count +=1


for port in ports:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.05)
    code = cliente.connect_ex((ip, port))

    if code == 0:
        print('{} -> Porta Aberta'.format(port))
    else:
        print('{} -> Porta Fechada'.format(port))

print("Scan Finalizado")