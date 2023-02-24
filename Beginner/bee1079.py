value = int(input())

for i in range(0,value):
    digits = input()
    digits = digits.split(" ")

    a = float(digits[0])
    b = float(digits[1])
    c = float(digits[2])

    average = format((a * 2 + b * 3 + c * 5)/ 10, ".1f")

    print(average)