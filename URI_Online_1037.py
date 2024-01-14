lerValor = float(input());

intervaloNumero = [[0,25.0000],[25,50],[50,75],[75,100]]

for numeros in intervaloNumero:
    ini = numeros[0]
    fim = numeros[1]

    if(ini <= lerValor <= fim):
        print(f"Intervalo ({ini},{fim})")
        break