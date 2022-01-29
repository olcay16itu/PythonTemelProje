Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
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
>>> 
