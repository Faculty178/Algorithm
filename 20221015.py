#10872

n = int(input())

def factorial(num):
    if num == 0:
        return 1
    return factorial(num-1) * num

ans = factorial(n)
print(ans)
        
        


#10870

n = int(input())

def pibo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    
    return pibo(num - 1) + pibo(num -2)     

ans = pibo(n)
print(ans)



#10952

a, b = map(int, input().split())
while(a != 0 and b != 0):
    sum = a + b
    print(sum)
    a, b = map(int, input().split())




#10951

while(1):
    try:
        a, b = map(int, input().split())
        sum = a + b
        print(sum)
    except:
        break


   