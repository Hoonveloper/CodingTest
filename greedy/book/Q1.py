# 5:28~ 5:58 
# 모험가 길드 ( 그리디 )

import sys 
input=sys.stdin.readline

from collections import deque
n= int(input())

list=list(map(int,input().split()))
list.sort()
q= deque()
for i in range(n):
    q.append(list[i])
    
answer=0
flag=True
while True:
    flag=True
    if len(q) ==0 : break
    k=q.popleft()
    #print("---- {}----".format(k))
    for i in range(k-1):
        #print("Zz")
        a=q.popleft()

        if a!=k : flag=False
    
    if flag :answer+=1
print(answer)
    
'''


'''