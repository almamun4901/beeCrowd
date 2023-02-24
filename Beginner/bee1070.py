value = int(input())

count = 0

while count < 6:
    if value % 2 != 0:
        print(value)
        count = count + 1
    value = value + 1