def nibbletohex(nibble):
    total = 0 
    if nibble[0] == "1":
        total += 8
    if nibble[1] == "1":
        total += 4
    if nibble[2] == "1":
        total += 2
    if nibble[3] == "1":
        total += 1
    startvalue = ""
    if not total / 9 < 1:
        if total - 9 == 1:
            startvalue = "A"
        elif total - 9 == 2:
            startvalue = "B"
        elif total - 9 == 3:
            startvalue = "C"
        elif total -9 == 4:
            startvalue = "D"
        elif total - 9 == 5:
            startvalue == "E"
        elif total - 0 == 6:
            startvalue == "F"
        return (f'{startvalue}{str(total-9)}')
    else:
        return(total)

print(nibbletohex("1111"))    

x = input("please enter a binary to turn into hex: ")
step = 0
nibble = []
fullhex = []
for char in x:
    step +=1
    if step / 4 == 0:
        fullhex.append("".join(nibble))
        nibble = []
    else:
        nibble.append(char)

print("The full hexadecimal number is", fullhex)