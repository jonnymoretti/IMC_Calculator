def menu(): #Utilizei esta função para poder organizar o menu e o código
    print("=== Calculadora de Índeice de Massa Corporal ===")
    print("1 - IMC/BMC - Índice de Massa Corporal")
    print("2 - LBM - Lean Body Mass")
    print("3 - IBW - Ideal Body Weight")
    print("4 - ABSI - Body Shape Index")
    print("5 - ICQ/WHR - Índice de Cintura e Quadris")
    print("6 - WHtR - Waist to height Ratio")
    print("7 - Texto explicativo dos índices")
    print("8 - Sair")

menu()
option = int(input("Escolha uma das opções (1..8): "))#Utilizei esta variável para poder escolher entre uma das opções do menu

while option != 8:#Funciona como um loop que só termina quando a variável "option" for igual a 8
    if option == 1:
        def opcao1():#Utilizei esta função para poder organizar o programa do IMC
            altura = float(input("Digite a altura em metros: "))#Defini esta variavel para poder calcular o indice
            while altura < 0: #Utilizei este loop para quando a variavel for negativa o programa voltará a perguntar até obter uma resposta válida
                while True:
                    print("Altura inválida, por favor coloque uma altura aceitável.")
                    altura = float(input("Digite a altura em metros: "))
                    if altura > 0:
                        break
            peso = float(input("Digite o peso em kg: "))#Defini esta variavel para poder calcular o indice
            while peso < 0:
                while True:
                    print("Peso inválido, por favor coloque um peso aceitável.")
                    peso = float(input("Digite o peso em kg: "))
                    if peso > 0:
                        break
            imc = peso / (altura ** 2)#Defini esta variavel para poder calcular o indice
            situacao = situacao_por_imc(imc)#Utilizei esta variavel para poder ter os valores da função mencionada abaixo
            print("Seu IMC é de {:.2f}".format(imc),)
            print(f"O que indica que você está {situacao}")

        def situacao_por_imc(imc):#Utilizei esta função para as condições que dependendo do valor da taxa irá escolher a opção correta permitindo assim descrever o resultado obtido
            if imc < 17:
                situacao="Muito Abaixo do peso"
            elif 17 <= imc < 18.49:
                situacao="Abaixo do peso"
            elif 18.49 <= imc < 24.99:
                situacao="Peso normal"
            elif 25 <= imc < 29.99:
                situacao="Acima do peso"
            elif 30 <= imc < 34.99:
                situacao="Obesidade I"
            elif 35 <= imc < 39.99:
                situacao="Obesidade II"
            else:
                situacao="Obesidade III"
            return situacao #Utilizei o "return" para poder enviar os objectos de volta ao código de chamada, no qual seria a variável "situacao"
            
        opcao1()
        print()#Utilizo este "print()" para poder pular uma linha e, tornando assim mais legível
        input("Pressione Enter para voltar ao menu")#Utilizo este "input" para definir uma chave de modo a que quando se premir a tecla Enter voltaremos ao menu inicial

    elif option == 2:
        def opcao2():#Utilizei esta função para poder organizar o programa do LBM
            idade = int(input("Digite a sua idade: "))#Variável necessária para calcularmos o índice de acordo com a idade da pessoa
            if idade <= 14:
                h = float(input("Digite a sua altura em cm: "))
                while h < 0: 
                    while True:
                        print("Altura inválida, por favor coloque uma altura aceitável.")
                        h = float(input("Digite a sua altura em cm: "))
                        if h > 0:
                            break
                p = float(input("Digite o seu peso em kg: "))
                while p < 0:
                    while True:
                        print("Peso inválido, por favor coloque um peso aceitável.")
                        p = float(input("Digite o seu peso em kg: "))
                        if p > 0:
                            break
                eECV = (0.0215*p**0.6469)*h**0.7236
                eLBM = 3.8*eECV
                PeterF = eLBM
                print("De acordo com a fórmula de Peters o teu LBM é {:.2f}".format(PeterF))
            else:
                    while True:#loop para quando o sexo for feminino ou masculino, em que o loop acaba quando escolher o sexo correto (feminino ou masculino)
                        gender = input("Digite seu género, M para masculino, F para feminino: ")
                        if gender in ["f","F"]:
                            h = float(input("Digite a sua altura em cm: "))
                            while h < 0:
                                while True:
                                    print("Altura inválida, por favor coloque uma altura aceitável.")
                                    h = float(input("Digite a sua altura em cm: "))
                                    if h > 0:
                                        break
                            p = float(input("Digite o seu peso em kg: "))
                            while p < 0:
                                while True:
                                    print("Peso inválido, por favor coloque um peso aceitável.")
                                    p = float(input("Digite o seu peso em kg: "))
                                    if p > 0:
                                        break
                            BoerLBM = (0.252*p) + (0.473*h) - 48.3
                            JamesLBM = (1.07*p) - (148*((p/h)**2))
                            HumeLBM = (0.29569*p) + (0.41813*h) - 43.2933
                            print("De acordo com a Fórmula de Boer teu LBM é {:.1f}".format(BoerLBM))
                            print("De acordo com a Fórmula de James teu LBM é {:.1f}".format(JamesLBM))
                            print("De acordo com a Fórmula de Hume teu LBM é {:.1f}".format(HumeLBM))
                            break
                        elif gender in ["m","M"]:
                            h = float(input("Digite a sua altura em cm: "))
                            while h < 0:
                                while True:
                                    print("Altura inválida, por favor coloque uma altura aceitável.")
                                    h = float(input("Digite a sua altura em cm: "))
                                    if h > 0:
                                        break
                            p = float(input("Digite o seu peso em kg: "))
                            while p < 0:
                                while True:
                                    print("Peso inválido, por favor coloque um peso aceitável.")
                                    p = float(input("Digite o seu peso em kg: "))
                                    if p > 0:
                                        break
                            BoerLBM = (0.407*p) + (0.267*h) - 19.2
                            JamesLBM = (1.1*p) - (128*((p/h)**2))
                            HumeLBM = (0.32810*p) + (0.33929*h) - 29.5336
                            print("De acordo com a Fórmula de Boer teu LBM é {:.1f}".format(BoerLBM))
                            print("De acordo com a Fórmula de James teu LBM é {:.1f}".format(JamesLBM))
                            print("De acordo com a Fórmula de Hume teu LBM é {:.1f}".format(HumeLBM))
                            break
                        else:
                            print("Digite novamente o género.")

        opcao2()
        print()
        input("Digite Enter para voltar ao menu.")
        


        
    elif option == 3:
        def opcao3():#Utilizei esta função para poder organizar o programa do IBW
            while True:#loop para quando o sexo for feminino ou masculino, em que o loop acaba quando escolher o sexo correto (feminino ou masculino)
                gender = input("Digite o seu género, M para masculino, F para feminino: ")
                if gender in ["f","F"]:
                    altura = float(input("Digite a sua altura em metros: "))
                    while altura < 0:
                        while True:
                            print("Altura inválida, por favor coloque uma altura aceitável.")
                            altura = float(input("Digite a sua altura em metros: "))
                            if altura > 0:
                                break
                    WomenIBW = 22 * ((altura - 0.1)**2)
                    print("De acordo com a Fórmula do IBW para as mulheres, o seu peso ideal em kg é: {:.2f}".format(WomenIBW))
                    break
                elif gender in ["m","M"]:
                    altura = float(input("Digite a sua altura em metros: "))
                    while altura < 0:
                        while True:
                            print("Altura inválida, por favor coloque uma altura aceitável.")
                            altura = float(input("Digite a sua altura em metros: "))
                            if altura > 0:
                                break
                    MenIBW = 22 * (altura**2)
                    print("De acordo com a Fórmula do IBW para os homens, o seu peso ideal é: {:.2f}".format(MenIBW))
                    break
                else:
                    print("Erro: Digite novamente o género.")
        opcao3()
        print()
        input("Digite Enter para voltar ao menu.")
        
        
    elif option == 4:
        def opcao4():#Utilizei esta função para poder organizar o programa do ABSI
            idade = int(input("Digite a sua idade: "))#Variavel para, não muito necessária, mas útil para sabermos a idade da pessoa
            while True:#loop para quando o sexo for feminino ou masculino, em que o loop acaba quando escolher o sexo correto (feminino ou masculino)
                genero = input("Digite o seu género, M para masculino, F para feminino: ")
                if genero in ["f","F"]:
                    altura = int(input("Digite a sua altura em cm: "))
                    while altura < 0:
                        while True:
                            print("Altura inválida, por favor coloque um peso aceitável.")
                            altura = float(input("Digite a sua altura em metros: "))
                            if altura > 0:
                                break
                    peso = float(input("Digite o seu peso em kg: "))
                    while peso < 0:
                        while True:
                            print("Peso inválido, por favor coloque uma altura aceitável.")
                            peso = float(input("Digite o seu peso em kg: "))
                            if peso > 0:
                                break
                    waist = int(input("Digite a sua Circunferência de Cintura em cm: "))
                    while waist < 0:
                        while True:
                            print("Cincunferência da cintura inválida, por favor coloque uma circunferência de cintura aceitável.")
                            waist = float(input("Digite a sua Circunferência de Cintura em metros: "))
                            if waist > 0:
                                break
                    altura = altura / 100 #Dividi a váriavel "altura" por 100 pra transformar centimetros em metros
                    BMI = peso / (altura**2)
                    WC = waist / 100 #Dividi a váriavel "waist" por 100 pra transformar centimetros em metros
                    ABSI = WC / ((BMI**(2/3))*(altura**(1/2)))
                    print(f"De acodo com a Fórmula do ABSI, o teu ABSI é :{ABSI}")
                    break
                elif genero in ["m","M"]:
                    altura = int(input("Digite a sua altura em cm: "))
                    while altura < 0:
                        while True:
                            print("Altura inválida, por favor coloque uma altura aceitável.")
                            altura = float(input("Digite a sua altura em cm: "))
                            if altura > 0:
                                break
                    peso = float(input("Digite o seu peso em kg: "))
                    while peso < 0:
                        while True:
                            print("Peso inválido, por favor coloque um peso aceitável.")
                            peso = float(input("Digite o seu peso em kg: "))
                            if peso > 0:
                                break
                    waist = int(input("Digite a sua Circunferência de Cintura em cm: "))
                    while waist < 0:
                        while True:
                            print("Circunferência da Cintura inválida, por favor coloque uma circunferência de cintura aceitável.")
                            waist = float(input("Digite a sua Circunferência da Cintura em cm: "))
                            if waist > 0:
                                break
                    altura = altura / 100
                    BMI = peso / (altura**2)
                    WC = waist / 100
                    ABSI = WC / ((BMI**(2/3))*(altura**(1/2)))
                    print(f"De acodo com a Fórmula do ABSI, para homens, o teu ABSI é :{ABSI}")
                    break
                else:
                    print("Género inválido, digite novamente.")
        opcao4()
        print()
        input("Pressione Enter para voltar ao menu.")


    elif option == 5:
        def opcao5():#Utilizei esta função para poder organizar o programa do ICQ
            while True:#loop para quando o sexo for feminino ou masculino, em que o loop acaba quando escolher o sexo correto (feminino ou masculino)
                gender = input("Digite o seu género, M para masculino, F para feminino: ")
                if gender in ["f","F"]:
                    waist = int(input("Digite o tamanho da sua Cintura em cm: "))
                    while waist < 0:
                        while True:
                            print("Circunferência da cintura inválida, por favor coloque uma circunferência de cintura aceitável.")
                            waist = float(input("Digite a sua Circunferência da Cintura em cm: "))
                            if waist > 0:
                                break
                    quadril = int(input("Digite o tamanho do seu Quadril em cm: "))
                    while quadril < 0:
                        while True:
                            print("Tamanho do quadril inválido, por favor coloque um tamanho de quadril aceitável.")
                            quadril = float(input("Digite o tamannho do seu Quadril em cm: "))
                            if quadril > 0:
                                break
                    ICQ = waist / quadril
                    if ICQ <= 0.80: #Utilizei estas repitições para as condições que dependendo do valor da taxa irá escolher a opção correta permitindo assim descrever o resultado obtido
                        print(f"De acordo com o ICQ o seu risco de saúde é Baixo, pois o seu ICQ, para as mulheres é: {ICQ}")
                    elif 0.81 <= ICQ <= 0.85:
                        print(f"De acordo com o ICQ o seu risco de saúde é Moderado pois o seu ICQ, para as mulheres é: {ICQ}")
                    elif ICQ >= 0.86:
                        print(f"De acordo com o ICQ o seu risco de saúde é Alto pois o seu ICQ, para as mulheres é: {ICQ}")
                        break
                elif gender in ["m","M"]:
                    waist = int(input("Digite o tamanho da sua Cintura em cm: "))
                    while waist < 0:
                        while True:
                            print("Circunferência da cintura inválida, por favor coloque uma circunferência de cintura aceitável.")
                            waist = float(input("Digite o tamanho da sua Cintura em cm: "))
                            if waist > 0:
                                break
                    quadril = int(input("Digite o tamanho do seu Quadril em cm: "))
                    while quadril < 0:
                        while True:
                            print("Tamnaho do quadril inválido, por favor coloque um tamanho de quadril aceitável.")
                            quadril = float(input("Digite o tamanho do seu Quadril em cm: "))
                            if quadril > 0:
                                break
                    ICQ = waist / quadril
                    if ICQ <= 0.95:
                        print(f"De acordo com o ICQ o seu risco de saúde é Baixo, pois o seu ICQ, para os homens é: {ICQ}")
                    elif 0.96 <= ICQ < 1.0:
                        print(f"De acordo com o ICQ o seu risco de saúde é Moderado, pois o seu ICQ, para os homens é: {ICQ}")
                    elif ICQ >= 1.0:
                        print(f"De acordo com o ICQ o seu risco de saúde é Alto, pois o seu ICQ, para os homens é: {ICQ}")
                        break
                else:
                    print("Género inválido, digite novamente.")
        opcao5()
        print()
        input("Pressione Enter para voltar ao menu.")

                    
    elif option == 6:
        def opcao6():#Utilizei esta função para poder organizar o programa do WHtR
            idade = int(input("Digite a sua idade: "))#Utilizei esta variável para fazer duas opções de programa, para jovens (menores de 15) e adultos (maiores que 15)
            if idade < 15:
                waistcin = int(input("Digite a sua Circunferência de Cintura em cm: "))
                while waistcin < 0:
                        while True:
                            print("Circunferência da cintura inválida, por favor coloque uma circunferência de cintura aceitável.")
                            waistcin = float(input("Digite a sua Circunferência da Cintura em cm: "))
                            if waistcin > 0:
                                break
                altura = int(input("Digite a sua altura em cm: "))
                while altura < 0:
                        while True:
                            print("Altura inválida, por favor coloque uma altura aceitável.")
                            altura = float(input("Digite a sua altura em cm: "))
                            if altura > 0:
                                break
                WHR = waistcin / altura
                if WHR <= 0.34: #Utilizei estas repitições para as condições que dependendo do valor da taxa irá escolher a opção correta permitindo assim descrever o resultado obtido
                    print(f"O seu WHtR é: {WHR}, em que de acordo com o WHtR crianças estás extremamente magro(a).")
                if 0.35 <= WHR <= 0.45:
                    print(f"O seu WHtR é: {WHR}, em que de acordo com o WHtR para crianças estás magro(a).")
                if 0.46 <= WHR <= 0.51:
                    print(f"O seu WHtR é: {WHR}, em que de acordo com o WHtR para crianças estás saudável.")
                if 0.52 <= WHR <= 0.63:
                    print(f"O seu WHtR é: {WHR}, em que de acordo com o WHtR para crianças estás acima do peso.")
                if WHR >= 0.64:
                    print(f"O seu WHtR é: {WHR}, em que de acordo com o WHtR para crianças estás obeso(a).")
            else:
                while True:#loop para quando o sexo for feminino ou masculino, em que o loop acaba quando escolher o sexo correto (feminino ou masculino)
                    gender = input("Digite o seu género, M para masculino, F para feminino: ")
                    if gender in ["f","F"]:
                        waist = int(input("Digite a sua Circunferência de Cintura em cm: "))
                        while waist < 0:
                            while True:
                                print("Circunferência da cintura inválida, por favor coloque uma circunferência de cintura aceitável.")
                                waist = float(input("Digite a sua Circunferência da Cintura em cm: "))
                                if waist > 0:
                                    break
                        altura = int(input("Digite a sua altura em cm: "))
                        while altura < 0:
                            while True:
                                print("Altura inválida, por favor coloque uma altura aceitável.")
                                altura = float(input("Digite a sua altura em cm: "))
                                if altura > 0:
                                    break
                        WWHR = waist / altura
                        if WWHR <= 0.34: #Utilizei estas repitições para as condições que dependendo do valor da taxa irá escolher a opção correta permitindo assim descrever o resultado obtido
                            print(f"O seu WHtR é: {WWHR}, em que de acordo com o WHtR para mulheres adultas estás extremamente magra.")
                        if 0.35 <= WWHR <= 0.41:
                            print(f"O seu WHtR é: {WWHR}, em que de acordo com o WHtR para mulheres adultas estás magra.")
                        if 0.42 <= WWHR <= 0.48:
                            print(f"O seu WHtR é: {WWHR}, em que de acordo com o WHtR para mulheres adultas estás saudável.")
                        if 0.49 <= WWHR <= 0.53:
                            print(f"O seu WHtR é: {WWHR}, em que de acordo com o WHtR para mulheres adultas estás acima do peso.")
                        if 0.54 <= WWHR <= 0.57:
                            print(f"O seu WHtR é: {WWHR}, em que de acordo com o WHtR para mulheres adultas estás muito acimo do peso.")
                        if WWHR >= 0.58:
                            print(f"O seu WHtR é: {WWHR}, em que de acordo com o WHtR para mulheres adultas estás obesa.")
                            break
                    elif gender in ["m","M"]:
                        waist = int(input("Digite a sua Circunferência de Cintura em cm: "))
                        while waist < 0:
                            while True:
                                print("Circunferência da cintura inválida, por favor coloque uma circunferência de cintura aceitável.")
                                waist = float(input("Digite a sua Circunferência da Cintura em cm: "))
                                if waist > 0:
                                    break
                        altura = int(input("Digite a sua altura em cm: "))
                        while altura < 0:
                            while True:
                                print("Altura inválida, por favor coloque uma altura aceitável.")
                                altura = float(input("Digite a sua altura em cm: "))
                                if altura > 0:
                                    break
                        MWHR = waist / altura
                        if MWHR <= 0.34:
                            print(f"O seu WHtR é: {MWHR}, em que de acordo com o WHtR para homens adultos estás extremamente magro.")
                        if 0.35 <= MWHR <= 0.42:
                            print(f"O seu WHtR é: {MWHR}, em que de acordo com o WHtR para homens adultos estás magro.")
                        if 0.43 <= MWHR <= 0.52:
                            print(f"O seu WHtR é: {MWHR}, em que de acordo com o WHtR para homens adultos estás saudável.")
                        if 0.53 <= MWHR <= 0.57:
                            print(f"O seu WHtR é: {MWHR}, em que de acordo com o WHtR para homens adultos estás acima do peso.")
                        if 0.58 <= MWHR <= 0.62:
                            print(f"O seu WHtR é: {MWHR}, em que de acordo com o WHtR para homens adultos estás muito acimo do peso.")
                        if MWHR >= 0.63:
                            print(f"O seu WHtR é: {MWHR}, em que de acordo com o WHtR para homens adultos estás obeso.")
                            break
                    else:
                        print("Erro: Digite novamente o género.")
        opcao6()
        print()
        input("Pressione Enter para voltar ao menu.")


    elif option == 7:
        def texto_explicativo():#Utilizei esta função para poder organizar o programa do texto explicativo
            print("Explicação de cada índice")#Utilizo este "print()" para quando abrir o ficheiro aparecer o texto dentro dos parenteses
            f = open('readme.txt',"r")#Utilzo esta variável para poder abrir o ficheiro de texto
            line = f.readline()#Utilizo esta variável para poder ler as linhas do ficheiro de texto
            for line in f:
                print(line,end='')
            f.close #Utilizo este comando para fechar o ficheiro de texto
        texto_explicativo()
        print()
        input("Pressione Enter para voltar ao menu.")


    else: #Utilizo este "else" para quando a opção digitada não estiver entre as recomendadas pedem-te para digitar novamente as opções
        print("Erro: Opção Inválida! Digite opção entre 1 e 8") 
    print()
    menu()
    option = int(input("Escolha uma das opções (1..8): "))#Utilizo esta variavel depois da repetiçao do else

print("Obrigado por utilizar o nosso programa. Até Logo!")