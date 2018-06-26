#4-2-1
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다" % total)

#4-2-2
my_list = ('65,45,2,3,45,8')
a = my_list.split(',')
sum = 0
for i in a :
    sum += int(i)
print(sum)

#4-2-4
a = int(input('구구단을 출력할 숫자를 입력하세요(2~9): '))
for i in range(1,10) :
    print(a * i, end = ' ')