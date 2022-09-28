#2750

n = int(input())
a = [0]*n

for i in range(n):
    a[i] = int(input())

for i in range(n-1):
    for j in range(n-1-i):
        if(a[j]> a[j+1]):
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            
for i in range(n):
    print(a[i])
    

#1427
import sys
print = sys.stdout.write
A = list(input())

for i in range(len(A)):
    big = i
    for j in range(i+1, len(A)):
        if A[j] > A[big]:
            big = j
        if A[i] < A[big]:
            temp = A[i]
            A[i] = A[big]
            A[big] = temp
            

for i in range(len(A)):
    print(A[i])
        

# #11399
S = int(input())
B = list(map(int, input().split()))
sumlist = [0]*S

B.sort()
sumlist[0] = B[0]
for i in range(1, S):
    sumlist[i] = sumlist[i-1] + B[i]
    
sum = 0

for i in range(0, S):
    sum += sumlist[i]

print(sum)
