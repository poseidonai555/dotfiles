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
        print("flag")
        if total - 9 == 1:
            startvalue = "A"
        elif total - 9 == 2:
            startvalue = "B"
        elif total - 9 == 3:
            startvalue = "C"
        elif total - 9 == 4:
            startvalue = "D"
        elif total - 9 == 5:
            startvalue = "E"
        elif total - 9 == 6:
            startvalue = "F"
        return (f'{startvalue}{str(total-9)}')
    else:
        return(total)    

x = input("please enter a binary to turn into hex: ")
step = 1
nibble = []
fullhex = []
for char in x:
    if step % 4 == 0:
        nibble.append(char)
        fullhex.append(nibbletohex()"".join(nibble)))
        nibble = []
    else:
        nibble.append(char)
    step +=1

print("The full hexadecimal number is", fullhex)