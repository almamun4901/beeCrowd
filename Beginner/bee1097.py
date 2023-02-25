i = 1
while i <= 9:
    diff = 6
    while diff >= 4:
        print("I=", end="")
        print(i, end=" ")
        print("J=", end="")
        print(i+diff)

        diff = diff - 1

    i = i + 2