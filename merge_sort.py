import time
import matplotlib.pyplot as plt
import numpy as np


def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle of the array
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort the two halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

def correct(arr):
    cor = True
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            cor = False

    if cor:
        print("Selection Sort returns a sorted array correctly")
    else:
        print("Selection sort failed to return a sorted array")


size = 10
array = [5, 2, 4, 7, 1, 3, 2, 6]
print(array)
sorted_array = merge_sort(array)
print(sorted_array)
correct(sorted_array)
