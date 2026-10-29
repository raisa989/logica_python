 
for n in range(1, 1001): #for ja conhecido, onde o i indica o ponto de partida onde as voltas são contadas e o x a delimitação de onde parar ja estabelecido anteriormente
    if n % 15 == 0: # verifica se é multiplo de 15 pelo resto da divisão, e caso seja, executa a linha debaixo
        print("FizzBuzz")
    elif n % 5 == 0:
        print("Buzz")
    elif n % 3 == 0:
        print("Fizz")
    else: # caso não atenda a condição do if
        print(n)
 