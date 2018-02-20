## Week 7

### Exercise 1
1. What is the difference between runtime complexity and space complexity?
3. What are the runtimes for linear, binary, and random search?
4. Order the following according on the basis of complexity: O(nlogn), O(n!), O(n^2), O(n), O(logn), O(sqr_root(n)), O(1), O(2^n)
5. Where do we usually see O(logn) runtime complexity?
5. How do constants factor into our analysis of algorithm complexity? 


### Exercise 2
What is the time and space complexity of the following peices of code?
#### (a)
```python
def sum(n):
	if n <= 0:
		return 0
	return n + sum(n - 1)
```

#### (b)
```python
def pair_sum_sequence(n):
	sum = 0
	for i in range(n):
		sum += pair_sum(i, i + 1)
	return sum

def pair_sum(a, b):
	return a + b
```

#### (c)
```python
def ex(list_1, list_2):
	for a in list_1:
		print(a)
	for b in list_2:
		print(b)
```

#### (d)
```python
def ex_2(list_1, list_2):
	for a in list_1:
		for b in list_2:
			print(a + "," + b)
```