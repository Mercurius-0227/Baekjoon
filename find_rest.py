#1978
#소수 찾기
#2020.07.17 완성!

import sys
input=sys.stdin.readline

N=int(input())
list_A=input().split()
list_A=list(map(int,list_A))
count=0
i=0
j=0
mark=1

for i in range(N):
    for j in range(2,list_A[i]):
        rest=list_A[i]%j
        if list_A[i]==1:
            mark=1
        if rest==0:
            mark=1
        else:
            mark=0
    if mark==0:
        count+=1

print(count)



            