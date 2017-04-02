#HEAP SORT

import time
import numpy as np
import matplotlib.pyplot as plt
import random
import math

#maxHeapify
def heapify(myArray, n, i):
    largest = i
    l = 2 * i       #left child
    r = 2 * i + 1   #right child

    if l < n and myArray[i] < myArray[l]:
        largest = l
    else:
        largest = i
    if r < n and myArray[largest] < myArray[r]:
        largest = r

    if largest != i:
        myArray[i], myArray[largest] = myArray[largest], myArray[i] #swap
        heapify(myArray, n, largest)

def heapSort(myArray):
    #buildMaxHeap
    n = len(myArray)
    for i in range(math.floor(n/2), 0, -1): #descending loop
        heapify(myArray, n, i)
    #heapsort
    for i in range(n-1, 1, -1): #descending loop
        myArray[i], myArray[1] = myArray[1], myArray[i]
        n = n - 1
        heapify(myArray, n, 1)

#myList = ['x', 9, 7, 5, 3, 1, 12, 56, 123]
#print("------------------------------------------------------------")
#print("Unsorted list: ", myList)
#print("------------------------------------------------------------")
#heapSort(myList)
#print("Sorted list: ", myList)
#print("------------------------------------------------------------")


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
	
    # Sleep for n miliseconds
    
    # Profile function Example-fn and create plot
def FirstPlot():
    # Measure exeuction time
    algo_name = "[FirstPlot] Heap sort"
    input_data = []
    exec_time = []
    for n in range(100, 1100, 100):
        start_time = time.clock() # expressed in seconds
        myList = random.sample(range(0, 9999999), n)
        heapSort(myList)
        end_time = time.clock()
        exec_time.append((end_time - start_time) * 1000) #get miliseconds
        input_data.append(n)
    
    CreatePlot(input_data, exec_time, algo_name)

    # Profile function Example-fn and create plot	
def SecondPlot():
    # Measure exeuction time
    algo_name = "[SecondPlot] Heap sort"
    input_data = []
    exec_time = []
    
    for n in range(200, 2200, 200):
        start_time = time.clock() # expressed in seconds
        myList = random.sample(range(0, 9999999), n)
        heapSort(myList)
        end_time = time.clock()
        exec_time.append((end_time - start_time) * 1000) #get miliseconds
        input_data.append(n)
    
    CreatePlot(input_data, exec_time, algo_name)


# Profile functions and create plots
FirstPlot()
SecondPlot()

# Show plots
ShowPlot()