# Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

# Entrada
# O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

# Saída
# Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

# Obs: Utilize ponto (.) para separar a parte decimal.

# 576.73

# NOTAS:
# 5 nota(s) de R$ 100.00
# 1 nota(s) de R$ 50.00
# 1 nota(s) de R$ 20.00
# 0 nota(s) de R$ 10.00
# 1 nota(s) de R$ 5.00
# 0 nota(s) de R$ 2.00
# MOEDAS:
# 1 moeda(s) de R$ 1.00
# 1 moeda(s) de R$ 0.50
# 0 moeda(s) de R$ 0.25
# 2 moeda(s) de R$ 0.10
# 0 moeda(s) de R$ 0.05
# 3 moeda(s) de R$ 0.01


# 4.00

# NOTAS:
# 0 nota(s) de R$ 100.00
# 0 nota(s) de R$ 50.00
# 0 nota(s) de R$ 20.00
# 0 nota(s) de R$ 10.00
# 0 nota(s) de R$ 5.00
# 2 nota(s) de R$ 2.00
# MOEDAS:
# 0 moeda(s) de R$ 1.00
# 0 moeda(s) de R$ 0.50
# 0 moeda(s) de R$ 0.25
# 0 moeda(s) de R$ 0.10
# 0 moeda(s) de R$ 0.05
# 0 moeda(s) de R$ 0.01


valorFloat = float(input());
valorInteiro = int(valorFloat);
valorMoeda = float("{:.2f}".format(valorFloat - valorInteiro));

# Notas para decompor 100,50,20,10,5,2,1;
notasDecompor = [100,50,20,10,5,2];
moedasDecompor = [1,0.50,0.25,0.10,0.05,0.01];
positionArray = 0;
print("NOTAS :");

if(valorInteiro >0 & valorInteiro<1000000.00):
    for x in notasDecompor:
        if(valorInteiro >= x):
            calc = int(valorInteiro/x);
            print(str(calc)+" nota(s) de R$ " + str(x) + ",00");
            valorInteiro = valorInteiro - (calc*x);            
        else:
            print("0 nota(s) de R$ " + str(x) + ",00");
                    
if(valorMoeda >=0.1 and valorMoeda<1000000.00):
    for x in moedasDecompor:
        if(valorMoeda >= x):
            valorMoeda = valorMoeda - x;
            print(str(calc)+" moeda(s) de R$ " + str(x) );
        else:
            print("0 moeda(s) de R$ " + str(x));              


