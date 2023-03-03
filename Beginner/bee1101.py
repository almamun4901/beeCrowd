takeInput = True

while takeInput:
    value = input()
    value = value.split(" ")

    m = int(value[0])
    n = int(value[1])

    if m == 0 or n == 0:
        takeInput = False
        break

    sum = 0
    for i in range(n, m+1):
        sum = sum + i
        print(i, end=" ")

    print("Sum=",end="")
    print(sum)





