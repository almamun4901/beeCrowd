# Bee 1021
value = float(input())
valueraw = value

value100 = int(value // 100)
value = value % 100

value50 = int(value // 50)
value = value % 50

value20 = int(value // 20)
value = value % 20

value10 = int(value // 10)
value = value % 10

value5 = int(value // 5)
value = value % 5

value2 = int(value // 2)
value = value % 2

value1 = int(value // 1)
value = value % 1

valueHalf = int(value // 0.5)
value = value % 0.5

valueQuarter = int(value // 0.25)
value = value % 0.25

valueTenth = int(value // 0.1)
value = value % 0.1

valueFifth = int(value // 0.05)
value = value % 0.05

valueOneth = int(value // 0.01)
value = value % 0.01

print("NOTAS:")
print(value100,"nota(s) de R$ 100.00")
print(value50,"nota(s) de R$ 50.00")
print(value20,"nota(s) de R$ 20.00")
print(value10,"nota(s) de R$ 10.00")
print(value5,"nota(s) de R$ 5.00")
print(value2,"nota(s) de R$ 2.00")
print("MOEDAS:")
print(value1,"moeda(s) de R$ 1.00")
print(valueHalf,"moeda(s) de R$ 0.50")
print(valueQuarter,"moeda(s) de R$ 0.25")
print(valueTenth,"moeda(s) de R$ 0.10")
print(valueFifth,"moeda(s) de R$ 0.05")
print(valueOneth,"moeda(s) de R$ 0.01")
