print("Seja bem vindo a nossa ouvidoria!")
print("made by ELR")
estalogado = False
usuario = input('nome do usuário: ')
senha = input('senha do usuário: ')

usuario_bd = 'ellias'
senha_bd = 'ellias123'
if usuario_bd == usuario and senha_bd == senha:
    estalogado = True
    print(str(usuario.upper()), ',Seja bem vindo!')

else:
    estalogado = False
    print('Usuário ou senha inválidas')
ocorrencias =[]
contador =+ 1
if estalogado == True:
    while True:
        print('1.Cadastrar Ocorrência\n2.Listar Ocorrências\n3.Apagar Ocorrências\n4.Sair')
        opc = int(input('Escolha a opção:\n'))
        if opc == 1:
            print('Cadastrar ocorrências')
            nome_pessoa = str(input("Digite o seu nome:\n"))
            cpf_pessoa = str(input("Digte o seu cpf:\n"))
            descricao = str(input("Digite a sua ocorrência:\n"))
            ocorrencia = { "id": contador,'Nome' : nome_pessoa,
                          "CPF" : cpf_pessoa,
                          'Ocorrência' : descricao}
            ocorrencias.append(ocorrencia)
            contador +=1
            for opc in ocorrencias:
                print("Você poderia deixar um feedback da nossa ouvidoria?")
                fdbk = (int(input("Caso queira, digite 1! Caso contrário, digite 2!\n")))
                if fdbk == 1:
                    input("Deixe aqui o seu feedback!\n")
                    print("Obrigado pelo o feedback e por usar nossa ouvidoria!")
                    break
                elif fdbk == 2:
                    break
                elif fdbk > 2:
                    print("Não posso executar essa ação")
                else:
                    print("Obrigado por usar nossa ouvidoria!")
        elif opc == 2:
            print("Exibindo todas as ocorrências:\n",ocorrencias)
        elif opc == 3:
            while True:
                apg = int(input("1. Para apagar todas as ocorrências \n2. Para apagar uma ocorrência específica.\n"))
                if apg == 1:
                    ocorrencias.clear()
                    print("Você apagou todas as ocorrências!")
                    break
                elif apg == 2:
                    deletar = int(input("Digite o número da ocorrência que você deseja deletar \n"))
                    ocorrencias.pop(deletar - 1)
                    for item in ocorrencias:
                        print(item)
                    break
                else:
                    print("Não posso rodar essa ação")
            continue
        elif opc == 4:
            break
            print('Você saiu do sistema, obrigado por utilizar-lo!')
        else:
            print('Opção invalida')




