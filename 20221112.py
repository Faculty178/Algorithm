#11478

import sys
input = sys.stdin.readline

line = input()
ans = set()

for i in range(len(line)):
    for j in range(i, len(line)):
        temp = line[i:j+1]
        ans.add(temp)

print(len(ans))



#11729
def hanoi_tower(n, start, end) :
    if n == 1 :
        print(start, end)
        return
       
    hanoi_tower(n-1, start, 6-start-end) # 1단계
    print(start, end) # 2단계
    hanoi_tower(n-1, 6-start-end, end) # 3단계
    
n = int(input())
print(2**n-1)
hanoi_tower(n, 1, 3)