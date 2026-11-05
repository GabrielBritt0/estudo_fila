fila = ['GABRIEL', 'DIEGO', 'LUARA'] 

#menu para o usuário escolher o que deseja no programa
def menu():

    print('''
1- Adicionar
2- Retirar
3- Sair
    ''')
menu()

def adicionar():
    while True:
        adicionar_fila = str(input('Digite a proxima pessoa da fila ou N para parar: ')).upper()

        if adicionar_fila != 'N':
            fila.append(adicionar_fila)
            print(fila)
        else:
            break

def retirar():
    fila.pop(0)
    print(fila)

while True:
    escolha = int(input('Escolha uma opção: '))
    if escolha == 1:
        adicionar()
    elif escolha == 2:
        retirar()
    elif escolha == 3:
        break


