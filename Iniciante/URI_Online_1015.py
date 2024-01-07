# Leia os quatro valores correspondentes aos eixos x e y de dois pontos 
# quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles,
# mostrando 4 casas decimais após a vírgula, segundo a fórmula:

import math


p1 = list(map(float,input().split(' ')));
p2 = list(map(float,input().split(' ')));

x1 = p1[0];
x2 = p2[0];
y1 = p1[1];
y2 = p2[1];0


distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2);

print("{:.4f}".format(distancia));

