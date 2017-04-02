#SELECTION SORT

import time
import numpy as np
import matplotlib.pyplot as plt
import random

def selectionSort(myList):
    n = len(myList) 

    #for i in range(0, n-1) : 
    #    for j in range(i+1, n) :
    #        if myList[i] > myList[j] :
    #            temp = myList[i]
    #            myList[i] = myList[j]
    #            myList[j] = temp
    for i in range(0, n - 1):
        iMin = i

        for j in range(i + 1, n):
            if myList[j] < myList[iMin]:
                iMin = j

        #swap elements
        if iMin != i:
            temp = myList[iMin]
            myList[iMin] = myList[i]
            myList[i] = temp

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
    algo_name = "[FirstPlot] Selection sort"
    input_data = []
    exec_time = []
    for n in range(100, 1100, 100):
        start_time = time.clock() # expressed in seconds
        myList = random.sample(range(0, 9999999), n)
        selectionSort(myList)
        end_time = time.clock()
        exec_time.append((end_time - start_time) * 1000) #get miliseconds
        input_data.append(n)
    
    CreatePlot(input_data, exec_time, algo_name)

    # Profile function Example-fn and create plot	
def SecondPlot():
    # Measure exeuction time
    algo_name = "[SecondPlot] Selection sort"
    input_data = []
    exec_time = []
    
    for n in range(200, 2200, 200):
        start_time = time.clock() # expressed in seconds
        myList = random.sample(range(0, 9999999), n)
        selectionSort(myList)
        end_time = time.clock()
        exec_time.append((end_time - start_time) * 1000) #get miliseconds
        input_data.append(n)
    
    CreatePlot(input_data, exec_time, algo_name)


# Profile functions and create plots
FirstPlot()
SecondPlot()

# Show plots
ShowPlot()