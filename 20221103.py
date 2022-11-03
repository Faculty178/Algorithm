#15649

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = []
already = [False]*(n+1)

def dfs():
    if len(nums) == m:
        print(' '.join(map(str, nums)))
        return 
    for i in range(1, n+1):
        if already[i]:
            continue
        already[i] = True
        nums.append(i)
        dfs()
        nums.pop()
        already[i] = False
        
dfs()


#15650

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = []
already = [False]*(n+1)

def dfs(first):
    if len(nums) == m:
        print(' '.join(map(str, nums)))
        return 
    for i in range(first, n+1):
        if already[i]:
            continue
        already[i] = True
        nums.append(i)
        dfs(i+1)
        nums.pop()
        already[i] = False
        
dfs(1)



#15651

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = []

def dfs():
    if len(nums) == m:
        print(' '.join(map(str, nums)))
        return 
    
    for i in range(1, n+1):
        nums.append(i)
        dfs()
        nums.pop()
        
dfs()



#15652

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = []


def dfs(first):
    if len(nums) == m:
        print(' '.join(map(str, nums)))
        return 
    for i in range(first, n+1):
        nums.append(i)
        dfs(i)
        nums.pop()
        
dfs(1)



