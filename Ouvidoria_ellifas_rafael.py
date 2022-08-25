print("Seja bem vindo a nossa ouvidoria!")
print("made by elliascorp")
#coloquei usuário e senha só pq achei que ficaria mais organizado :D
estalogado = False
usuario = input('nome do usuário: ')
senha = input('senha do usuário:')

usuario_bd = 'ellias'
senha_bd = 'ellias123'
if usuario_bd == usuario and senha_bd == senha:
    estalogado = True
    print(str(usuario.upper()), ',Seja bem vindo!')

else:
    estalogado = False
    print('Usuário ou senha inválidas')
if estalogado == True:
    while True:
        print('1.cdstoc,2.listoc,3.apagaroc,4.sair')
        opc = int(input('Escolha a opção'))
        if opc == 1:
            print('opção1')
        elif opc == 2:
            print('opção2')
        elif opc == 3:
            print('opção3')
        elif opc == 4:
            print('opção4')
        else:
            print('Opção invalida')




