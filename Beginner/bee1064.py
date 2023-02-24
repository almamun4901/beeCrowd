a = float(input())
b = float(input())
c = float(input())
d =float(input())
e = float(input())
f = float(input())

count = 0
sum = 0

if a > 0:
    count = count + 1
    sum = sum + a
if b > 0:
    count = count + 1
    sum = sum + b
if c > 0:
    count = count + 1
    sum = sum + c
if d > 0:
    count = count + 1
    sum = sum + d
if e > 0:
    count = count + 1
    sum = sum + e
if f > 0:
    count = count + 1
    sum = sum + f

print(count, "valores positivos")
print(format(sum / count, ".1f" ))