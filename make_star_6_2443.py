#2443번. 별 찍기-6
#2020.07.31

n=int(input())
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))