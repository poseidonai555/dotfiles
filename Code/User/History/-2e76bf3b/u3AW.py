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
    endvaluee = ""
    if not total / 9 < 1:
        if total - 9 == 1:


print(nibbletohex("1111"))