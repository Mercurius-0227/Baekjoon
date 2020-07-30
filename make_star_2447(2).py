#2447번. 별 찍기
#2020.07.29
#방법2.(재귀함수x)
n=int(input())
#문자열 변수 저장
star=[]
for i in range(n):
    for j in range(n):
        mark=1
        i_=i
        j_=j
        while i_!=0:
            #빈 곳 지정
            if i_%3==1 and j_%3==1:
                mark=2
                star.append(' ')
                break
            j_=j_//3
            i_=i_//3
        if mark==1:
            star.append('*')
    star.append('\n')
result=''.join(star)
print(result)