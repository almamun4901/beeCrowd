myList = []
limit = int(input())
for i in range(0,limit):
    x = int(input())
    if x >= 10 and x <= 20:
        myList.append(x)

print(len(myList), "in")
print(limit - len(myList), "out")

