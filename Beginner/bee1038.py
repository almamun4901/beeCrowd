value = input()

value = value.split(" ")
code = int(value[0])
quantity = int(value[1])

if code == 1:
    print("Total: R$", format(quantity * 4, ".2f"))
elif code == 2:
    print("Total: R$", format(quantity * 4.5, ".2f"))
elif code == 3:
    print("Total: R$", format(quantity * 5, ".2f"))
elif code == 4:
    print("Total: R$", format(quantity * 2, ".2f"))
elif code == 5:
    print("Total: R$", format(quantity * 1.5, ".2f"))
