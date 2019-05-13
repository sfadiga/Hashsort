def hash_sort(arr):
    '''
        this code will only work in python 2
        A very simple and naive sort algorithm that uses a hash table as auxiliary structure 
        A good use case for this algorithm is a list of numbers distributed randomly 
        but with range approximate of the size of the list. 
        :param arr: a list of numbers to be sorted, the list will be sorted in place
    '''
    # creates the aux hash 
    # add a counter as a value to this hash so it could handle duplicate values
    # uses the values from the arr as key to the hash, this is where sorting gets place
    hash = {}
    for a in arr:
        if a not in hash:
            hash[a] = 0
        hash[a] += 1
 
    # traverses the hash extracting the count values from it and set back to the
    # original arr structure, the inner for handles the counter for 1 or more duplicates
    index = 0
    for k in hash:
        v = hash[k]
        for n in range(0, v):
            arr[index] = k
            index += 1
