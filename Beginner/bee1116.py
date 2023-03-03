takeInput = int(input())

for i in range (takeInput):
    value = input()
    value = value.split(" ")

    m = int(value[0])
    n = int(value[1])

    if n != 0:
        print(format(m / n, ".1f"))
    else:
        print("divisao impossivel")