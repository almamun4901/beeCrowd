takeInput = True

while takeInput:
    value = input()
    value = value.split(" ")

    m = int(value[0])
    n = int(value[1])

    if m == 0 or n == 0:
        takeInput = False
        break

    if m > 0 and n > 0:
        print("primeiro")
    elif m > 0 and n < 0:
        print("quarto")
    elif m < 0 and n < 0:
        print("terceiro")
    elif m < 0 and n > 0:
        print("segundo")