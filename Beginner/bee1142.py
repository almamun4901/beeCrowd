value = int(input())
count = 1
# limit = count + 3
for i in range(value):
    limit = count + 3
    while count < limit:
        print(count, end=" ")
        count = count+1

        if count % 4 == 0:
            print("PUM")
            count = count + 1
