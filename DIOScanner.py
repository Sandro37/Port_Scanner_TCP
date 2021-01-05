import nmap

scanner = nmap.PortScanner()

print("Seja bem vindo ao DIOScaner")
print("<--------------------------->")

ip = input("Digite o ip a ser varrido:")

print("IP Digitado foi: {}".format(ip))

print(type(ip))

while True:
    menu = int(input("""\nEscolha um tipo de varredura a ser realizada
          1 -> Varredura do Tipo SYN
          2 -> Varredura do Tipo UDP
          3 -> Varredura do TIpo Intenso
               Digite a opção escolhida:"""))
    if menu == 1 or menu == 2 or menu == 3:
        break
    else:
        print("\nDigite Umas das escolhas")

print("A opção escolhida foi: {}".format(menu))
try:
    if menu == 1:
        print("Versão do Nmap: {}".format(scanner.nmap_version()))
        scanner.scan(ip, '1-1024', '-v -sS')
        print(scanner.scaninfo())
        print("Status do ip: {}".format(scanner[ip].state()))
        print(scanner[ip].all_protocols())
        print("\nPortas Abertas: {}".format(scanner[ip]['tcp'].keys()))
    elif menu == 2:
        print("Versão do Nmap: {}".format(scanner.nmap_version()))
        scanner.scan(ip, '1-1024', '-v -sU')
        print(scanner.scaninfo())
        print("Status do ip: {}".format(scanner[ip].state()))
        print(scanner[ip].all_protocols())
        print("\nPortas Abertas: {}".format(scanner[ip]['udp'].keys()))
    elif menu == 3:
        print("Versão do Nmap: {}".format(scanner.nmap_version()))
        scanner.scan(ip,'1-1024', '-v -sC')
        print(scanner.scaninfo())
        print("Status do ip: {}".format(scanner[ip].state()))
        print(scanner[ip].all_protocols())
        print("\n Portas Abertas: {}".format(scanner[ip]['tcp'].keys()))
except Exception as ex:
    print(ex)