## Problen 1
Find the bug(s).

### (a)
```python
class College(self, name, num_students):
	self.name = name
	self.num_students = num_students

	def get_name():
		return self.name

	def add_student():
		return self.num_students += 1

```

### (b)
```python
class Rectangle:
	def __init__(width, height):
		self.width = width
		self.height = height

	def get_area(self):
		return self.width * self.height

	def set_width(self, new_width):
		self.width = new_width
```

### (c)
```python
class Country:
	def __init__(self, name, population):
		self.name = self.name
		self.population = self.population

	def get_name(self):
		return self.name

	def get_population(self):
		return self.population
```

### (d)
```python
def Circle:
	def __init__(self, name, radius):
		self.name = name
		self.radius = radius

	def get_radius(self):
		return self.radius

	def set_radius(self, new_radius):
		self.radius = new_radius

	def __str__(self):
		return "The Circule " + self.name + " has a radius of " + str(self.radius)
```

### (e)
```python
class Balance:
	def init(self, name, account_num, balance):
		self.name = name
		self.account_num = account_num
		self.balance = balance

	def get_balance(self):
		return balance

	def add_money(self, amount):
		self.balance += amount

	def subtract_money(self, amount):
		self.balance -= amount

	def __str__(self):
		print(name + " has a balance of " + str(balance))
```

## Problem 2
### (a)
Create a class called <insert your name> with instance variables that you think represent important attributes about yourself.

### (b)
Next, create methods that modify those instance variables. For example, for the class Imanol, I would write a method call birthday() that would increment my age by 1. 

### (c)
Finally, once you are done creating that class, save it to a file called <insert name here>.py. Now, create another file called clone.py that creates 100 instances of the object based on yourself.

