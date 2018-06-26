#3-1-1
money = 5000
card = False

if card == True or money > 4000 :
    print('TAXI available')

#3-1-2
lucky_list = [1, 9, 23, 46]
hold1 = 45
hold2 = 9
print('Hold1 : WoW') if hold1 in lucky_list else print('Hold1 : Sorry')
print('Hold2 : WoW') if hold2 in lucky_list else print('Hold2 : Sorry')

#3-1-3
a = int(input('?'))
if a % 2  == 0 :
    print('Even')
else :
    print('Odd')

#3-1-4
a = 'age : 30, Height : 180'
b = a.split(',')
print(b)
c = b[0].split(':')[-1]  # b[0] 'age : 30'을 age와 30으로 분리한 것중에 마지막 = 30
d = b[1].split(':')[-1]
age = int(c)
height = int(d)
print('Yes') if age < 30 and height >= 175 else print('No')