#15650번. N과 M(2)
#2020.07.30
from itertools import combinations

n,m=map(int,input().split())
a=[]
for i in range(1,n+1):
    a.append(i)
b=list(combinations(a,m))
for i in range(len(b)):
    print(' '.join(map(str,b[i])))