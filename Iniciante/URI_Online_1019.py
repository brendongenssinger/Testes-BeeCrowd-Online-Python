# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica,
#  e informe-o expresso no formato horas:minutos:segundos.

# Entrada
# O arquivo de entrada contém um valor inteiro N.

# Saída
# Imprima o tempo lido no arquivo de entrada (segundos), 
# convertido para horas:minutos:segundos, conforme exemplo fornecido.


valorSeconds = int(input());
H = 0;
M = 0;
S = 0;

if(valorSeconds > 3599):
    H = int((valorSeconds/3600));
    valorSeconds = valorSeconds - (H*60*60);    
if(valorSeconds>=60):
    M = int(valorSeconds/60);
    valorSeconds = valorSeconds - (M *60);
if(valorSeconds < 60):
    S = valorSeconds;

print(str(H)+":"+str(M)+":"+str(S));

