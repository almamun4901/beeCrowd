sum = 0
count = 0
while count < 2:
    value = float(input())

    if value < 0 or value > 10:
        print("nota invalida")
    else:
        count = count + 1
        sum = sum + value

avrg = sum / 2
print("media =", format(avrg, ".2f"))