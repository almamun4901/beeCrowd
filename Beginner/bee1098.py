# i = 0
#
# while i <= 2:
#     diff = 1
#     while diff <= 3:
#         print("I=", end="")
#         print(i, end=" ")
#         print("J=", end="")
#         print(diff + i)
#
#         diff = diff + 1
#
#     i = i + 0.2

i = 0

while i <= 2:
    diff = 1
    while diff <= 3:
        print("I=", end="")
        if i % 1 != 0:
            print(format(i,".1f"), end=" ")
        else:
            print(format(i,".0f"), end=" ")

        print("J=", end="")

        j = diff + i
        if j % 1 == 0:
            print(format(j,".0f"))
        else:
            print(format(j,".1f"))


        diff = diff + 1

    i = i + 0.2