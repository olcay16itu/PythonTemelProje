Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def reversetry(l):
	if isinstance(l,list):
		l.reverse()
		for i in l:
			reversetry(i)
	return l

>>> a = [[1, 2], [3, 4], [5, 6, 7]]
>>> reversetry(a)
[[7, 6, 5], [4, 3], [2, 1]]
>>> 
