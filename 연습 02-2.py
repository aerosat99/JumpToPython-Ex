#02-2-1
print('"점프 투 파이썬" 문제를 풀어보자')

#02-2-2
print('''
Life is too short
You need Python''')

#02-2-3,7
a = 'PYTHON'
print('%30s'%a)
print(' '*24 + a)

#02-2-4,5
pin = "881120-1068234"
birthday = pin[0:6]
print(birthday)
sex = pin[7]
print(sex)

#02-2-6
a = '1980M1120'
b = a[0:4]
c = a[4]
d = a[5:]
print(c+b+d)

#02-2-8
a = 'Life is too short, you need python'
print(a.find('short'))
print(a.index('short'))

#02-2-9
a = 'a:b:c:d'
b = a.replace(':','#')
print(b)

#02-2-10
a = 'a:b:c:d'
b = a.split(':')
c = '#'.join(b)
print(c)