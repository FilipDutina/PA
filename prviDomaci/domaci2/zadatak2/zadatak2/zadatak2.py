#RADIX SORT

import time
import numpy as np
import matplotlib.pyplot as plt
import random
import math

def radixSort(myList):
    radix = 10  #decSys
    maxLength = False   #end of current number
    temp = -1
    placement = 1   #dimension of number(1, 10, 100, 1000...)

    while not maxLength:
        maxLength = True
        #make buckets ----> [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
        buckets = [list() for i in range(radix)]
    
        for i in myList:
            temp = i / placement
            buckets[math.floor(temp % radix)].append(i) #make integer from float
            if maxLength and temp > 0:
                maxLength = False

        a = 0
        for b in range(radix):
            bucket = buckets[b]
            for i in bucket:
                myList[a] = i
                a = a + 1

        placement = placement * radix   #increase the dimension of number

#myList = [9, 7, 5, 3, 1, 12, 56, 123]
#print("------------------------------------------------------------")
#print("Unsorted list: ", myList)
#print("------------------------------------------------------------")
#radixSort(myList)
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
    algo_name = "[FirstPlot] Radix sort"
    input_data = []
    exec_time = []
    for n in range(100, 1100, 100):
        start_time = time.clock() # expressed in seconds
        myList = random.sample(range(0, 9999999), n)
        radixSort(myList)
        end_time = time.clock()
        exec_time.append((end_time - start_time) * 1000) #get miliseconds
        input_data.append(n)
    
    CreatePlot(input_data, exec_time, algo_name)

    # Profile function Example-fn and create plot	
def SecondPlot():
    # Measure exeuction time
    algo_name = "[SecondPlot] Radix sort"
    input_data = []
    exec_time = []
    
    for n in range(200, 2200, 200):
        start_time = time.clock() # expressed in seconds
        myList = random.sample(range(0, 9999999), n)
        radixSort(myList)
        end_time = time.clock()
        exec_time.append((end_time - start_time) * 1000) #get miliseconds
        input_data.append(n)
    
    CreatePlot(input_data, exec_time, algo_name)


# Profile functions and create plots
FirstPlot()
SecondPlot()

# Show plots
ShowPlot()