# Mergesort
    
def mergelists(leftSide, rightSide):
    # Right and Left pointer for both sub-lists.
    leftIndex = 0
    rightIndex = 0
    arr = []
    
    # Move pointers and sort numbers into a final index
    while(leftIndex < len(leftSide) and rightIndex < len(rightSide)):
        # If left number is lower than right number, add left number to final array and
        # move left pointer.
        if leftSide[leftIndex] <= rightSide[rightIndex]:
            arr.append(leftSide[leftIndex])
            leftIndex+=1
        # If right number is lower than left number, add right number to final array and
        # move right pointer.        
        else:
            arr.append(rightSide[rightIndex])
            rightIndex+=1
    # Add remaining numbers to the final array.
    while(leftIndex < len(leftSide)):
        arr.append(leftSide[leftIndex])
        leftIndex+=1
    while(rightIndex < len(rightSide)):
        arr.append(rightSide[rightIndex])
        rightIndex+=1
        
    return arr
        
    
    
def merge_sort(array):
    if len(array) > 1:
        # Find Mid-Point and split the array into 2
        midPoint = len(array) // 2
        leftSide = array[:midPoint]
        rightSide = array[midPoint:]
        
        leftArr = merge_sort(leftSide)
        rightArr = merge_sort(rightSide)
        
        # Merge both sub-lists
        finalMerge = mergelists(leftArr, rightArr)
        return finalMerge
    else:
        return array

    
arr = [3,8,1,5,6,2,9,11]
print(f"Before: {arr}")
print(f"After: {merge_sort(arr)}")