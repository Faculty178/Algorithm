#2588
import sys
input = sys.stdin.readline

A = int(input())  
B = input()       

AxB2 = A * int(B[2])
AxB1 = A * int(B[1])
AxB0 = A * int(B[0])
AxB = A * int(B)

print(AxB2, AxB1, AxB0, AxB, sep='\n')



#25083
print("         ,r'\"7")
print("r`-_   ,'  ,/")
print(" \\. \". L_r'")
print("   `~\\/")
print("      |")
print("      |")



#10809
word = input()
alphabet = list(range(97,123)) 

for x in alphabet :
    print(word.find(chr(x))) 