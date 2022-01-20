# 1이 될 때까지 (greedy)

# 5:04~
import sys 
input=sys.stdin.readline

n,k= map(int ,input().split())
count=0
while True:
    if n==1: break
    elif n%k==0:
        n/=k
    else:
        n-=1
    count+=1
print(count)