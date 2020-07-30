#방법2
#
def check_chess(a,n,m):

    #첫번째 경우
    cnt1=0
    for i in range(n):
        for j in range(m):
            ii=(0 if i in [0,2,4,6] else 1)
            jj=(0 if j in [0,2,4,6] else 1)
            #체스판의 행과 열이 모두 짝수이거나 모두 홀수 일 때 [0,0]가 "B"로 시작
            #행이 짝수, 열이 홀수 혹은 행이 홀수, 열이 짝수 일 때 [0,0]가 "W"로 시작
            if (ii==0 and jj==0) or (ii==1 and jj==1):
                if a[i][j] !="B":cnt1+=1
            if (ii==0 and jj==1) or (ii==1 and jj==0):
                if a[i][j] !="W":cnt1+=1

    #두 번째 경우
    cnt2=0
    for i in range(n):
        for j in range(m):
            ii=(0 if i in [0,2,4,6] else 1)
            jj=(0 if j in [0,2,4,6] else 1)
            #체스판의 행이 짝수, 열이 홀수 혹은 행이 홀수, 열이 짝수 일 때 [0,0]가 "W"로 시작
            #행과 열이 모두 짝수이거나 모두 홀수 일 때 [0,0]가 "B"로 시작
            if (ii==0 and jj==0) or (ii==1 and jj==1):
                if a[i][j] !="W":cnt2+=1
            if (ii==0 and jj==1) or (ii==1 and jj==0):
                if a[i][j] !="B":cnt2+=1
    #cnt1과 cnt2중 최솟값을 반환
    return min(cnt1,cnt2)
    

n,m=map(int,input().split())
chess=[list(input())for i in range(n)]
check=list()
for i in range(n-7):
    for j in range(m-7):
        a=[z[(0+j):(8+j)] for z in chess[(0+i):(8+i)]]
        check.append(check_chess(a,n,m))
print(min(check))