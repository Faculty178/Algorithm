#11654

a = input()
print(ord(a))


# #3009

lista = []
listb = []
x = 0
y = 0

for _ in range(3):
    a, b = map(int, input().split())
    lista.append(a)
    listb.append(b)

for i in range(3):
    if lista.count(lista[i]) == 1:
        x = lista[i]
    
    if listb.count(listb[i]) == 1:
        y = listb[i]

print(x, y)


#2439

n = int(input())

for i in range(n):
    star = "*"*(i+1)
    print(star.rjust(n))


#1110

n= int(input())
cnt = 0
new_n = n

while(True):
    cnt += 1
    calc = n//10 + n%10
    n = calc%10 + (n%10*10)
   
    if(n == new_n):
        break


print(cnt)



#10250

n = int(input())

for _ in range(n):
    h, w, num = map(int, input().split())

    height = num % h
    rnum = num//h + 1

    if height == 0:
        height = h
        rnum -= 1

    ans = height*100 + rnum
    print(ans)


#10757
import sys
a, b = map(int, sys.stdin.readline().split())
print(a + b)


#2869
import sys
up, down, v = map(int, sys.stdin.readline().split())

if(v - down) % (up - down) == 0:
    print((v-down) // (up-down))
else:
    print((v-down) // (up-down) +1)


