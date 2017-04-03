import random

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp = A[i+1]
    A[i+1] = A[r]
    A[r] = temp
    return i+1

def randomizedPartition(A, p, r):
    i = random.randint(p, r)
    temp = A[r]
    A[r] = A[i]
    A[i] = temp
    return partition(A, p, r)

def randomizedQuickSort(A, p, r):
    if p < r:
        q = randomizedPartition(A, p, r)
        randomizedQuickSort(A, p, q-1)
        randomizedQuickSort(A, q+1, r)

def bucketSort(A):
    n = len(A)
    B = []
    for i in range(0, n):
        B[i] = 0
    for i in range(1, n+1):
        B[i] = A[i]
    for i in range(0, n):
        randomizedQuickSort(B, 0, len(B))
    for i in range(0, n):
        C[i] = C[i] + B[i]
        
#bucketSort ne radi valjano
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Before sorting: ", alist)
n = len(alist)-1
bucketSort(alist)
print("After sorting: ", alist)       
  