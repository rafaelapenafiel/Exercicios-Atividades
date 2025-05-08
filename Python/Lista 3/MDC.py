N1 = int(input("Número 1: "))
N2 = int(input("Número 2: "))
while N1 % N2 !=0:
    N1, N2 = N2, N1%N2
print (f'mdc = {N2} ')
