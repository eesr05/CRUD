import dois

password = '123'
user = 'admin'
contador = 1
while (contador<3):
    usuario= input("Usuario: ")
    senha = input("Senha: ")
    if(usuario==user and  senha==password):
        print("Acesso liberado")   
        break           
    elif ((user != usuario or senha != password) and contador==3):
        print("Usuario ou senha incorretos. Tente novamente.")
    else:
        print("Usuario ou senha incorretos. Tente novamente.")
        contador = contador + 1  
        
print('======================')
print('       MoThor         ')
print('======================')



# password = '123'
# user = 'admin'
# contador = 0
# while contador <= 3:
#     usuario = input('Usuario: ')
#     senha = input('Senha: ')
#     if usuario != user or senha != password:
#         print('errado')
#         contador = contador +1
#         break
#         print('Tchau')
#     else:
#         print('Certo')



    #break
while True:
    print('=====================')
    print('   Menu Principal    ')
    print('=====================')
    print('[1]Cadastrar')
    print('[2]Mostrar Todos')
    print('[3]Selecionar um')
    print('[4]Alterar')
    print('[5]Excluir')
    print('[6]Sair do Sistema')
    menu = int(input('Escolha uma opção: '))
    if menu == 1:

        dois.li()
        # cadastro.listas(menu)
        #li = cadastro.cadastro(menu) + cadastro.listas(menu)
        #print(li)
        volta = str(input('Pressione qualquer tecla para voltar ao Menu Principal. '))

    if menu == 2:
        dois.mostrarTudo()
        #cadastro.cadastro()

        volta = str(input('Pressione qualquer tecla para voltar ao Menu Principal. '))
    elif menu == 3:
        dois.selecionar()
        volta = str(input('Pressione qualquer tecla para voltar ao Menu Principal. '))
    elif menu == 4:
        dois.alterar()
        volta = str(input('Pressione qualquer tecla para voltar ao Menu Principal. '))
    elif menu == 5:
        dois.deletar()
        volta = str(input('Pressione qualquer tecla para voltar ao Menu Principal. '))
    elif menu == 6:
        print('Programa encerrado.')
        print('Tchau')
        break