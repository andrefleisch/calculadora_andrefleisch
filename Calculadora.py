operacao = 1

while operacao != 0:
    operacao = int(input(f"----| Menu Calculadora |---- \n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n0 - Sair:\nEscolha sua operação: "))
    if operacao > 4:
         print("Operação inválida")
         continue
    elif operacao == 0:
        print("Encerrando a calculadora...")
        break
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo numero: "))
    if operacao == 1:
        print(f"{n1} + {n2} = {n1 + n2} ")
    elif operacao == 2:
            print(f"{n1} - {n2} = {n1 - n2}")
    elif operacao == 3:
        print(f"{n1} * {n2} = {n1*n2}")
    elif operacao == 4:
        print(f"{n1} ÷ {n2} = {n1/n2}")

    
    







    