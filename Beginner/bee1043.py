values = input()

values = values.split(" ")

a = float(values[0])
b = float(values[1])
c = float(values[2])

if a+b > c and b+c > a and c+a > b:
    perimeter = a+b+c
    print("Perimetro =",format(perimeter, ".1f"))
else:
    area = 0.5 * (a + b) * c
    print("Area =",format(area,".1f"))


