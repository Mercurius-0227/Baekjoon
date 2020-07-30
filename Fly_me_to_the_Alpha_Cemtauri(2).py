#1011
#처음과 끝의 1을 없다고 가정.

def jump_jump(distance, move_count, move, fibonacci):
    #값이 나올 때까지 반복.
    while True: 
        #fibonacci 이상 distance가 남아있어야 극단적 감소 가능(-1씩)(가장 짧은 시간이 걸림)
        if distance>fibonacci:
            #일단 한번 더 카운트
            move_count+=1
            #1광년씩 증가하며 이동
            move+=1
            #fibonacci와 distance의 합은 전체 길이가 되어야 함.
            fibonacci+=move
            distance-=move
            
        elif distance==fibonacci:
            move_count+=1
            distance-=move
            fibonacci+=move
            if distance==0:
                print(move_count)
                break
        else:
            #마지막이 (1광년-1광년)인 경우
            if move==1 or move==0:
               move+=1
            move_count+=1
            move-=1
            fibonacci+=move
            distance-=move
            if distance==0:
                print(move_count)
                break
       
            

def Alpha_Cemtauri(x, y):
    #전체 길이에서 처음과 끝 1씩 제외하기 위해 -2.
    distance=y-x-2
    #처음과 마지막을 미리 카운트해놓음.
    move_count=2
    #처음과 마지막 모두 1광년씩 움직임.
    move=1
    #fibonacci와 distance를 더하면 전체 길이가 되어야 하므로 2.
    fibonacci=2
    #중간값들 구하는 함수 호출.
    jump_jump(distance, move_count, move, fibonacci)

x,y=input().split()
x=int(x)
y=int(y)
distance=0
move_count=0

Alpha_Cemtauri(x, y)