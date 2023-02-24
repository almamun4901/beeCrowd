values = input()

values = values.split(" ")

a = float(values[0])
b = float(values[1])
c = float(values[2])

newArr = [a, b, c]
newArr.sort(reverse=True)

a = newArr[0]
b = newArr[1]
c = newArr[2]

if a > 0 and b > 0 and c > 0:
    if a >= b + c:
        print("NAO FORMA TRIANGULO")
    elif a * a == b * b + c * c:
        print("TRIANGULO RETANGULO")
    elif a * a > b * b + c * c:
        print("TRIANGULO OBTUSANGULO")
    elif a * a < b * b + c * c:
        print("TRIANGULO ACUTANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    if (a == b and c != a and c != b) or (b == c and a != b and a != c)  or (c == a and b != c and b != a):
        print("TRIANGULO ISOSCELES")