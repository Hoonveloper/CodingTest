# 큰 수의 법칙 문제 (그리디)
# 4:36~4:50
import sys 
input=sys.stdin.readline

n,m,k= map(int,input().split())
numbers=[]


numbers= list(map(int, input().split()))

numbers.sort(reverse=True)

print(numbers)

answer =0

count=0
while True:
    i=0
    for i in range(k):
        if (count==m) : break
        count+=1
        answer += numbers[0]
    
    if(count==m) : break
    count+=1
    answer+= numbers[1]
    
print(answer)