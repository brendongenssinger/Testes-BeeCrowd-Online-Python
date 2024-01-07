# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

# Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

# Entrada
# O arquivo de entrada contém um valor inteiro.

# Saída
# Imprima a saída conforme exemplo fornecido.


valorDias = int(input());
ANO = 0;
MES = 0;
DIAS = 0;

if(valorDias > 365):    
    ANO = int(valorDias/365);
    valorDias = valorDias - (365*ANO);  
if(valorDias >= 30):
    MES = int(valorDias/30);
    valorDias = valorDias - (30*MES);
if(valorDias < 30):
    DIAS = int(valorDias);

print(str(ANO)+" ano(s)\n"+str(MES)+" mes(es)\n"+str(DIAS)+" dia(s)");
