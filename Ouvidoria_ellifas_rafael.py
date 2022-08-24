print("Seja bem vindo a nossa ouvidoria!")
print("made by elliascorp")
#coloquei usuário e senha só pq achei que ficaria mais organizado :D

usuario = input('nome do usuário: ')
senha = input('senha do usuário:')

usuario_bd = 'ellias'
senha_bd = 'ellias123'



if usuario_bd == usuario and senha_bd == senha:
    print(str(usuario.upper()), ',Seja bem vindo!')

else:
    print('Usuário ou senha inválidas')



