#CS1 - Exercise 3
## Problem 1
Write down what each of the following pieces of code prints out. If there is an error in the code, describe the error.


### (a)
```python
for a in range(0, 5):
	for b in range(0, 5):
		if is_perfect_square(a, b):
			print(str(a*b) + “  is a perfect square)
		else:
			print(str(a*b) + “  is not a perfect square)
```


### (b)
```python
a = False
while not a:
	for x in range(3, 22):
		if a == 13:
			a = True
```


### (c)
```python
def return_false():
	print(False)
	return False

def return_true():
	print(True)
	return True


a = return_false() or return_true()
b = return_true() or return_false()
c = return_false() and return_true()
d = return_true() and return_false()
print(a, b, c, d)
```
 

### (d)
```python
n = -1
while n > -3:
	print(n, m)
	m = n - 1
	while m > -4:
		m -= 1
	n-= 1
	print(m, n)
```


## Problem 2
Write the selection_sort algorithm with a while loop instead of a for loop (hint: refer to chapter 9).

 
## Problem 3
Modify the selection_sort algorithm to order the characters in a string (e.g., “bafdc” -> “abcdf”).


## Problem 4
Modify the bouncing ball gravity problem found in chapter 10 so that the source of gravity flips from the bottom to the top of the screen every x seconds (do this problem on your computer, not by hand).