
login = []
senha = []
funcionarios = ['Pedro' , 'Ana'   , 'Carlos', 'Maria Clara', 'João Antonio']
salarios     = [ 3470.00,  2200.00,  3970.34,  7450.23     ,  5677.33 ]

while True:

    escolha = input('''   
    MENU
    1- Cadastrar Login e Senha
    2- Aumento de 10%
    3- Relatório
    4- Cadastrar Funcionário
    Escolha: ''')

    if escolha == '1':

        nome = input("Cadastre seu login: ")

        if nome in login:
            input("Funcionário já cadastrado.")
            continue

        elif nome in funcionarios:
            login.append(nome)
                
        else:
            input("Funcionário não cadastrado.")
            continue

        secret = input("Cadastre sua senha: ")
        senha.append(secret)
        
    if escolha == '2':

        nome = input("Login: ")

        if nome not in login:
            input("Funcionário não cadastrado.")
            continue

        else:
            pass

        for x in range (len(login)):

            if nome == login[x]:

                secret = input("Senha: ")

                if secret == senha[x]:
                    pass
                        
                else:
                    input("Senha incorreta.")
                    continue

            else:
                continue

            input("Aumentando salários abaixo da média em 10%...")

            media = sum(salarios)/len(salarios)

            for x in range (len(salarios)):

                if salarios[x] < media:

                    salarios[x] = salarios[x]*0.1 + salarios[x]

                else:
                    continue
        
    if escolha == '3':

        nome = input("Login: ")

        if nome not in login:
            input("Funcionário não cadastrado.")
            continue

        else:
            pass

        for x in range (len(login)):

            if nome == login[x]:

                secret = input("Senha: ")

                if secret == senha[x]:
                    pass
                        
                else:
                    input("Senha incorreta.")
                    continue

            else:
                continue

            print()
            print("Relatório:")
            print()

            for x in range (len(funcionarios)):

                print(funcionarios[x],"-",salarios[x])

            print()
            input()
        
    if escolha == '4':

        novoNome = input("Insira seu nome: ")
        funcionarios.append(novoNome)

        while True:
        
            try:
            
                novoSal = float(input("Insira seu salário: "))
                salarios.append(novoSal)
                break

            except:
                input("Valor inválido.")
                continue
