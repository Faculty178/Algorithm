#2525

a,b = input().split()
c = int(input())
a = int(a)
b = int(b)

b = b + (c % 60)
if(b >= 60):
    a = a + (b // 60)
    b = b % 60

a = a + (c // 60)
if(a >= 24):
    a = a % 24

print(a, b)


#2562 

number=[]
for i in range(9):
    number.append(int(input()))

print(max(number))
print(number.index(max(number))+1)


#3052

number_list=[]
for i in range(10):
    number_list.append(int(input()) % 42)

number_list = set(number_list)
print(len(number_list))
