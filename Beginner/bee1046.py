values = input()

values = values.split(" ")

a = int(values[0])
b = int(values[1])

if b > a:
    print("O JOGO DUROU", b-a ,"HORA(S)")
else:
    print("O JOGO DUROU", 24 - a + b ,"HORA(S)")


