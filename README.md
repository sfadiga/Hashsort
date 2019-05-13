# Hashsort
An idea of a simple and naive sorting algorithm that uses a hash (dictionary) as auxiliary structure.

#### This algorithm will only work in python 2, where the dictionary keys are inserted on the hashtable in a sorted manner

The implementation uses python dictionary, which time complexity table follows:
```
Operation Average Case Amortized Worst Case
Copy[2]       O(n)             O(n)
Get Item      O(1)             O(n)
Set Item[1]   O(1)             O(n)
Delete Item   O(1)             O(n)
Iteration[2]  O(n)             O(n)
```
https://wiki.python.org/moin/TimeComplexity
* not sure if this is python 2 related

From this table we can extract that the first part of the algorithm complexity is O(n):
```
for a in arr:
    if a not in hash:
        hash[a] = 0
    hash[a] += 1
```

The dictionary have an average case of O(1) for hash insertion (set) and traversing the input is O(n).


The final part of the algorithm traverses the dictionary extracting the 'list' of values associated with the input arr:

```
index = 0
for k in hash:
    v = hash[k]
    for n in range(0, v):
        arr[index] = k
        index += 1
```

This part have a O(n*m) as m is the average duplication of a number on the arr input data.

## Some test results with a list of 20000 numbers in different test setups. 

### sorting 20000 random numbers
* bubble sort exe time: 25.0210001469 secs
* hash sort exe time: 0.0 secs
* python sort exe time: 0.0160000324249 secs
* sort pass
### sorting 20000 sorted numbers
* bubble sort exe time: 0.0 secs
* hash sort exe time: 0.000999927520752 secs
* python sort exe time: 0.0 secs
* sort pass
### sorting 20000 almost sorted numbers
* bubble sort exe time: 0.00500011444092 secs
* hash sort exe time: 0.0120000839233 secs
* python sort exe time: 0.0 secs
* sort pass
### sorting 20000 reversed numbers
* bubble sort exe time: 41.1089999676 secs
* hash sort exe time: 0.0160000324249 secs
* python sort exe time: 0.0 secs
* sort pass
### sorting 20000 sparse random numbers
* bubble sort exe time: 29.6339998245 secs
* hash sort exe time: 0.0160000324249 secs
* python sort exe time: 0.00600004196167 secs
* sort pass

