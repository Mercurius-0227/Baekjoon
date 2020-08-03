#2442번. 별 찍기-5
#2020.07.31

n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))