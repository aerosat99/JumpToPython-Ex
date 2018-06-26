languages = ['python','perl','c','java']

for lang in languages :
    if lang in ['python','perl'] :
        print('%6s needs interpreter'%lang)
    elif lang in ['c','java']:
        print('%6s needs compiler'%lang)
    else :
        print('should not reach here')

#02-1-1
grade = {'국어' : 80, '영어' : 75, '수학' : 55}
sum = grade['국어'] + grade['영어'] + grade['수학']
print(sum/len(grade))

#02-1-2,3
a = 17 // 3
b = 17 % 3
print(a,b)

#02-1-4
a = int(input('입력 = '))
if a % 2 == 0 :
    print('Even')
else :
    print('Odd')