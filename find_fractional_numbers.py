
n=int(input("정수를 입력하세요(1 ≤ n ≤ 10,000,000)>"))
i=0
k=0
main=0
front_main=0
denominator=0
numerator=0
remainder=0

while True:
    k=k+1
    main=main+k
    front_main-=main-k
    if n>front_main and n<=main:
        quotient=main
        remainder=n-main
        break
  
while True:
    denominator=1
    numerator=main-1
    for i in remainder:
        denominator+=1
        numerator-=1
        print(denominator,"/",numerator)
        break
        
