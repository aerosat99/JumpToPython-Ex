#3-2-1
i = 1
sum = 0
while i <= 100 :
    i += 1
    sum += i
print(sum)

#3-2-2
i = 3
sum = 0
while i % 3 == 0 and i <= 1000 :
    i += 3
    sum += i
print(sum)

#3-2-3
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
while A :
    b = A.pop()
    if b > 50 :
        sum += b
print(sum)

#3-2-4
a = 1
while a < 5:
    print('*' * a)
    a += 1

#3-2-5
star = 7
space = 0
while star > 0 :
    print(' ' * space + '*' * star)
    star += -2
    space += 1

