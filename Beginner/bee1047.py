values = input()

values = values.split(" ")

a = int(values[0])
b = int(values[1])
c = int(values[2])
d = int(values[3])

if c > a:
    print("O JOGO DUROU", c-a ,"HORA(S)")
else:
    print("O JOGO DUROU", 24 - a + c ,"HORA(S)")