# 구구단
for i in range(2,10) :  # 2~9단
    for j in range(1,10) : # 각 단마다 1~9까지 곱한다
        print(i * j, end = ' ') # 각 단은 옆으로 보여주고
    print(' ')                      # 단끼리는 줄 바꾼다

#4-1-1
def is_odd(a) :
    if a % 2 == 0 :
        return 'Even'
    else :
        return 'Odd'
print(is_odd(7))        # 함수 안에 print 없으면 함수 사용할때 print 추가 해야 하고

#4-1-2
def avg(*args) :
    sum = 0
    for i in args :
        sum += i
    print(sum/len(args))

avg(17,18,19,20,23)      # 함수 안에 print 넣으면 함수 사용할때 print 필요 없다

#4-1-3
def mul(a) :
    for i in range(1,10) :
        print(a * i, end = ' ')

a = int(input('입력 = '))
mul(a)

#4-1-4
def fib(a) :
    if a == 0 :
        return 0
    elif a == 1 :
        return 1
    else :
        return fib(a-2) + fib(a-1)

for a in range(0, 10) :
    print(fib(a))

#4-1-5
def myfunc(numbers):
    result = []
    for number in numbers:
        if number > 5:
            result.append(number)
    return result

p = myfunc([1,3,5,7,8,10])
print(p)

myfunc = lambda numbers : [number for number in numbers if number > 5]
p = myfunc([1,3,5,7,8,10])
print(p)