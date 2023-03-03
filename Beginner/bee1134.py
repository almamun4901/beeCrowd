alcohol = 0
gasoline = 0
diesel = 0


while True:
    value = int(input())
    if value == 4:
        break
    elif value == 1:
        alcohol = alcohol+1
    elif value == 2:
        gasoline = gasoline + 1
    elif value == 3:
        diesel = diesel + 1

print("MUITO OBRIGADO")
print("Alcool:", alcohol)
print("Gasolina:", gasoline)
print("Diesel:", diesel)
