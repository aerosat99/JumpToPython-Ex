#2-5-1
a = {'name' : '홍길동', 'birth' : 1125, 'age' : 30}
print(a)

#2-5-2
a = dict()
a['name'] = 'python'
print(a)

a = dict()
a[('a',)] = 'python'  # 키값에 튜플 가능
print(a)

a = dict()
a[250] = 'python'  # 키값에 리스트 불가능
print(a)

a = dict()
#a[[1]] = 'python'  # 키값에 리스트 불가능
print(a)

#2-5-3
a = {'A':90, 'B':80, 'C':70}
print(a['B'])
del a['B']

a = {'A':90, 'B':80, 'C':70}
a.pop('B')
print(a)

#2-5-4
a = {'A':90, 'B':80}
b = a.get('C', 70)
print(b)

#2-5-5
a = {'A':90, 'B':80, 'C':70}
b = a.values()
print(b)
print(min(b))

c = list(b)    # list 함수로 리스트로 변경
c.sort()
print(c[0])

#2-5-6
a = {'A':90, 'B':80, 'C':70}
b = a.items()
print(b)
c = list(b)
c.sort()
print(c)