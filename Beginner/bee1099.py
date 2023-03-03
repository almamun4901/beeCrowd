number = int(input())

for i in range (number):
    x = input()
    x = x.split(" ")

    x[0] = int(x[0])
    x[1] = int(x[1])

    if x[1] > x[0]:
        a = x[0]
        b = x[1]
    else:
        a = x[1]
        b = x[0]

    if a == b:
        print(a-b)
    elif a+1 == b:
        print("0")
    else:
        total = 0
        for j in range(a + 1, b):
            if j % 2 != 0:
                total = total + j

        print(total)

