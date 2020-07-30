#15651번. N과 M(3)
#2020.07.30
from itertools import product

n,m=map(int,input().split())
a=[]
for i in range(1,n+1):  
    a.append(i)
b=[]
for i in product(a,repeat=m):
    b.append(i)
for i in range(len(b)):
    print(' '.join(map(str,b[i])))

