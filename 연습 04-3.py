#4-3-1
f1 = open("test1.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test1.txt", 'r')
print(f2.read())
f2.close()

#4-3-2
f2 = open('test2.txt','a')
a = input('message = ')
f2.write(a)
f2.write("\n")
f2.close()


#4-3-3
with open('abc.txt','w') as f :
    f.write('AAA\nBBB\nCCC\nDDD\nEEE')

f = open('abc.txt','r')
lines = f.readlines()  # 모든 라인을 읽음
f.close()

rlines = reversed(lines)  # 읽은 라인을 역순으로 정렬

f = open('abc.txt','w')
for line in rlines :
    line = line.strip()  # 포함되어 있는 줄바꿈 문자 제거
    f.write(line)
    f.write('\n')       # 줄바꿈 문자 삽입
f.close()

#4-3-4
with open('test4.txt','w') as f :
    f.write('Life is too short\nYou need java')

f = open('test4.txt','r')
data = f.read()
data1 = data.replace('java','python')
f.close()

with open('test4.txt','w') as f :
    f.write(data1)

#4-3-5
with open('sample.txt','w') as f :
    f.write('70\n60\n55\n75\n95\n90\n80\n80\n85\n100')

f = open('sample.txt','r')
data = f.readlines()    # sample.txt를 줄단위로 모두 읽는다.
f.close()

f = open('result.txt','w')
sum = 0
for i in data :
    score = int(i)     # 줄에 적힌 점수를 숫자형으로 변환한다.
    sum += score
avg = sum / int(len(data))
f.write(str(avg))
f.close()
# 숫자 값은 result.txt 파일에 바로 쓸 수 없으므로 str함수를 이용하여 문자열로 변경한 후 파일에 쓴다.