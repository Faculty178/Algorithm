#24060

# 병합 정렬 구현
import sys
input = sys.stdin.readline

ans = []
n, k = map(int, input().split())
a = list(map(int, input().split()))

def merge(L):
    if( len(L) == 1):
        return L
    
    mid = (len(L) + 1) // 2
    
    left = merge(L[:mid])
    right = merge(L[mid:])
    
    i = 0
    j = 0
    L2 = []
    
    while (i < len(left) and j < len(right)):
        if( left[i] < right[j]):
            L2.append(left[i])
            ans.append(left[i])
            i += 1
        else:
            L2.append(right[j])
            ans.append(right[j])
            j += 1
    
    while i < len(left):
        L2.append(left[i])
        ans.append(left[i])
        i+=1
    while j < len(right):
        L2.append(right[j])
        ans.append(right[j])
        j+=1
    
    return L2

merge(a)

#k 추가
if (len(ans) >= k):
    print(ans[k-1])
else:
    print(-1)




#1085

x, y, w, h = map(int, input().split())
lengths = [x, y, w-x, h-y]
print(min(lengths))




#3053

import math
R = int(input())
print(R*R*math.pi)
print(R*R*2)