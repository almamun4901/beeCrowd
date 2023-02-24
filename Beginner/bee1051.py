value = float(input())

tax = 0


if value >= 0 and value <= 2000:
    print("Isento")

if value >= 2000.01 and value <= 3000:
    tax = (value -2000) * 0.08
    print("R$", format(tax, ".2f"))

if value >= 3000.01 and value <= 4500:
    tax = (1000 * 0.08) + ((value -3000) * 0.18)
    print("R$", format(tax, ".2f"))

if value > 4500:
    tax = (1000 * 0.08) + (1500 * 0.18) + ((value - 4500) * 0.28)
    print("R$", format(tax, ".2f"))

