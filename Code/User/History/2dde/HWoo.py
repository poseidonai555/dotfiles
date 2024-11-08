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

def bubbleSort(sortList, swap):
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
        length = last_swap_index
    
        if sorted:
            break
    if not swap:
        return sortList
    else:
        return sortList, swaps

def mergeSort(sortList, swap):
    # Base case: if the list is of length 0 or 1, it is already sorted
    if len(sortList) <= 1:
        return sortList, 0  # Return the list and 0 swaps
    
    mid = len(sortList) // 2
    leftHalf, leftSwaps = mergeSort(sortList[:mid])   # Recursive call on the left half
    rightHalf, rightSwaps = mergeSort(sortList[mid:])  # Recursive call on the right half

    mergedList, mergeSwaps = merge(leftHalf, rightHalf)  # Merge the sorted halves
    totalSwaps = leftSwaps + rightSwaps + mergeSwaps  # Total swaps

    return mergedList, totalSwaps  # Return merged list and total swaps

def merge(left, right):
    sortedList = []
    i = j = 0
    swaps = 0

    # Merge the two halves while there are elements in both
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sortedList.append(left[i])
            i += 1
        else:
            sortedList.append(right[j])
            j += 1
            swaps += 1  # Increment swap count for every element from right added
            swaps += (len(left) - i)  # Count remaining elements in left as swaps

    # If there are remaining elements in left, add them
    while i < len(left):
        sortedList.append(left[i])
        i += 1

    # If there are remaining elements in right, add them
    while j < len(right):
        sortedList.append(right[j])
        j += 1

    return sortedList, swaps  # Return merged list and swap count


def efficiency_test(n):
    import random
    l = []
    for i in range(n):
        l.append(random.randint(1,100))
    return bubbleSort(n, True), mergeSort(n, True)

numList = getList()
print("Bubble sort given:")
print(numList)
print("Bubble sort returns")
print(bubbleSort(numList, False))
print("Merge sort returns")
print(mergeSort(numList, False))
x = input("would you like to do efficiency test, if so enter the length of the list, otherwise leave this blanc")
if x:
    print(efficiency_test(x))
input()
