#8958

n = int(input())

for _ in range(n):
    oxlist = list(input())
    score = 0
    score_sum = 0

    for ox in oxlist:
        if(ox == 'O'):
            score = score + 1
            score_sum = score_sum + score
        else:
            score = 0
    print(score_sum)




#4344

n = int(input())

for _ in range(n):
    caselist = list(map(int, input().split()))
    snumber = caselist[0]
    del caselist[0]
    
    case_avg = sum(caselist) / len(caselist)
    goodnum = 0
    
    for i in range(len(caselist)):
        if (caselist[i] > case_avg):
            goodnum = goodnum +1
    
    ans = goodnum/snumber*100
    
    print("%0.3f%%" % ans)
    
    

    
        
