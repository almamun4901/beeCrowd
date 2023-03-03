x = int(input())
y = int(input())
sum = 0

if y < x:
    (y,x) = (x, y)

for i in range(x, y+ 1):
    if i % 13 != 0:
        sum = sum + i

print(sum)