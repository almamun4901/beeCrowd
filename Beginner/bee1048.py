value = float(input())

if value >= 0 and value <= 400:
    bonus = value * 0.15
    percentage = 15

elif value >= 401.01 and value <= 800:
    bonus = value * 0.12
    percentage = 12

elif value >= 800.01 and value <= 1200:
    bonus = value * 0.10
    percentage = 10

elif value >= 1200.01 and value <= 2000:
    bonus = value * 0.07
    percentage = 7

elif value > 2000:
    bonus = value * 0.04
    percentage = 4

print("Novo salario:", format(value + bonus, ".2f"))
print("Reajuste ganho:", format(bonus, ".2f"))
print("Em percentual:", percentage, "%")
