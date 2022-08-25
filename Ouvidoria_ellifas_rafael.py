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
ocorrencias =[]
ids = []
if estalogado == True:
    while True:
        print('1.Cadastrar Ocorrência,2.Listar Ocorrências,3.Apagar Ocorrências,4.Sair')
        opc = int(input('Escolha a opção'))
        if opc == 1:
            print('Cadastrar ocorrências')
            id += 1
            nome_pessoa = str(input("Digite o seu nome"))
            cpf_pessoa = str(input("Digte o seu cpf"))
            descricao = str(input("Digite a sua ocorrência"))
            ocorrencia = { "id":1, 'Nome' : nome_pessoa,
                          "CPF" : cpf_pessoa,
                          'Ocorrência' : descricao }
            ocorrencias.append(ocorrencia)
            ids.append(id)
        elif opc == 2:
            print(ocorrencias)
        elif opc == 3:
            print('Apagar Ocorrência')
            id_remove = int(input("Digite o id da ocorrência que você deseja deletar"))
            for i in range(len(ocorrencias)):
                if ocorrencias[i][id] == id_remove:
                    ocorrencias.pop(i)
                print("Ocorrência Apagada")
        elif opc == 4:
            break
            print('Sair')
        else:
            print('Opção invalida')




