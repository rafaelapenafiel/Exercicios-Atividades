N = int(input("Número: "))

a, b = 1, 1
k = 1

while k <= N-2:
    a, b = b, a + b
    k = k + 1
print (b)
