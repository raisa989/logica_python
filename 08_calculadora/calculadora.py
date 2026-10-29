from cores import *

while True: 
    print("\n" + FRENTE_MAGENTA, ESTILO_NEGRITO + "__CALCULADORA__" + RESET)
    numero1 = float (input("Digite o primeiro número: "))
    numero2 = float (input("Digite o segundo número: "))
    operador = input("Digite o operador :")


    if operador =="+":
        resultado = numero1+numero2
        print(resultado)
    elif operador =="-":
        resultado = numero1-numero2
        print(resultado)
    elif operador =="*":
        resultado = numero1*numero2
        print(resultado)
    elif operador == "/":
        if numero2 == 0:
            print("Não é possível dividir por zero")
        else:
            resultado = numero1 / numero2
            print(resultado)

    else:
        print("Operador inválido")
    

    print()