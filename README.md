# PythonTemelProje-Python Basic Projects
A function that flattens a list and a function that reverses the elements in the given list has been created. 
## Flatten Function
```python
def flatten(x,y):
	for i in x:
		if isinstance(i,list):
			flatten(i,y)
		else:
			y.append(i)
	return y
 
a=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
b=[]
flatten(a,b)
[1, 'a', 'cat', 2, 3, 'dog', 4, 5]
```
## Reverse Function
```python
def reversetry(l):
	if isinstance(l,list):
		l.reverse()
		for i in l:
			reversetry(i)
	return l

a = [[1, 2], [3, 4], [5, 6, 7]]
reversetry(a)
[[7, 6, 5], [4, 3], [2, 1]]
```
