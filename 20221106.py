#2675

import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    num, s = input().split()
    text = ''
    for i in s:
        text += int(num) * i
    print(text)



#1157

import sys
input = sys.stdin.readline

word = input().lower()      # word = mississipi / baaa
word_list = list(set(word)) # word_list = ['m', 'i', 's', 'p'] / ['b', 'a']
cnt = []

for i in word_list:         # i = m, i, s, p / b, a
    count = word.count(i)
    cnt.append(count)       # cnt = [4, 4, 1, 1] / [1, 3]

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))].upper())




#1316

import sys
input = sys.stdin.readline

n = int(input())

group_word = 0
for _ in range(n):
    word = input()
    error = 0
    for index in range(len(word)-1): 
        if word[index] != word[index+1]:  
            new_word = word[index+1:]  
            if new_word.count(word[index]) > 0:  
                error += 1 
    if error == 0:  
        group_word += 1  
print(group_word)