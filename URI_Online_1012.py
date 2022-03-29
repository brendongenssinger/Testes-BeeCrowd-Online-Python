# Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. 
# Em seguida, calcule e mostre:
# a) a área do triângulo retângulo que tem A por base e C por altura.
# b) a área do círculo de raio C. (pi = 3.14159)
# c) a área do trapézio que tem A e B por bases e C por altura.
# d) a área do quadrado que tem lado B.
# e) a área do retângulo que tem lados A e B.

#input






print("Informe o número")
READVALUES = str(input());

A = float(READVALUES.split(' ')[0]);
B = float(READVALUES.split(' ')[1]);
C = float(READVALUES.split(' ')[2]);

AREATRIANGULO = (C*A)/2;
AREACIRCULODERAIO = 3.14159*C**2;
AREATRAPEZIO = ((A+B)*C)/2;
AREAQUADRADO = B**2
AREARETANGULO = A*B;

print("TRIANGULO: {:.3f}".format(round(AREATRIANGULO,3)));
print("CIRCULO: {:.3f}".format(round(AREACIRCULODERAIO,3)));
print("TRAPEZIO: {:.3f}".format(round(AREATRAPEZIO,3)));
print("QUADRADO: {:.3f}".format(round(AREAQUADRADO,3)));
print("RETANGULO: {:.3f}".format(round(AREARETANGULO,3)));

