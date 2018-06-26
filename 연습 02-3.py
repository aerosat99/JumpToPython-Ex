#02-3-1
a = ['Life', 'is', 'too', 'short', 'you', 'need', 'python']
print(a)
print(a[4], a[2])

#02-3-2
a = ['Life', 'is', 'too', 'short']
b = (a[0]+' '+a[1]+' '+a[2]+' '+a[3])
print(b)
c = ' '.join(a)
print(c)

#02-3-3
a = [1, 2, 3]
print(len(a))

#02-3-4
a = [1, 2, 3]
a.append([4,5])  # [1, 2, 3, [4, 5]]
print(a)

b = [1, 2, 3]
b.extend([4,5])  # [1, 2, 3, 4, 5]
print(b)

#02-3-5
k = [1, 3, 5, 4, 2]
k.sort()
k.reverse()
print(k)

#02-3-6
a = [1, 2, 3, 4, 5]
del a[1]
del a[2]
print(a)

a = [1, 2, 3, 4, 5]
a.remove(2)
a.remove(4)
print(a)

a = [1, 2, 3, 4, 5]
a.pop(1)
a.pop(2)
print(a)
