import operadores as op
import sys

while True:
    print("\n===== BEM VINDO A CALCULADORA =====\n")

    print("Veja a lista e depois insira que tipo de operação você quer fazer\n")

    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")
    print("6 - Raiz quadrada")
    print("7 - Porcentagem")
    print("0 - Sair\n")

    #  Este try Verifica a variável "operacao"
    try:
        operacao = int(input("Qual operação você deseja: "))

        if operacao == 0:
            print("\nEncerrando o programa...")
            sys.exit()

        if operacao == 1:
            # Verifica a variável "numero1"
            try:
                numero1 = float(input("\nInsira o primeiro número para a soma: "))
            except ValueError:
                print("Valor errado! Tente novamente.\n")
                continue

            #  Verifica a variável "numero2"
            try:
                numero2 = float(input("Insira o segundo número: "))
            except ValueError:
                print("Valor errado! Tente novamente.\n")
                continue
            op.soma(numero1, numero2)

        elif operacao == 2:
            # Verifica a variável "numero1"
            try:
                numero1 = float(input("\nInsira o primeiro número para a subtração: "))
            except ValueError:
                print("Valor errado! Tente novamente.\n")
                continue

            #  Verifica a variável "numero2"
            try:
                numero2 = float(input("\nInsira o segundo número: "))
            except ValueError:
                print("Valor errado! Tente novamente.\n")
                continue
            op.sub(numero1, numero2)

        elif operacao == 3:
            # Verifica a variável "numero1"
            try:
                numero1 = float(
                    input("\nInsira o primeiro número para a multiplicação: ")
                )
            except ValueError:
                print("Valor errado! Tente novamente.\n")
                continue

            #  Verifica a variável "numero2"
            try:
                numero2 = float(input("Insira o multiplicador: "))
            except ValueError:
                print("Valor errado! Tente novamente.\n")
                continue
            op.multi(numero1, numero2)

        elif operacao == 4:
            # Verifica a variável "numero1"
            try:
                numero1 = float(input("\nInsira o numerador: "))
            except ValueError:
                print("Valor errado! Tente novamente.\n")
                continue

            #  Verifica a variável "numero2"
            try:
                numero2 = float(input("Insira o denominador: "))
            except ValueError:
                print("Valor errado! Tente novamente.\n")
                continue
            op.div(numero1, numero2)

        elif operacao == 5:
            # Verifica a variável "numero1"
            try:
                numero1 = float(input("\nInsira a base da potência: "))
            except ValueError:
                print("Valor errado! Tente novamente.\n")
                continue

            #  Verifica a variável "numero2"
            try:
                numero2 = float(input("Insira o expoente da potência: "))
            except ValueError:
                print("Valor errado! Tente novamente.\n")
                continue
            op.potencia(numero1, numero2)

        elif operacao == 6:
            # Verifica a variável "numero1"
            try:
                numero1 = float(input("\nInsira o índice da raíz: "))
            except ValueError:
                print("Valor errado! Tente novamente.\n")
                continue

            #  Verifica a variável "numero2"
            try:
                numero2 = float(input("Insira o número que deseja obter a raíz: "))
            except ValueError:
                print("Valor errado! Tente novamente.\n")
                continue
            op.raiz(numero1, numero2)

        elif operacao == 7:
            # Verifica a variável "numero1"
            try:
                numero1 = float(input("\nInsira o número inteiro: "))
            except ValueError:
                print("Valor errado! Tente novamente.\n")
                continue

            #  Verifica a variável "numero2"
            try:
                numero2 = float(input("Insira a porcentagem (sem o %): "))
            except ValueError:
                print("Valor errado! Tente novamente.\n")
                continue
            op.porcent(numero1, numero2)

        else:
            print("Número inserido pelo usuário inválido, tente novamente com outro número válido.")
            continue

        while True:
            perguntaFinal = input("\nQuer fazer outra conta? (s/n) ").lower()
            
            if perguntaFinal == "s":
                break
            elif perguntaFinal == "n":
                print("\nEncerrando o programa...")
                sys.exit()
            else:
                print("\nOpção inválida, digite s ou n")

    except ValueError:
        print("\nValor errado inserido, tente novamente e insira um número.\n")
