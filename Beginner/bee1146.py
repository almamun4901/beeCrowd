while True:
    value = int(input())

    if value == 0:
        break;

    for i in range(1, value+1):
        if i == value:
            print(i)
        else:
            print(i, end=" ")
