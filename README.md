# PythonTemelProje
>>> def flatten(x,y):
	for i in x:
		if isinstance(i,list):
			flatten(i,y)
		else:
			y.append(i)
	return y

>>> a=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
>>> b=[]
>>> flatten(a,b)
[1, 'a', 'cat', 2, 3, 'dog', 4, 5]

