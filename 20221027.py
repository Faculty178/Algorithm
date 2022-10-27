#2839

import sys
input = sys.stdin.readline

n = int(input())

ans = 0

while n >= 0 :
	if n % 5 == 0:
		ans += n//5
		print(ans)
		break
	n = n - 3
	ans += 1
else:
	print(-1)





#2775

import sys
input = sys.stdin.readline

lst = [[0 for j in range(14)] for i in range(15)]
for i in range(15):
    lst[i][0] = 1
for h in range(14):
    lst[0][h] = h+1
for i in range(1,15):
    for j in range(1,14):
        lst[i][j] = lst[i][j - 1] + lst[i - 1][j]

Test_case = int(input())
for i in range(Test_case):
    k = int(input())
    n = int(input())
    print(lst[k][n-1])
	



	
#25501

import sys
input = sys.stdin.readline


def recursion(txt, l, r):
	global cnt 
	cnt += 1
	
	if(l >= r):
		return 1
	elif( txt[l] != txt[r]):
		return 0
	else:
		return recursion(txt, l+1, r-1)

def isPalindrome(txt):
	return recursion(txt, 0, len(txt)-1)
	
	
	
n = int(input())

for _ in range(n):
	cnt = 0
	print(isPalindrome(input().rstrip()), cnt)
