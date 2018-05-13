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

# Quicksort
def quicksort(arr):
    ans = arr[:]
    quicksort_util(ans,0,len(ans)-1)
    return ans

def quicksort_util(arr,low,high):
    if low>=high:
        return
    p = partition(arr,low,high)
    quicksort_util(arr,low,p-1)
    quicksort_util(arr,p+1,high)

def partition(arr,low,high):
    mid = int((low+high)/2)
    pivot = arr[mid]
    left,right = low,high
    while left<right:
        while left<=high and arr[left]<pivot:
            left += 1
        while right>=low and arr[right]>pivot:
            right -= 1
        if left<right:
            arr[left],arr[right] = arr[right],arr[left]
    return right


# Testcase
arr = [1,2,3,5,6,7,8,10,13]
print(linSearch(arr,10))
print(binSearch(arr,10))

arr = [1,5,3,2,4,11,8,6,9]
arr2 = bubbleSort(arr)
arr3 = mergeSort(arr)
arr4 = quicksort(arr)
print(arr2)
print(arr3)
print(arr4)
