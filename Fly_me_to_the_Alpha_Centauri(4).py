#1011: Fly me to the Alpha Centauri

#방법 1:
#규칙1. N의 제곱 + N의 거리 이후 횟수가 증가한다
#규칙2. N의 제곱일 때는 2*N-1, N의 제곱 + N일 때는 2*N, 그 이후로는 2*N+1의 횟수를 가진다

import math
T=int(input())
for i in range(T):
    x,y=map(int, input().split())
    
    diff=int(y-x)
    #3 이하는 그대로 출력
    if diff<=3:
        print(diff)
    #3 이상은 x와 y의 거리에 따라 규칙을 찾아 해결
    else:
        #제곱근 함수 sqrt 사용(import math)
        n=int(math.sqrt(diff))
        #n의 제곱일 때는 2*n-1
        if diff == n**2:
            print(2*n-1)
        #n의 제곱 + n일 때는 2*n
        elif n**2<diff<=n**2+n:
            print(2*n)
        #그 외는 2*n+1
        else:
            print(2*n+1)


