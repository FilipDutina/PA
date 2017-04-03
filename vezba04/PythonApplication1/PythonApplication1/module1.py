import sys
import random
import time
import numpy as np
import matplotlib.pyplot as plt
import math



def RandomizedPartition(A,p,r):
    i= random.randint(p, r)
    A[r], A[i] = A[i], A[r]
    return Partition(A,p,r)

def RandomizedQuicksort(A,p,r):
    if p < r:
        q = RandomizedPartition(A,p,r)
        RandomizedQuicksort(A,p,q-1)
        RandomizedQuicksort(A,q+1,r)

def Partition(A,p,r):
    x= A[r]
    i= p-1
    for j in range(p,r):
        if A[j] <= x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r] = A[r], A[i+1]
    return i+1

def insertion_sort(seq):
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j - 1] > seq[j]:
            seq[j - 1], seq[j] = seq[j], seq[j - 1]
            j -= 1


def Bucket(A): 
        
    n = len(A)
    B = []
    for i in range(0, n-1):
        B[i] = []
    for i in range(1, n):
        B[math.floor(n*A[i])]=A[i]
    for i in range(0, n-1):
        insertion_sort(A)
    for i in range(0, n):
        C[i] = C[i] + B[i]
    




def CreatePlot(input_data, exec_time, algo_name):
    fig = plt.figure()     
    fig.suptitle(algo_name, fontsize=14, fontweight='bold')    
 
    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)       
    ax.set_title('Vreme izvrsenja')
    ax.set_xlabel('Ulaz [n]')    
    ax.set_ylabel('Vreme [ms]')

    ax.plot(input_data, exec_time, '-', color='green')
    
    print(algo_name)
    for i in range(0, len(input_data)):
        print("input_data: ", input_data[i], ", exec_time: ", exec_time[i])

    return fig

def ShowPlot():
    plt.show()

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list
	
    
    # Profile function Example-fn and create plot
def FirstPlot():
    # Measure exeuction time
    algo_name = "[FirstPlot] Example-fn"
    input_data = []
    exec_time = []
    for n in range(100, 1100, 100):    
        l = random.sample(range(0,1000),n)
        start_time = time.clock() # expressed in seconds
        RandomizedQuicksort(l,0,len(l)-1)
        end_time = time.clock()
        exec_time.append((end_time - start_time)*1000) #get miliseconds
        input_data.append(n)
    
    CreatePlot(input_data, exec_time, algo_name)

    # Profile function Example-fn and create plot	
def SecondPlot():
    # Measure exeuction time
    algo_name = "[SecondPlot] Example-fn"
    input_data = []
    exec_time = []
    
    for n in range(200, 2200, 200):
        l = random.sample(range(0,2000),n)
        start_time = time.clock() # expressed in seconds
        RandomizedQuicksort(l,0,len(l)-1)
        end_time = time.clock()
        exec_time.append((end_time - start_time)*1000) #get miliseconds
        input_data.append(n)
    
    CreatePlot(input_data, exec_time, algo_name)








l = random_list(1, 100, 50)
print("Before sorting: ", l)
n=len(l)-1
#insertion_sort(l)
Bucket(l)
#RandomizedQuicksort(l,0,n)
print("After sorting: ", l)
# Profile functions and create plots
#FirstPlot()
#SecondPlot()
# Show plots
#ShowPlot()