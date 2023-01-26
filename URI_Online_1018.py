# Leia um valor inteiro. A seguir, calcule o menor número de notas 
# possíveis (cédulas) no qual o valor pode ser decomposto. 
# As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. 
# A seguir mostre o valor lido e a relação de notas necessárias.

# Entrada
# O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

# Saída
# Imprima o valor lido e, em seguida, 
# a quantidade mínima de notas de cada tipo necessárias, 
# conforme o exemplo fornecido. 
# Não esqueça de imprimir o fim de linha após cada linha, 
# caso contrário seu programa apresentará a mensagem: “Presentation Error”.
from ast import For


valorInteiro = int(input());
# Notas para decompor 100,50,20,10,5,2,1;
notasDecompor = [100,50,20,10,5,2,1];
positionArray = 0;
print(valorInteiro);

if(valorInteiro >0 & valorInteiro<1000000):
    for x in notasDecompor:
        if(valorInteiro >= x):
            calc = int(valorInteiro/x);
            print(str(calc)+" nota(s) de R$ " + str(x) + ",00");
            valorInteiro = valorInteiro - (calc*x);            
        else:
            print("0 nota(s) de R$ " + str(x) + ",00");
        positionArray+=positionArray;

