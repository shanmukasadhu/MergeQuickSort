

def findPivot(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i+=1
            (arr[i], arr[j]) = (arr[j],arr[i])
    (arr[i+1], arr[high]) = (arr[high], arr[i+1])
    return i+1
def quick_sort(arr, low, high):
    if low < high:
        
        pivot = findPivot(arr, low, high)
        
        quick_sort(arr,  low, pivot-1)
        quick_sort(arr, pivot+1, high)
 
 
data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quick_sort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)
    
        
        
    
    
    