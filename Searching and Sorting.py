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

# Bubblesort
def bubbleSort(arr):
    ans = arr[:]
    flag = True
    while flag:
        flag = False
        for i in range(1,len(ans)):
            if ans[i]<ans[i-1]:
                ans[i],ans[i-1] = ans[i-1],ans[i]
                flag = True
    return ans

# Mergesort        
def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid = int(len(arr)/2)
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left,right)

def merge(arr1,arr2):
    ans = []
    i,j = 0,0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1
    ans += arr1[i:] if i<len(arr1) else arr2[j:]
    return ans



# Testcase
arr = [1,2,3,5,6,7,8,10,13]
print(linSearch(arr,10))
print(binSearch(arr,10))

arr = [1,5,3,2,4,11,8,6,9]
arr2 = bubbleSort(arr)
arr3 = mergeSort(arr)
print(arr2)
print(arr3)
