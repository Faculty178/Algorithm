# #1874
count = 1
temp = True
stack = []
op = []

N = int(input())
for i in range(N):
    num = int(input())
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1

    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        temp = False
        break

if temp == False:
    print("NO")
else:
    for i in op:
        print(i)




# #1253

n = int(input())
nums = map(int, input().split())
nums = sorted(nums)

answer = 0

def pointer(li, target):
    global answer
    start, end = 0, len(li) - 1

    while start < end:
        s = li[start] + li[end]
        if target == s:
            answer += 1
            return
        elif target > s:
            start += 1
        elif target < s:
            end -= 1


for i in range(n):
    pointer(nums[:i] + nums[i+1:], nums[i])

print(answer)


#1377
import sys
input = sys.stdin.readline

n = int(input())
A = []
cnt = 0

for i in range(n):
    A.append((int(input()), i))

newA = sorted(A)

for i in range(n):
    if cnt < newA[i][1] - i : 
        cnt = newA[i][1] - i

print(cnt + 1)
