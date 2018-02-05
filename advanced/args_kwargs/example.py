def test_var_args(*argv):
	for arg in argv:
		print(arg)

def test_kwargs(**kwargs):
	for key, value in kwargs.items():
		print('{0} = {1}'.format(key, value))

def main():
	test_var_args('red', 'green', 'blue')
	test_kwargs(red=(1,0,0), blue=(0, 1, 0), green=(0,0,1))

if __name__ == '__main__':
	main()
