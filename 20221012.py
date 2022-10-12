#10950

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    print(a + b)




#25304

x = int(input())
n = int(input())
sum = 0

for _ in range(n):
    a, b = map(int, input().split())
    sum = sum + (a * b)

if(sum == x):
    print("Yes")
else:
    print("No")




#15552

import sys
t = int(input())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)




#11021

t = int(input())

for i in range(1, t+1):
    a, b = map(int, input().split())
    sum = a + b
    print(f"Case #{i}: {sum}")




#11022

t = int(input())

for i in range(1, t+1):
    a, b = map(int, input().split())
    sum = a + b
    print(f"Case #{i}: {a} + {b} = {sum}")



#10871

n, x = map(int, input().split())
data = list(map(int, input().split()))

for i in range(n):
    if(data[i] < x):
        print(data[i], end=" ")


