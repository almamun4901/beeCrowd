import math

values = input()

values = values.split(" ")

a = float(values[0])
b = float(values[1])
c = float(values[2])

root_value = b*b - (4 * a * c)

if a == 0 or root_value < 0:
    print("Impossivel calcular")
else:
    r1 = (-b + math.sqrt(root_value))/ (2*a)
    r2 = (-b - math.sqrt(root_value))/ (2*a)
    print("R1 =",format(r1, ".5f"))
    print("R2 =",format(r2, ".5f"))