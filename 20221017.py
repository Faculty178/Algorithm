#1747

import math
from sys import stdin
input = stdin.readline

n = int(input())

def prime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if not num%i:
            return False
    
    return True

def palindrum(num):
    for i in range(len(num)//2):
        if num[i] != num[-i-1]:
            return False
    return True


while True:
    if palindrum(str(n)) and prime(n):
        break
    else:
        n += 1

print(n)
        

    



#2751

import sys
input=sys.stdin.readline

n=int(input())
li=[]

for i in range(n):
    li.append(int(input()))

for i in sorted(li):
    print(i)