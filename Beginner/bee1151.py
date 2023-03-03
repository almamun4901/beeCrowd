value = int(input())

first = 0
second = 1

print(first, end=" ")
print(second, end=" ")

for i in range(2, value):
    next = first + second

    first = second
    second = next

    if i == value - 1:
        print(next)
    else:
        print(next, end=" ")

