n = int(input('Enter how many fibonacci numbers you want to print:'))
if(n == 1):
	print(0)
elif(n == 2):
	print(0, 1)
elif(n <= 0):
	print('Input number should be greater than 0')		
else:	
	def fibonacci(a,b):
		c = a + b
		print(c , end=' ')
		global count
		count += 1
		if(count!=n-2):
			fibonacci(b,c)
	print(0, 1, end= ' ')
	count = 0
	fibonacci(0,1)	


    
	