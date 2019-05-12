# Hashsort
An idea of a simple and naive sorting algorithm that uses a hash (dictionary) as auxiliary structure.

The implementation uses python dictionary, which time complexity table follows:
Operation Average Case Amortized Worst Case
Copy[2]       O(n)             O(n)
Get Item      O(1)             O(n)
Set Item[1]   O(1)             O(n)
Delete Item   O(1)             O(n)
Iteration[2]  O(n)             O(n)
from: https://wiki.python.org/moin/TimeComplexity

From this table we can extract that the first part of the algorithm:
 
  for a in arr:
        if a not in hash:
            hash[a] = []
        hash[a].append(a)

The dictionary have an average case of O(1) for hash insertion (set) and traversing the input is O(n).

The final part of the algorithm traverses the dictionary extracting the list of values associated with the input arr:

  index = 0
    for k in hash:
        v = hash[k]
        if v:
            for l in v:
                arr[index] = l 
                index += 1

This part have a O(n*m) as m is the average repetition of a number on the arr input data.
Some test results with a list of 20000 numbers in different configurations. 

sorting 20000 random numbers
bubble sort exe time: 62.37069487571716 secs
hash sort exe time: 0.014582395553588867 secs
python sort exe time: 0.001989126205444336 secs
sort pass

sorting 20000 sorted numbers
bubble sort exe time: 34.52772521972656 secs
hash sort exe time: 0.013000726699829102 secs
python sort exe time: 0.0 secs
sort pass

sorting 20000 almost sorted numbers
bubble sort exe time: 34.41408395767212 secs
hash sort exe time: 0.013001441955566406 secs
python sort exe time: 0.0 secs
sort pass

sorting 20000 reversed numbers
bubble sort exe time: 87.37928915023804 secs
hash sort exe time: 0.012990236282348633 secs
python sort exe time: 0.0 secs
sort pass

sorting 20000 sparced random numbers
bubble sort exe time: 63.875147342681885 secs
hash sort exe time: 0.015000581741333008 secs
python sort exe time: 0.005990028381347656 secs
sort pass