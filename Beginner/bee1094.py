number = int(input())

coelho = 0
rato = 0
sapo = 0

for i in range(0, number):
    test = input()
    test = test.split(" ")
    test[0] = int(test[0])
    if test[1] == "C":
        coelho = coelho + test[0]
    elif test[1] == "R":
        rato = rato + test[0]
    elif test[1] == "S":
        sapo = sapo + test[0]

total = coelho + sapo + rato
perCoelho = format((coelho / total) * 100, ".2f")
perRato = format((rato / total) * 100, ".2f")
perSapo = format((sapo / total) * 100, ".2f")

print("Total:",total,"cobaias")
print("Total de coelhos:", coelho)
print("Total de ratos:", rato)
print("Total de sapos:", sapo)
print("Percentual de coelhos:",perCoelho,"%")
print("Percentual de ratos:",perRato,"%")
print("Percentual de sapos:",perSapo,"%")
