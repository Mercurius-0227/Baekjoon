#14888번. 연산자 끼워넣기
#2020.08.03 완성
from itertools import permutations

#새 연산식을 구할 함수
def go_go(n,a,b,m,new_b):
    #연산식 문자열 리스트 new_b를 이용해 가능한 모든 연산식 문자열 구하기
    new_bb=[]
    for element in permutations(new_b,len(a)-1):
        new_bb.append(element)

    #문자열 리스트 new_b와 문자열 리스트 a를 이용해 모든 식을 새 리스트 new에 저장
    new=[]
    for i in range(m):
        imsi=[]
        imsi.append('('*(len(a)-1))
        for j in range(len(a)):
            imsi.append(a[j])
            if j!=0: imsi.append(')')
            if j<len(a)-1: imsi.append(new_bb[i][j])
        new.append(imsi)
    #print(new)
    new_=[]
    for i in range(m):
        new_.append(' '.join(new[i]))

    #문자열로 이루어진 모든 식 계산해서 결과를 새 리스트에 저장
    result=[]
    for i in range(m):
        imsi_=eval(new_[i])
        result.append(imsi_)
    
    #리스트에서 최댓값과 최솟값 찾기
    print(max(result))
    print(min(result))


            
#수 입력받음
n=int(input())
a=list(map(str,input().split()))
b=list(map(int,input().split()))

#새로 만들어질 연산식의 개수 구하기
m=1
for i in range(1,sum(b)+1):
    m=m*i
for j in range(len(b)):
    if b[j]>1:
        m=m//b[j]

#연산식 개수로 입력받은거 +-*/로 이루어진 문자열로 변환
new_b=[]
for i in range(len(b)):
    if b[i]==0:
        continue
    else: 
        if i==0:
            new_b.append('+'*b[0])
        elif i==1:
            new_b.append('-'*b[1])
        elif i==2:
            new_b.append('*'*b[2])
        else:
            new_b.append('/'*b[3])

#새 연산식을 구할 함수
go_go(n,a,b,m,new_b)