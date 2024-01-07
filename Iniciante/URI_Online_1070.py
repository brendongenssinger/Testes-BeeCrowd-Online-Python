#Seis Números Ímpares.

#Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.



X = int(input());

if(X % 2 == 0):
    X = X +1;
    print(str(X));
    for i in range(0,5):
        X = X + 2;
        print(str(X));



print();
