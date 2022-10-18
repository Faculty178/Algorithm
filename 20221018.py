#10815
#Dictionary

import sys
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

dic = {i: 0 for i in nlist}

for j in mlist:
    if j in dic: 
        print(1, end=" ")
    else:
        print(0, end=" ")