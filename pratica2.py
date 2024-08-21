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

n1 = int(input("Digite o primeiro número"))
n2 = int(input("Digite o segundo número"))
calculo = int(input("Qual é a operação que você deseja fazer?\n Para soma, digite 1\n Para subtração, digite 2\n Para divisão, digite 3\n Para multiplicação, digite 4"))

resultado = calculadora(n1, n2, calculo)
print(resultado)
