value = input()

value = value.split(" ")
start = int(value[0])

# sum = int(value[0])
sum = 0
for i in range(1, len(value)):
    if int(value[i]) >= 1:
        number = int(value[i])
        break

while number >= 1:
    sum = sum + start + number - 1
    number = number - 1

print(sum)