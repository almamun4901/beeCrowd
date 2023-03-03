def scores():
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


def play():
    scores()
    print("novo calculo (1-sim 2-nao)")
    value = int(input())
    while value != 1 or value != 2:
        print("novo calculo (1-sim 2-nao)")
        value = int(input())

        if value == 1:
            scores()
        elif value == 2:
            break

play()
