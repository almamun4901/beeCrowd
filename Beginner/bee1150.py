x = int(input())

while True:
    z = int(input())
    if z > x:
        break
sum = 0
count = 0
while sum <= z:
    sum = sum + x + count
    count = count + 1

print(count)