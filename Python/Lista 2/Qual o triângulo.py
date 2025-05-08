L1 = int(input("Lado 1: "))
L2 = int(input("Lado 2: "))
L3 = int(input("Lado 3: "))
if L1 > L2 + L3 or L2 > L1 + L3 or L3 > L1 + L2:
    print ('Não pode ser um triângulo')
    print ('Um dos lados é maior que a soma')
elif L1 == L2 == L3:
    print ('Triângulo Equilátero')
elif L1 == L2 or L2 == L3 or L1 == L3:
    print ('Triângulo Isósceles')
else:
    print ('Triângulo Escaleno')
