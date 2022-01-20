# 숫자 카드 게임 (그리디)
# 4:55~ 5:00
import sys 
input=sys.stdin.readline
n,m = map(int, input().split())

answer_list = []
for i in range(n):
    
    data = list(map(int, input().split()))
    data.sort() #1. [고칠점] sort 대신 min으로
    answer_list.append(data[0]) 
    
answer_list.sort() # 2. [고칠점] sort 대신 max로 

print(answer_list[n-1])
    

'''
[배울점]
파이썬에서 sort()의 시간복잡도는 O(N*logN)이다.
반면 min, max의 시간복잡도는 O(N) 이므로 위 코드에서 sort 대신 min을 쓰면 더 효율적이다.
ex) 


'''