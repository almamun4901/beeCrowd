x = int(input())
y = int(input())

total = 0

if x > y:
    start = y
    end = x
else:
    start = x
    end = y

for i in range(start+1, end):
    if i % 2 != 0:
        total = total + i

print(total)