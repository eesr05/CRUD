def login():
    
    return

def li():
    ficha = list([['Maria', ' Gerente ', '9.000'], ['Olivia', ' CEO  ', ' 12.000'], ['Jose', ' Editor  ', ' 2.300']])
    while True:
        nome = str(input('Nome: '))
        cargo = str(input('Cargo: '))
        sal = float(input('Salario: '))
        idade = int(input('Idade: '))
        sexo = str(input('Sexo: '))
        cpf = int(input('CPF: '))
        remoto = input('Remoto: ').upper()
        while sexo not in 'FfMm':
            sexo = str(input('Dados invalidos. Tente novamente, sexo: '))
        while remoto not in 'SimSsNaoNn':
            remoto = str(input('Resposta invalida, por favor tente novamente: '))

        ficha.append([nome, cargo, sal])
        resp = str(input('Deseja adicionar outro: [S/N]'))
        if resp in 'Nn':
            break
    print('==' * 30)
    print(f'{"No.": <4}{"Nome": <15}{"Cargo":<10}{"Salario":>18}')
    print('==' * 30)
    for i, a in enumerate(ficha):
        print(f'{i:<4}{a[0]:<15}{a[1]:<10}{a[2]:>18}')
    while True:
        deseja = input('Voltar ao menu principal: 1-Sim  ')
        if deseja == '1':
            break
        
            
    return


def mostrarTudo():
    ficha = list([['Maria', ' Gerente ', '9.000'], ['Olivia', ' CEO  ', ' 12.000'], ['Jose', ' Editor  ', ' 2.300']])
    print('==' * 30)
    print(f'{"No.": <4}{"Nome": <15}{"Cargo":<10}{"Salario":>18}')
    print('==' * 30)
    for i, a in enumerate(ficha):
        print(f'{i:<4}{a[0]:<15}{a[1]:<10}{a[2]:>18}')
    return


def selecionar():
    ficha = list([['Maria', ' Gerente ', '9.000'], ['Olivia', ' CEO  ', ' 12.000'], ['Jose', ' Editor  ', ' 2.300']])
    print('==' * 30)
    print(f'{"No.": <4}{"Nome": <15}{"Cargo":<10}{"Salario":>18}')
    print('==' * 30)
    for i, a in enumerate(ficha):
        print(f'{i:<4}{a[0]:<15}{a[1]:<10}{a[2]:>18}')
    mostra = input('Escolha pelo numero do funcionario ou pelo Nome: ')
    if mostra == '0' or mostra == 'Maria':
        print(f'Funcionario:{ficha[0]} ')
    elif mostra == '1' or mostra == 'Olivia':
        print(f'Funcionario:{ficha[1]} ')
    elif mostra == '2' or mostra == 'Jose':
        print(f'Funcionario:{ficha[2]} ')



def alterar():
    ficha = list([['Maria', ' Gerente ', 9000], ['Olivia', ' CEO  ', 12000], ['Jose', ' Editor  ', 2300]])
    print('==' * 30)
    print(f'{"No.": <4}{"Nome": <15}{"Cargo":<10}{"Salario":>18}')
    print('==' * 30)

    for i, a in enumerate(ficha):
         print(f'{i:<4}{a[0]:<15}{a[1]:<10}{a[2]:>18}')
    qual = int(input('Qual funcionario: '))

    if qual == 0 or qual == 'Maria':
        qual = ficha[0][2]  # + (funcionarios[0:] + 10/100 )
        print(qual)
    elif qual == 1 or qual =='Olivia':
        qual = ficha[1][2]
        print(qual)
    elif qual == 2 or qual=='Jose':
        qual = ficha[2][2]
        #print(qual)

    alt = int(input('Alterar: \n'
                    '1- Salario \n'))
    if alt == 1:
        deseja = int(input('1- Aumentar salario \n'
                           '2- Diminuir salario '))
        if deseja == 1:
            aumento = int(input('Aumentar em:\n'
                                '1- 10%\n'
                                '2- 20%\n'
                                '3-35%\n'))
            if aumento == 1:
                resultado = qual + (qual * 10 / 100)
                print('O novo salario é de {}'.format(resultado))
            if aumento == 2:
                resultado = qual + (qual * 20 / 100)
                print('O novo salario é de {}'.format(resultado))
            if aumento == 3:
                resultado = qual + (qual * 35 / 100)
                print('O novo salario é de R${}'.format(resultado))

        elif deseja == 2:
            diminuir = int(input('Desconto: \n 1-10% \n 2- 20%'))
            if diminuir == 1:
                resultado = qual - (qual * 10 / 100)
                print('Com o desconto o salario é de R${}'.format(resultado))
            elif diminuir == 2:
                resultado = qual - (qual * 10 / 100)
                print('Com o desconto o salario é de R${}'.format(resultado))
    return


def deletar():
    ficha = list([['Maria', ' Gerente ', '9.000'], ['Olivia', ' CEO  ', ' 12.000'], ['Jose', ' Editor  ', ' 2.300']])
    print('==' * 30)
    print(f'{"No.": <4}{"Nome": <15}{"Cargo":<10}{"Salario":>18}')
    print('==' * 30)
    for i, a in enumerate(ficha):
        print(f'{i:<4}{a[0]:<15}{a[1]:<10}{a[2]:>18}')
    deseja = int(input('Digite o numero do funcionario que deseja excluir: '))
    if deseja == 0:
        print(ficha[0])
        print(deseja)
        d = int(input('Tem certeza:\n 1-Sim\n 2-Nao'))
        if d == 1:
            ficha.pop(deseja)
            # print(ficha)
            print('Funcionario deletado.')
        elif d == 2:
            print('Operação cancelada.')
    if deseja == 1:
        print(ficha[1])
        # print(ficha)
        d = int(input('Tem certeza:\n 1-Sim\n 2-Nao'))
        if d == 1:
            ficha.pop(deseja)
            # print(ficha)
            print('Funcionario deletado.')
        elif d == 2:
            print('Operação cancelada.')
    if deseja == 2:
        print('0-', ficha[2])
        # print(ficha)
        d = int(input('Tem certeza:\n 1-Sim\n 2-Nao'))
        if d == 1:
            ficha.pop(deseja)
            #print(ficha)
            print('Funcionario deletado.')
        elif d == 2:
            print('Operação cancelada.')
            return

# print(li())
