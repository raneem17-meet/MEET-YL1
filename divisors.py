def devisors(n):
	num = 1 
	while( num <= n):
		if (n%num==0):
			print (num)
		num+=1

devisors(8)
