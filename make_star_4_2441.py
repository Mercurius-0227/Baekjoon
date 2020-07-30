#2441번. 별 찍기-4
#2020.07.30

n=int(input())
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*i)
