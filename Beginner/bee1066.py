a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

countPos = 0
countEven = 0
countNeg = 0
countOdd = 0

array = [a,b,c,d,e]

for i in range (0, len(array)):
    if array[i] % 2 == 0:
        countEven = countEven + 1

    if array[i] % 2 != 0:
        countOdd = countOdd + 1

    if array[i] > 0:
        countPos = countPos + 1

    if array[i] < 0:
        countNeg = countNeg + 1

print(countEven, "valor(es) par(es)")
print(countOdd, "valor(es) impar(es)")
print(countPos, "valor(es) positivo(s)")
print(countNeg, "valor(es) negativo(s)")
