values = input()

values = values.split(" ")

a = int(values[0])
b = int(values[1])
c = int(values[2])

arr = [a, b, c]
ArrDec = sorted(arr)
for i in range (len(arr)):
    print(ArrDec[i])

print("")

for i in range (len(arr)):
    print(arr[i])


# if (a < b and a < c) and b < c:
#     print(a)
#     print(b)
#     print(c)
# elif (b < a and b < c) and c < a:
#     print(b)
#     print(c)
#     print(a)
# elif (c < a and c < b) and b < a:
#     print(c)
#     print(b)
#     print(a)