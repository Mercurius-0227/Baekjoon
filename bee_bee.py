cnt=0
front_cnt=0
n=int(input("정수를 입력하세요>"))
i=0
front_i=0
k=0

while True:
    k=k+1
    i=i+k
    front_i=i-k
    cnt=(i*6)+1
    front_cnt=(front_i*6)+1
    if n>=front_cnt and n<=cnt:
        if n==front_cnt:
             print(k)
             break
        print(k+1)
        break
