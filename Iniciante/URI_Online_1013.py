# Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem 
# “eh o maior”. Utilize a fórmula:

# Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

# Entrada
# O arquivo de entrada contém três valores inteiros.

# Saída
# Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

#input




#print("Informe o número")
def parseInt(number):
    return int(number)

_readvalues = input();

numbersInt = list(map(parseInt,_readvalues.split(' ')));
A=numbersInt[0];
B=numbersInt[1];
C=numbersInt[2];

MAIORAB = (numbersInt[0]+numbersInt[1]+abs(numbersInt[0]-numbersInt[1]))/2;
if(MAIORAB > C):
    print(str(int(MAIORAB)) + " eh o maior");
else:
    print(str(C) + " eh o maior");


