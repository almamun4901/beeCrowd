values = input()

values = values.split(" ")
# print(values)

a = int(values[0])
b = int(values[1])
c = int(values[2])
d = int(values[3])

if (b > c and d > a) and (c + d > a + b) and a % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")

