value = input()

value = value.split(" ")
x = int(value[0])
y = int(value[1])

for i in range (1, y+1):

    if i % x == 0:
        print(i, end="\n")
    else:
        print(i, end=" ")