# Initialize the call count as a global variable
call_count = 0

def merge_sort(items):
    global call_count  # Use the global variable to count calls

    # Base case for recursion
    if len(items) < 2:
        return
    
    # Increment the call count each time merge_sort is called
    call_count += 1
    
    # Calculate midpoint
    midpoint = (len(items) - 1) // 2  
    
    # Create left half list
    left_half = items[0:midpoint + 1]  
    
    # Create right half list
    right_half = items[midpoint + 1:len(items)]  
    
    # Recursive call on left half
    merge_sort(left_half)  
    
    # Recursive call on right half
    merge_sort(right_half)  
    
    # Call procedure to merge both halves
    merge(items, left_half, right_half)  

def merge(items, left_half, right_half):
    # Merging function to sort and combine the halves
    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            items[k] = left_half[i]
            i += 1
        else:
            items[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        items[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        items[k] = right_half[j]
        j += 1
        k += 1

# Example usage
data = [7, 1, 3, 8, 5]
merge_sort(data)

# Output the number of times merge_sort was called
print(f"The merge_sort function was called {call_count} times.")
