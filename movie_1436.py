#1436번. 영화감독 숌
#666을 포함하는 숫자 중 몇 번째 숫자인지 출력
n=int(input())
movie=666
count=0
#movie를 1씩 더해감
while(True):
    #666이 안에 있으면 count를 증가
    if "666" in str(movie):
        count+=1
    #count가 입력받은 값과 같다면 movie출력
    if count==n:
        print(movie) 
        break
    movie+=1