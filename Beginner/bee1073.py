limit = int(input())

for i in range(1,limit+1):
    if i % 2 == 0:
        square = pow(i, 2)
        print(i,end="")
        print("^2 =", square)