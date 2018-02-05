## Problem 1
Assign a variable x the value 0. Within a while loop, increment x by 1 for each iteration of the loop. Have the loop terminate once x has:
	- Been an even number two times
	- AND
	- Been an odd number three times

## Problem 2
Write a function that prints out every integer between inputs a and b. If a is greater than b, or if a and b are equal, print “bad input” and exit the function. To get full credit, use a for-loop, NOT a while-loop.

## Problem 3
Write a function that takes in a string and prints out every letter in that string. [Hint: remember that strings share certain qualities with lists. How do you index into a list?]

## Problem 4
Write a function that takes in a string and outputs the same string but with all the vowels capitalized. 

## Problem 5
Which of the following if statements will cause you to lose a point on the exam?

```Python
happy = True
if happy == True:
	print(“don’t write boolean conditions like this”)
if happy:
	print(“do write boolean conditions like this”)
```

## Problem 6
Evaluate the following code and write down the results:

```python
a = True
b = False
c = False
d = True

print(a and b)
print(a or b or c)
print(c or d and b or c)
print(b or c or a)
```

### Problem 7
Write a function that detects whether an integer is even or odd. [Hint: %]

### Proble 8
Write a function that takes in an array full of 1’s and 0’s (e.g. [0, 1, 1, 0, 0, 1] and outputs an array with all the 1’s and 0’s flipped. If any of the elements in the array are not a 1 or a 0, print “bad input” to the console and exit the function. 