#보물 (1026)
# 5:17~5:19


import sys 
input=sys.stdin.readline

n= int(input())

a=list(map(int, input().split()))
b=list(map(int, input().split()))
a.sort(reverse=True)
b.sort()
answer =0
for i in range(n):
    answer += a[i] * b[i]
print(answer)