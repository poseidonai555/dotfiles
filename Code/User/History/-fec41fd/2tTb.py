x = int(input("Please enter a number: "))

multiples = []

for i in range(x):
    l = []
    for j in range(i):
        if (i+1) % (j+1) == 0:
            l.append(j)
    multiples.append(l)

factors = []

for item in multiples:
    for i in range(len(item)):
        for xitem in multiples:
            if multiples[item][i] in multiples[xitem]:
                factors.append(multiples[item][i])

print(multiples)
print(factors)