
a = input()[1:-1]
a = [float(x) for x in a.split(',')]
c = []
for i in range(len(a)):
	if(a[i]>0):
		c.append(a[i])

print(c)		
