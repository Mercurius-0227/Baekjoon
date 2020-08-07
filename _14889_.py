#14889번. 스타터와 링크
#2020.08.05 완성


from itertools import combinations

def go_go(n,s):
    a=[]
    for i in range(n):
        a.append(i)
    team=list(combinations(a, n//2))  
    power=[]
    for i in range(len(team)):
        t=list(combinations(team[i],2))
        imsi=0
        for k in range(len(t)):
            a=t[k][0]
            b=t[k][1]
            imsi+=s[a][b]
            imsi+=s[b][a]
        power.append(imsi)
    min_=abs(power[0]-power[-1])
    for i in range(len(power)):
        imsi=abs(power[i]-power[-1-i])
        if abs(imsi)<abs(min_): min_=imsi
    
    print(min_)

n=int(input())
s=[]
for i in range(n):
    imsi=list(map(int,input().split()))
    s.append(imsi)

go_go(n,s)