#3-3-1
for i in range(1,101) :
    print(i)

#3-3-2
sum = 0
for i in range(1,1001) :
    if i % 5 == 0 :
        sum += i
print(sum)

#3-3-3
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for a in A :
    if a > 0 :
        sum += a
print(sum/len(A))

#3-3-4
data = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
result = {} # 딕셔너
for blood_type in data:
    if blood_type in result:  # 키 값이 존재하는 경우에는 기존 값에 더함
        result[blood_type] += 1
    else:  # 키 값이 없는 경우에는 새로운 키 생성
        result[blood_type] = 1
print(result)

#3-3-5
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)

result = [n*2 for n in numbers if n % 2 == 1]
print(result)

#3-3-6
sentence = 'Life is too short, you need python'
ex = 'aeiou'
print(''.join([a for a in sentence if a not in ex]))