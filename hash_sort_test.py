import hash_sort
 
import time
import random 


def bubble_sort(arr):
    '''
    a simple bubble sort algorithm
    '''
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1-i):
            if arr[ j ] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def sort_tester(size, verbose):
    '''
    compares 3 sorting algorithms, the hash sort, a bubble sort and python's sort
    print the timings for each algorithm runtime
    '''
    print("sorting {} numbers".format(size))
    data = []
    hash_data = []
    sort_data = []
    bsort_data = []
    for i in range(0, size):
        n = random.randrange(size)
        data.append(n)
        hash_data.append(n)
        sort_data.append(n)
        bsort_data.append(n)
    
    if verbose:
        print("original data:")
        print(data)
    
    start = time.time()
    hash_sort.hash_sort(hash_data)
    end = time.time()
    print 'hash sort exe time: {} secs'.format(end - start)

    if verbose:
        print("hash sorted data:")
        print(hash_data)

    start = time.time()
    bubble_sort(bsort_data)
    end = time.time()
    print 'bubble sort exe time: {} secs'.format(end - start)

    if verbose:
        print("bubble sorted data:")
        print(bsort_data)


    start = time.time()
    sort_data.sort()
    end = time.time()
    print 'python sort exe time: {} secs'.format(end - start)

    if verbose:
        print("python sorted data:")
        print(sort_data)

    if bool(set(data).intersection(hash_data)):
        print("sort pass")
    else:
        print("sort failed")
       


sort_tester(200000, False)



