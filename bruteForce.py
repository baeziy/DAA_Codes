def foo(P):
	maxima = []
		
	for i in P:
		maximal = True
		for j in P:
			if (i != j) and (i[0] <= j[0]) and (i[1] <= j[1]):
				maximal = False
				break
		if maximal == True:
			maxima.append(i)	
	return maxima			
print(foo([(2,1), (4,1), (6,1), (2,2), (3,2), (2,3), (1,4), (5,4), (3,5), (2,7)]))
