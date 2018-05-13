# Searching Algos

# Linear Search
def linSearch(arr, x):
    for i,el in enumerate(arr):
        if el==x:
            return i
    return -1

# Binary Search
def binSearch(arr, x):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = int((high+low)/2)
        if arr[mid]<x:
            low = mid+1
        elif arr[mid]>x:
            high = mid-1
        else:
            return mid
    return -1

arr = [1,2,3,5,6,7,8,10,13]
print(linSearch(arr,10))
print(binSearch(arr,10))
