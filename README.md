# PythonTemelProje
## Flatten Function
<p>def flatten(x,y):</p>
	<p>for i in x:</p>
		<p>if isinstance(i,list):</p>
			<p>flatten(i,y)</p>
		else:
			y.append(i)
	return y

a=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
b=[]
flatten(a,b)
[1, 'a', 'cat', 2, 3, 'dog', 4, 5]

## Reverse Function
def reversetry(l):
	if isinstance(l,list):
		l.reverse()
		for i in l:
			reversetry(i)
	return l

a = [[1, 2], [3, 4], [5, 6, 7]]
reversetry(a)
[[7, 6, 5], [4, 3], [2, 1]]
