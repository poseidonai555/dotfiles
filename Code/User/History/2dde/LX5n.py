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

def bubbleSort(sortList):
    length = len(sortList)
    while True:
        sorted = True
        last_swap_index = 0
        
        for i in range(1, length):
            if sortList[i - 1] > sortList[i]:
                sortList[i - 1], sortList[i] = sortList[i], sortList[i - 1]
                sorted = False
                last_swap_index = i
        length = last_swap_index
    
        if sorted:
            break
    return sortList

def mergeSort(sortList):
    # Base case: if the list is of length 0 or 1, it is already sorted
    if len(sortList) <= 1:
        return sortList
    
    mid = len(sortList) // 2
    leftHalf = mergeSort(sortList[:mid])   # Recursive call on the left half
    rightHalf = mergeSort(sortList[mid:])  # Recursive call on the right half

    return merge(leftHalf, rightHalf)  # Merge the sorted halves

def merge(left, right):
    sortedList = []
    i = 0
    j = 0

    # Merge the two halves while there are elements in both
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sortedList.append(left[i])
            i += 1
        else:
            sortedList.append(right[j])
            j += 1

    # If there are remaining elements in left, add them
    while i < len(left):
        sortedList.append(left[i])
        i += 1

    # If there are remaining elements in right, add them
    while j < len(right):
        sortedList.append(right[j])
        j += 1
        
    return sortedList

numList = getList()
print("Bubble sort given:")
print(numList)
print("Bubble sort returns")
print(bubbleSort(numList))
print("Merge sort returns")
print(mergeSort(numList))
input()
