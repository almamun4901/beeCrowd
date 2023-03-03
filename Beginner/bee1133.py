x = int(input())
y = int(input())

if y < x:
    (y,x) = (x, y)

for i in range (x , y):
    if i % 5 == 2 or i % 5 == 3:
        print(i)