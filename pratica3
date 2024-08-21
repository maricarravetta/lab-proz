def calculadora(n1, n2, calculo):
    if(calculo == 1):
        return n1 + n2
    elif (calculo == 2):
        return n1 - n2
    elif (calculo == 3):
        return n1 / n2
    elif (calculo == 4):
        return n1 * n2
    else:
        return 0
    
execucao = True

while (execucao == True):
    print("Escolha a operação matemática que quer realizar:\n Para soma, digite 1\n Para subtração, digite 2\n Para divisão, digite 3\n Para multiplicação, digite 4")
    calculo = int(input())

    if (calculo < 0) or (calculo >4):
        print("Esta opção não existe. Por favor, apresente outra escolha.")
    elif (calculo ==0):
        execucao = False
    else:
        print("Digite o primeiro número")
        n1 = int(input())
        print("Digite o segundo número")
        n2 = int(input())

        resultado = calculadora(n1, n2, calculo)

        print("O resultado da sua conta é de:", resultado)
