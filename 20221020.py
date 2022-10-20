#4948

n=123456
def prime_list(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True		

primes_list = list(range(2,246912))
ans_list = []

for i in primes_list:
    if prime_list(i):
        ans_list.append(i)
        
        
while True:
    
    cnt = 0

    num = int(input())
  
    if num == 0:
        break
    
    for i in ans_list:
        if num < i < 2*num+1:
            cnt += 1
            
    print(cnt)
    
    
#9020 

num = int(input())

n = 10000 


a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False


for i in range(num):
    ans1 = 0
    ans2 = 0
    even = int(input())

    even_first = even // 2

    ans1 = even_first
    ans2 = even_first
    
    if ans1 not in primes and ans2 not in primes:
        while True:
            ans1 -= 1
            ans2 += 1
            
            if ans1 in primes and ans2 in primes:
                break
        
    print("{0} {1}".format(ans1, ans2))