#02-4-1
a = (3,)
print(a)

#02-4-2
'''
>>> a = (1, 2, 3)
>>> a[1] = 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment'''

#02-4-3
a = (1,2,3)
b = (4,)
c = (a+b)
print(c)

print(type(4)) # int
print(type(4,)) # int