# Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

# Entrada
# Quatro números inteiros A, B, C e D.

# Saída
# Mostre a respectiva mensagem após a validação dos valores.


valores = str(input())
if(valores != ''):
    valoresSplit = valores.split()

    A = int(valoresSplit[0])
    B = int(valoresSplit[1])
    C = int(valoresSplit[2])
    D = int(valoresSplit[3])

    SomaCD = C+D
    SomaAB = A+B
    CisPar = True if C % 2 == 0 else False
    DisPar = True if D%2 == 0 else False
    CDisPositive = True if C > 0 and D > 0 else False
    AIsPar = True if A%2 ==0 else False


    if(B > C and D > A and (SomaCD > SomaAB)  and CDisPositive and AIsPar):
        print("Valores aceitos")
    else:
        print("Valores nao aceitos")