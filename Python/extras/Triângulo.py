a = int(input("Lado 1: "))
b = int(input("Lado 2: "))
c = int(input("Lado 3: "))

if a == b == c:
    print ("Triângulo Equilátero")

elif a == b or b == c or c == a:
    print ("Triângulo Isosceles")

else:
    print ("Triângulo Escaleno")
