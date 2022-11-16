#5086

while(True):
    a, b = map(int, input().split())
    if(a == 0 and b == 0):
        break
    
    if (b%a == 0) :
        print("factor")
    elif(a % b == 0):
        print("multiple")
    else:
        print("neither")
    


#1010

import math

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    ans = math.factorial(b)//(math.factorial(a)*math.factorial(b-a))
    
    print(ans)

    
    
#2004

a, b = map(int, input().split())

def count_number(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count


five_count = count_number(a, 5) - count_number(b, 5) - count_number(a-b, 5)
two_count = count_number(a, 2) - count_number(b, 2) - count_number(a-b, 2)

answer = min(five_count, two_count)
print(answer)