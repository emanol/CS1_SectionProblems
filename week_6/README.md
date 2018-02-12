# 1. Write down and record the state of the following lists at each step as they are modified by:
- selection sort
- insertion sort
- merge sort

## (a) list1 = [0, 3, -3, 16]

## (b) list2 = [89, 45, 85, 81, 77, 94, 22, 79, 92, 91]

## (c) list3 = [-1, 43, 43, 12, 18]

## (d) Which algorithm sorted list1, list2, and list3 the fastest?

# 2. Recursion
## (a) Write a function called car_trip(msg) that takes a string as input, then prints that string, and then calls car_trip(msg) once again. Demo your function with the input "Are we there yet?" 

## (b) Modify car_trip to terminate after it has called itself 100 times. Make sure that your function retains an element of recursion. [hint: consider adding another parameter to car trip; how would you increment in that case?]

## (c) Modify car_trip once again such that when car_trip is at an even count, it prints "...", and when it is at an odd count, it prints the input msg.

# References
## Selection Sort
```python
def selection_sort(the_list):
    n = len(the_list)     # makes it easy to denote the length of the list

    for i in range(n - 1):
        # Find the minimum value in the sublist starting at index i.
        # smallest will hold the index of the smallest value we have found
        # so far in the sublist.
        smallest = i

        for j in range(i, n):
            if the_list[j] < the_list[smallest]:
                smallest = j

        # After the inner loop, smallest has the index of the smallest
        # value in the sublist starting at index i.  Swap the values
        # at index i and smallest.
        (the_list[i], the_list[smallest]) = (the_list[smallest], the_list[i])
```

## Insertion Sort
```python
def insertion_sort(the_list):
    n = len(the_list)   # how many items to sort

    for i in range(1, n):
        key = the_list[i]   # remember what was in the ith position

        j = i-1     # look in positions to the left of i
        while j >= 0 and the_list[j] > key:
            the_list[j+1] = the_list[j]
            j -= 1

        the_list[j+1] = key
```

## Merge Sort
```python
# Take two sorted lists, the_list[p : q+1] and the_list[q+1 : r+1],
# and merge them into the_list[p : r+1].
def merge(the_list, p, q, r):
    # Make a copy of the list items.
    left = the_list[p: q + 1]
    right = the_list[q + 1: r + 1]

    # Until we've gone through one of left and right, move
    # the smallest unmerged item into the next position in
    # the_list[p : r+1].

    i = 0       # index into left
    j = 0       # index into right
    k = p       # index into the_list[p : r+1]

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            the_list[k] = left[i]
            i += 1
        else:
            the_list[k] = right[j]
            j += 1
        k += 1

    # We've gone through one of left and right entirely.
    # Copy the remainder of the other to the end of the_list[p : r+1].

    # If left has remaining items, copy them into the_list, using list slices.
    if i < len(left):
        the_list[k: r + 1] = left[i:]

    # If right has remaining items, copy them into the_list, using list slices.
    if j < len(right):
        the_list[k: r+1] = right[j:]
```