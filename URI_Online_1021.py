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



# Huw David Wright18:20
# we can chat also
# Você18:20
# okk
# Huw David Wright18:20
# My name is Dave
# you can call me Dave
# my class is formal and relaxed
# Huw David Wright18:22
# No it like a classroom
# I don´t teach like that
# I teach in a friendly atomsphere
# Huw David Wright18:23
# Please can you introduct yourself to me
# introduce
# what do you work wth computers
# Huw David Wright18:24
# stopyou one moment
# now i want you to take a deep breathe and breath in
# Huw David Wright18:26
# relaxed
# no is my class to make you stressed
# Huw David Wright18:32
# What do you want to do with your future
# like your job
# Huw David Wright18:37
# You need a dictionary
# Oxford Dictionary
# Huw David Wright18:38
# will tell you the meaning of the words
# Huw David Wright18:41
# Nice to meet you Nice to meet you too
# Informal Greeting
# Huw David Wright18:42
# Informal Greetings
# He is
# She is 
# This is
# Huw David Wright18:43
# Formal Greetings
# I present........
# I Introduce.......
# Huw David Wright18:46
# I present to you
# I Introduce to you my friends
# Huw David Wright18:47
# Is your name Brendon?
# Huw David Wright18:49
# Yes, it is
# Huw David Wright18:50
# Is your name Erik?
# Huw David Wright18:51
# No,, it isn´t
# Are you Fernado?
# Yes, I am
# Huw David Wright18:52
# Are you Errik?
# No, I´m not
# Huw David Wright18:58
# Plural = more than one
# Greetings
# Hello!
# Hii!
# Good morning
# Huw David Wright18:59
# Good afternoon
# How are you
# Goodbye
# Bye
# See you = tomorrow/later
# Huw David Wright19:00
# Have a nce day
# Good Night
# Huw David Wright19:03
# I work Monday til Saturday
# teaching
# 9am til 2pm and 4pm to 7pm
# Huw David Wright19:05
# Ok next Monday
# 4pm
# Huw David Wright19:08
# next class i will charge $5.10
# you get for half price
# normally it costs $10.20
# Huw David Wright19:09
# you pay into my Paypal
# Huw David Wright19:11
# i have homework for you 
# to show me next monday


