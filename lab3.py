import random
import time
import matplotlib.pyplot as plt
import numpy as np 
from scipy.interpolate import spline

############## INSERTION SORT ###############
def insSort(a):
    numComp=0
    for i in range(0, len(a)):
        for j in range(i, 0, -1):
            numComp += 1
            if a[j] < a[j-1]:
                temp = a[j]
                a[j] = a[j-1]
                a[j-1] = temp
            else:
                break
    return numComp


################ MERGESORT #################
def merge(a, lo, mid, hi):
    num_comp = 0
    # a[lo..mid] and a[mid+1..hi] are sorted
    
    # two pointers that point to the 1st element in each sorted part
    i = lo
    j = mid + 1

    # copy the original array into an auxiliary array
    aux = a.copy()

    # repeat for each slot in a[lo..hi]
    for k in range(lo, hi + 1):
        # all elements in the lower half has been merged
        if i > mid:
            a[k] = aux[j]
            j += 1
        # all elements in the upper half has been merged
        elif j > hi:
            a[k] = aux[i]
            i += 1
        # first element in the lower half is smaller than that in the upper half
        elif aux[i] < aux[j]:
            a[k] = aux[i]
            i += 1
            num_comp += 1
        else:
            a[k] = aux[j]
            j += 1
            num_comp += 1
    return num_comp
    
def mergeSort(a, lo, hi):
    first_comp = 0
    second_comp = 0
    if hi <= lo:
        return 0
    mid = lo + int((hi-lo) / 2)
    if hi-lo > 1:
        first_comp = mergeSort(a, lo, mid)
        second_comp = mergeSort(a, mid+1, hi)
    total = merge(a, lo, mid, hi) + first_comp + second_comp
    return total

ascending_time_insertion = []
descending_time_insertion = []
random_time_insertion = []

ascending_time_merge = []
descending_time_merge = []
random_time_merge = []

def run(sizes):
    for size in sizes:
        l = list(range(size))
        
        #ascending
        l_ins = l.copy()
        l_merge = l.copy()
        #insertion sort
        start = time.time()
        comp = insSort(l_ins)
        duration = time.time()-start
        ascending_time_insertion.append(duration)
        print('--------------')
        print("List size :" , size)
        print('--------------')
        print("list in ascending order: ")
        print("num of comparison for insertion sort: ",comp)
        print("CPU time : ",duration)
        #merge sort
        start = time.time()
        total_comp = mergeSort(l_merge,0,size-1)
        duration = time.time()-start
        ascending_time_merge.append(duration)
        print("num of comparison for merge sort: ",total_comp)
        print("CPU time: ",duration)
        print('-------------------------------')

        #----------------------------------------------------------------
        #descending
        l.sort(reverse=True)
        l_ins = l.copy()
        l_merge = l.copy()
        #insertion sort
        start = time.time()
        comp = insSort(l_ins)
        duration = time.time()-start
        descending_time_insertion.append(duration)
        print("list in dscending order: ")
        print("num of comparison for insertion sort: ",comp)
        print("CPU time : ",duration)
        #merge sort
        start = time.time()
        total_comp = mergeSort(l_merge,0,size-1)
        duration = time.time()-start
        descending_time_merge.append(duration)
        print("num of comparison for merge sort: ",total_comp)
        print("CPU time: ",duration)
        print('--------------------------------')
        
        #--------------------------------------------------------
        #random shuffle the list
        random.shuffle(l)
        l_ins = l.copy()
        l_merge = l.copy()
        #insertion sort
        start = time.time()
        comp = insSort(l_ins)
        duration = time.time()-start
        random_time_insertion.append(duration)
        print("list in random : ")
        print("num of comparison for insertion sort: ",comp)
        print("CPU time : ",duration)
        #merge sort
        start = time.time()
        total_comp = mergeSort(l_merge,0,size-1)
        duration = time.time()-start
        random_time_merge.append(duration)
        print("num of comparison for merge sort: ",total_comp)
        print("CPU time: ",duration)
        print('---------------------------------')

if __name__ == "__main__":

    size = [1000,2000,3000,4000,5000,6000]
    run(size)

    #plot the graph
    fig = plt.figure()
    #insertion sort
    #ascending
    ax1 = fig.add_subplot(231)
    ax1.title.set_text('ascending-insertion sort')
    ax1.plot(size,ascending_time_insertion,'o')
    #descending
    ax2 = fig.add_subplot(232)
    ax2.title.set_text('descending-insertion sort')
    ax2.plot(size,descending_time_insertion,'o')
    #random
    ax3 = fig.add_subplot(233)
    ax3.title.set_text('random-insertion sort')
    ax3.plot(size,random_time_insertion,'o')

    #mergesort
    #ascending
    ax4 = fig.add_subplot(234)
    ax4.title.set_text('ascending-mergesort')
    ax4.plot(size,ascending_time_merge,'o')
    #descending
    ax5 = fig.add_subplot(235)
    ax5.title.set_text('descending-mergesort')
    ax5.plot(size,descending_time_merge,'o')
    #random
    ax6 = fig.add_subplot(236)
    ax6.title.set_text('random-mergesort')
    ax6.plot(size,random_time_merge,'o')
    plt.show()
