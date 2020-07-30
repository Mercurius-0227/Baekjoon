#7568번: 덩치
#2020.07.23 완성

def compare_size(a,n,rank):
    for i in range(n):
        for j in range(n):
            if a[i][0]<a[j][0] and a[i][1]<a[j][1]:
                rank[i]+=1    
    #리스트를 출력 시 대괄호까지 출력되는 것을 막기 위해 문자열로 변환 후 출력
    print(" ".join(map(str,rank)))
    


n=int(input())
a=[]
rank=[]
for i in range(n):
    x=input().split()
    x[0]=int(x[0])
    x[1]=int(x[1])
    a.append(x)
    rank.append(1)
compare_size(a,n,rank)
