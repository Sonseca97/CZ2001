import random
import time
import matplotlib.pyplot as plt
import numpy as np 


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
        l_ins = l
        l_merge = l
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
        l_ins = l
        l_merge = l
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
        l_ins = l
        l_merge = l
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

    size = [1000,3000,5000,10000]
    run(size)

    fig = plt.figure()
    ax1 = fig.add_subplot(221)
    ax1.plot(size,random_time_merge,'b--')
    ax1.plot(size,random_time_insertion,'r--')

    ax2 = fig.add_subplot(222)
    ax2.plot(size,ascending_time_insertion,'r--',size,ascending_time_merge,'b--')
    ax3 = fig.add_subplot(223)
    ax3.plot(size,descending_time_insertion,'r--',size,descending_time_merge,'b--')

    ax1.title.set_text('list in random')
    ax2.title.set_text('list in ascending order')
    ax3.title.set_text('list in descending order')

    plt.show()
