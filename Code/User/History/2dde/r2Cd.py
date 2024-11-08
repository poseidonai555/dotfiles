def getList():
    numList = []
    while True:
        try:
            x = input("Add an integer number to the list (or press Enter to finish): ")
            if x == "":
                break
            numbers = x.split(',')
            for number in numbers:
                number = number.strip()
                if number:
                    numList.append(int(number))
        except ValueError:
            print("Only integers can be accepted")
    return numList

def bubbleSort(sortList, swap=True):
    length = len(sortList)
    swaps = 0
    
    while True:
        sorted = True
        last_swap_index = 0
        
        for i in range(1, length):
            if sortList[i - 1] > sortList[i]:
                sortList[i - 1], sortList[i] = sortList[i], sortList[i - 1]
                sorted = False
                last_swap_index = i
                swaps += 1

        length = last_swap_index
        if sorted:
            break

    if not swap:
        return sortList
    else:
        return sortList, swaps

def mergeSort(sortList, swap=True):
    if len(sortList) <= 1:
        return sortList
    
    mid = len(sortList) // 2
    leftHalf = mergeSort(sortList[:mid], swap)
    rightHalf = mergeSort(sortList[mid:], swap)

    mergedList, mergeSwaps = merge(leftHalf, rightHalf)
    
    if not swap:
        return mergedList
    else:
        totalSwaps = mergeSwaps + (0 if isinstance(leftHalf, list) else 0)
        return mergedList, totalSwaps

def merge(left, right):
    sortedList = []
    i = j = 0
    swaps = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sortedList.append(left[i])
            i += 1
        else:
            sortedList.append(right[j])
            j += 1
            swaps += 1
            swaps += (len(left) - i)

    while i < len(left):
        sortedList.append(left[i])
        i += 1

    while j < len(right):
        sortedList.append(right[j])
        j += 1

    return sortedList, swaps

def efficiency_test(n):
    import random
    l = []
    for i in range(n):
        while True:
            x = int(random.randint(1,100))
            if x not in l:
                break
        l.append(x)
    print(l)
    return bubbleSort(l, False), mergeSort(l, False)

numList = getList()
print("Bubble sort given:")
print(numList)
print("Bubble sort returns")
print(bubbleSort(numList, False))
print("Merge sort returns")
print(mergeSort(numList, False))
x = int(input("would you like to do efficiency test, if so enter the length of the list, otherwise leave this blanc: "))
if x:
    print(efficiency_test(x))
input()
