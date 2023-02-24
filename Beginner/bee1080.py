max = 0
pos = 0
for i in range (0, 5):
    x = int(input())

    if x > max:
        max = x
        pos = i



print(max)
print(pos+1)
