import math;

def bhaskara(a, b, c):
    delta = b**2 - 4*a*c

    if delta < 0:
        return "Impossivel calcular"
    elif delta == 0:
        x = -b / (2*a)
        x = "{:.5f}".format(x)
        return f"R1 = {x}\nR2 = {x}"
    else:
        if(A <=0):
            return "Impossivel calcular"
        
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        x1 = "{:.5f}".format(x1)
        x2 = "{:.5f}".format(x2)
        return f"R1 = {x1}\nR2 = {x2}"
    

valores = input();
valores = valores.split(" ");
A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

resultado = bhaskara(A,B,C)
print(resultado);
