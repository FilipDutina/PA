import math

#maxHeapify
def heapify(arr, n, i):
    largest = i
    l = 2 * i       #left
    r = 2 * i + 1   #right

    if l < n and arr[i] < arr[l]:
        largest = l
    else:
        largest = i
    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    #buildMaxHeap
    n = len(arr)
    for i in range(math.floor(n/2), 0, -1):
        heapify(arr, n, i)
    #heapsort
    for i in range(n-1, 1, -1):
        arr[i], arr[1] = arr[1], arr[i]
        n -= 1
        heapify(arr, n, 1)

#test
arr = ['x', 7, 15, 62, 74, -2, -14, 54, 33, 34, 32, -155]
print("Unsorted array is: ", arr)
heapSort(arr)
print("Sorted array is: ", arr)
        