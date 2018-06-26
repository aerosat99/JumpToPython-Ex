#2-6-1
a = set(['a', 'b', 'c'])
print(a)

#2-6-2
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
b = set(a)
print(b)

#2-6-3
s1 = set(['a', 'b', 'c', 'd', 'e'])
s2 = set(['c', 'd', 'e', 'f', 'g'])
s3 = s1 - s2
print(s3)

#2-6-4
a = {}
print(type(a))

b = set()
print(type(b))

#2-6-5
a = set(['a', 'b', 'c'])   #{} 안에 값만 입력하면 집합, 키:밸류 형태로 입력하면 딕셔너리
b = set(['d', 'e', 'f'])
c = a | b
print(c)        #합집합 | 교집합 &

a = set({'a','b','c'})
a.add('d')
a.add('e')
a.add('f')
print(a)

a = set({'a','b','c'})
a.update(['d','e','f'])
print(a)