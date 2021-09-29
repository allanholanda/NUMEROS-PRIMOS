# Exercício 7
limite = int(input('Digite um valor limite: '))

for x in range(2, limite):
    primo = True
    for y in range(2,x):
        if (x % y == 0):
            primo = False
    if primo:
       print(x)


