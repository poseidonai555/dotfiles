x = int(input("Please enter a number: "))

multiples = []

for i in range(x):
    l = []
    for j in range(i):
        if (i+1) % (j+1) == 0:
            l.append(j)
    multiples.append(l)

print(multiples)
    