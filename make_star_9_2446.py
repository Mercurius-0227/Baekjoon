#2446번. 별 찍기-9
#2020.07.31

n=int(input())
for i in range(n):
    print(" "*i+"*"*(2*n-2*i-1))
for i in range(n-1,0,-1):
    print(" "*(i-1)+"*"*(2*n-2*i+1))