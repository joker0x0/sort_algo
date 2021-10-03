def insertion_sort_algo(arr):

    for i in range(1, len(arr)):

        k = arr[i]

        j = i-1

        while j >= 0 and k < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = k


def selection_sort_algo(arr):

    for i in range(len(arr)):
        min_ind = i

        for j in range(i+1, len(arr)):

            if arr[min_ind] > arr[j]:
                min_ind = j

        arr[i], arr[min_ind] = arr[min_ind], arr[i]

def bubble_sort_algo(arr):

    for i in range(len(arr)):

        for j in range(0, len(arr)-i-1):

            if arr[j] > arr[j+1]:

                arr[j], arr[j+1] = arr[j+1], arr[j]

def merge_sort_algo(arr):

    if len(arr)>1:

        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort_algo(L)
        merge_sort_algo(R)

        i = j = k = 0

        while i < len(L) and j < len(R):

            if L[i] < R[j]:

                arr[k] = L[i]
                i+=1

            else:

                arr[k] = R[j]
                j+=1

            k+=1

        while i < len(L):

            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):

            arr[k] = R[j]
            j+=1
            k+=1
            
            
def partition(start, end, arr):

    piv_ind = start
    pivot = arr[piv_ind]

    while start < end:

        while start < len(arr) and arr[start] <= pivot:
            start+=1

        while arr[end] > pivot:
            end-=1            

        if start < end:

            arr[start], arr[end] = arr[end], arr[start]

    arr[end], arr[piv_ind] = arr[piv_ind], arr[end]

    return end

def quick_sort_algo(start, end, arr):

    if start < end:

        p = partition(start, end, arr)

        quick_sort_algo(start, p-1, arr)
        quick_sort_algo(p+1, end, arr)