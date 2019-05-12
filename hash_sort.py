def hash_sort(arr):
    '''
        A very simple and naive sort algorithm that uses a hash table as auxiliary structure 
        A good use case for this algorithm is a list of numbers distributed randomly 
        but with range approximate of the size of the list. 
        :param arr: a list of numbers to be sorted, the list will be sorted in place
    '''
    # creates the aux hash 
    # add a list as a value to this hash so it could handle duplicate values
    # uses the values from the arr as key to the hash, this is where sorting gets place
    hash = {}
    # transfer values from arr to the hash using the arr value as a key
    #start = time.time()    
    for a in arr:
        if a not in hash:
            hash[a] = []
        hash[a].append(a)
 
    # traverses the hash extracting the values from it and set back to the
    # original arr structure, the inner for handles the list (also if duplicate values)
    index = 0
    for k in hash:
        v = hash[k]
        if v:
            for l in v:
                arr[index] = l 
                index += 1
