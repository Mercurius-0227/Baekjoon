#2445번. 별 찍기-8
#2020.07.31

n=int(input())
for i in range(1,n+1):
    print("*"*i+" "*(2*n-2*i)+"*"*i)
for i in range(n-1,0,-1):
    print("*"*i+" "*(2*n-2*i)+"*"*i)