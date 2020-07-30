#2798 블랙잭
#2020.07.22

#입력받은 수와 가장 근접한 세 정수의 합을 구하는 함수
def black_jak(list_card, N, M):
    #가장 작은 세 정수의 합을 변수 Max_에 저장
    Max_=list_card[0]+list_card[1]+list_card[2]
    #Max_(세 정수의 합)가 M(입력받은 수)보다 작거나 같다면
    #변수rest에 M-Max_의 값을 저장함
    if M>=Max_:
        rest=M-Max_
    #선택한 세 장의 카드를 중복 없이 바꿈
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                #변수 test_Max에 다른 세 장의 카드의 합을 저장함
                test_Max=list_card[i]+list_card[j]+list_card[k]
                #test_Max가 M보다 작거나 같으면
                #test_rest에 M-test_Max의 값을 저장한다
                if test_Max<=M:
                    test_rest=M-test_Max
                #test_rest의 값이 rest보다 작다면 
                #test_rest가 M과 가장 근접한 나머지 값이므로
                #변수 Max_에 test_Max의 값을 저장
                #아니면 rest의 값 그대로 갖고감
                if test_rest<rest:
                    rest=test_rest
                    Max_=test_Max
    print(Max_)

N,M=input().split()
N=int(N)
M=int(M)
list_card=input().split()
list_card=list(map(int,list_card))
#입력받은 수들을 오름차순으로 정렬
list_card.sort()
black_jak(list_card, N, M)
Max_=0
test_Max=0
rest=0
test_rest=0
i=0
j=0
k=0