n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))
if n1 > n2 and n1 > n3:
    print (f'O maior deles é {n1} ')
elif n2 > n1 and n2 > n3:
    print (f' O maior número é {n2} ')
elif n3 > n1 and n3 > n2:
    print (f' O maior número é {n3} ')

if n1 < n2 and n1 < n3:
    print (f'O menor deles é {n1} ')
elif n2 < n1 and n2 < n3:
    print (f'O menor deles é {n2} ')
elif n3 < n1 and n3 < n2:
    print (f'O menor deles é {n3} ')
