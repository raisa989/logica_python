from cores import *

def somarmultiplosnumeros (numeros): #def	Palavra reservada (fixa do Python) para Criar uma função.
    return sum(numeros) #return Palavra reservada: Devolve um resultado de uma função.
            #O sum() já existe no Python. É uma função nativa, ou seja, você não precisa criá-la.
            #numeros: Nome que eu escolho para o parâmetro. Poderia ser lista, valores...

def multiplicarmultiplosnumeros(numeros):
    resultado = 1

    for numero in numeros: #FOR (para cada) número que estiver IN (dentro) da lista de números, faça alguma coisa.
        resultado = resultado * numero
        
    return resultado

def ehinteiro(numero): 
    if isinstance(numero, int): #if = verifica uma condição
        return True 
    #5(int) e 5.0(float) matematicamente, os dois representam o mesmo número: cinco
    elif isinstance(numero, float): #elif = verifica outra condição, se a anterior não foi atendida
        return numero.is_integer()

    else: #else = executa quando nenhuma das condições anteriores foi atendida
        return False # 5.7


def ehpar(numero): #Essa função aproveita a função anterior!
    if ehinteiro(numero) and numero % 2 == 0: #numero % 2 == 0 verifica se a divisão por 2 não deixa resto.
        return True

    return False

def ler_numeros():
    entrada = input("Digite os números separados por vírgula: ")

    numeros = [
        float(numero.strip()) for numero in entrada.split(",") 
        #strip() = limpa os espaços das pontas.
        #split() = separa.
    ]

    return numeros
#Até aqui, criamos as ferramentas, mas ainda precisamos de uma maneira de utilizá-las

#Agora vamos transformar as funções em uma calculadora interativa
while True:
    print("\n")
    print(FRENTE_AZUL +ESTILO_NEGRITO + ESTILO_PISCANTE+ "╔═══════════════╗" + RESET)
    print(FRENTE_AZUL+ ESTILO_NEGRITO + ESTILO_PISCANTE+"║  CALCULADORA  ║" + RESET)
    print(FRENTE_AZUL + ESTILO_NEGRITO +ESTILO_PISCANTE+"╚═══════════════╝" + RESET)
    print("1➜  Somar vários números")
    print("2➜  Multiplicar vários números")
    print("3➜  Verificar se um número é par e inteiro")
    print("4➜  Verificar se um número é inteiro")
    print("0➜  Encerrar")
    print()
    opcao = input(FRENTE_MAGENTA_CLARO+"Digite sua opção: "+RESET)

    try:
        if opcao == "1":
            numeros = ler_numeros()
            resultado = somarmultiplosnumeros(numeros)
            print("\n" + FRENTE_VERDE + ESTILO_NEGRITO +
      "✓ RESULTADO: " + str(resultado) + RESET)

        elif opcao == "2":
            numeros = ler_numeros()
            resultado = multiplicarmultiplosnumeros(numeros)
            print("\n" + FRENTE_VERDE + ESTILO_NEGRITO +
      "✓ RESULTADO: " + str(resultado) + RESET)

        elif opcao == "3":
            numero = float(input("Digite um número: "))
            print("\n" + FRENTE_CIANO + ESTILO_NEGRITO +
            "✓ É PAR E INTEIRO?: " + str(ehpar(numero)) + RESET)

        elif opcao == "4":
            numero = float(input("Digite um número: "))
            print("\n" + FRENTE_CIANO + ESTILO_NEGRITO +
            "✓ É INTEIRO? "+ str(ehinteiro(numero)) + RESET)

        elif opcao == "0":
            print("Calculadora encerrada!")
            break

        else:
            print(FRENTE_VERMELHO+"Opção inválida. Tente novamente." + RESET)

    except ValueError:
        print("Entrada inválida. Digite apenas números válidos.")