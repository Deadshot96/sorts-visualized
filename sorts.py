from typing import List
from Box import Box

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def bubbleSort(array: List[Box]):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)
                yield array

def selectionSort(array: List[Box]):
    for i in range(len(array) - 1):
        minIndex = i
        j = i + 1
        while (j < len(array)):
            if array[j] < array[minIndex]:
                minIndex = j
                # swap(array, i, minIndex)
                
            j += 1
            yield array
            
        swap(array, i, minIndex)
        yield array
    yield array

def insertionSort(array: List[Box]):
    for i in range(1, len(array)):
        temp = array[i]
        j = i
        while (j > 0 and array[j - 1] > temp):
            array[j] = array[j - 1]
            j -= 1
            yield array
            
        array[j] = temp
    yield array

def mergeSort(array: List[Box]):
    pass

def shellSort(array: List[Box]):
    gap = len(array) // 2
    while gap >= 1:
        for j in range(gap, len(array), gap):
            i = j - gap
            while (i >= 0):
                if array[i] > array[i + gap]:
                    swap(array, i, i + gap)
                    yield array
                i -= gap
        
        gap //= 2
        
    yield array
    