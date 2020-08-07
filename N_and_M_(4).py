#15652번. N과 M(4)
#2020.08.04

from itertools import combinations_with_replacement

n,m=map(int,input().split())
a=[]
for i in range(1,n+1):
    a.append(i)
answer=[]
answer=list(combinations_with_replacement(a,m))

for i in range(len(answer)):
    print(' '.join(map(str,answer[i])))