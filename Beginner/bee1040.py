fourNum = input()

fourNum = fourNum.split(" ")

a = float(fourNum[0])
b = float(fourNum[1])
c = float(fourNum[2])
d = float(fourNum[3])

average = format((a * 2 +b * 3 + c * 4 + d * 1) / 10, ".1f")
average = float(average)


print("Media:", average)
if average > 7:
    print("Aluno aprovado.")
elif average < 5:
    print("Aluno reprovado.")
elif average >= 5 and average <= 6.9:
    print("Aluno em exame.")

    score = float(input())
    print("Nota do exame:", score)

    newAverage = (average + score) / 2
    if newAverage >= 5:
        print("Aluno aprovado.")
    elif newAverage <= 4.9:
        print("Aluno reprovado.")

    print("Media final:", format(newAverage, ".1f"))
