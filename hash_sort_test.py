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


def test_bubble_sort(data):
    start = time.time()
    bubble_sort(data)
    end = time.time()
    print("bubble sort exe time: {} secs".format(end - start))

def test_python_sort(data):
    start = time.time()
    data.sort()
    end = time.time()
    print("python sort exe time: {} secs".format(end - start))

def test_hash_sort(data):
    start = time.time()
    hash_sort.hash_sort(data)
    end = time.time()
    print("hash sort exe time: {} secs".format(end - start))


def random_tester(size):
    '''
    tests a random list of numbers based on size
    '''
    print("sorting {} random numbers".format(size))
    data = [random.randrange(size) for x in range(0, size)]
    hdata = data.copy()
    bdata = data.copy()
    
    test_bubble_sort(bdata)
    test_hash_sort(hdata)
    test_python_sort(data)
       
    # sanity check for hash sort   
    if bool(set(data).intersection(hdata)):
        print("sort pass")
    else:
        print("sort failed")


def almost_sorted_test(size):
    '''
    tests a sorted list of numbers and add a unsorted number on the begining of the list
    '''
    print("sorting {} almost sorted numbers".format(size))
    data = [x for x in range(0, size - 1)]
    data.insert(0,size) # almost sorted
    hdata = data.copy()
    bdata = data.copy()
    
    test_bubble_sort(bdata)
    test_hash_sort(hdata)
    test_python_sort(data)
       
    # sanity check for hash sort   
    if bool(set(data).intersection(hdata)):
        print("sort pass")
    else:
        print("sort failed")


def sorted_test(size):
    '''
    tests a sorted list of numbers from size length
    '''
    print("sorting {} sorted numbers".format(size))
    data = [x for x in range(0, size)]
    hdata = data.copy()
    bdata = data.copy()
    
    test_bubble_sort(bdata)
    test_hash_sort(hdata)
    test_python_sort(data)
       
    # sanity check for hash sort   
    if bool(set(data).intersection(hdata)):
        print("sort pass")
    else:
        print("sort failed")


def reversed_test(size):
    '''
    tests a reversed list of numbers based on size 
    '''
    print("sorting {} reversed numbers".format(size))
    data = [x for x in reversed(range(0, size))]
    hdata = data.copy()
    bdata = data.copy()
    
    test_bubble_sort(bdata)
    test_hash_sort(hdata)
    test_python_sort(data)
       
    # sanity check for hash sort   
    if bool(set(data).intersection(hdata)):
        print("sort pass")
    else:
        print("sort failed")


def sparced_random_test(size):
    '''
    tests a sparced list of random numbers based on size 
    '''
    print("sorting {} sparced random numbers".format(size))
    data = [random.randrange(size * 10) for x in range(0, size)]
    hdata = data.copy()
    bdata = data.copy()
    
    test_bubble_sort(bdata)
    test_hash_sort(hdata)
    test_python_sort(data)
       
    # sanity check for hash sort   
    if bool(set(data).intersection(hdata)):
        print("sort pass")
    else:
        print("sort failed")


'''
tests 
'''
test_size = 20000
random_tester(test_size)
sorted_test(test_size)
almost_sorted_test(test_size)
reversed_test(test_size)
sparced_random_test(test_size)

